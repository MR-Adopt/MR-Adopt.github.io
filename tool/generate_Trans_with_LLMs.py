"""
自动解析profile，填充prompt template, 生成prompt
"""
import multiprocessing
import random
import os, sys
import time
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing, java_parser, Evosuite_runner_general, compile_java_poj, java_test, request_LLMs

import construct_prompt, generate_Inputs_with_LLMs
import extract_code

import test_IT
import config
import re
from  filelock import FileLock

file_lock = FileLock("file.lock")


inputTrans_poj_dir = config.ROOT_DIR
OUTPUT_DIR = config.OUTPUT_DIR

Profile_GT_MTCs_wo_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_wo_IT/profile.json"
Profile_GT_MTCs_w_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_w_IT/profile.json"
Profile_GT_MTCs_wo_IT = json_processing.read(Profile_GT_MTCs_wo_IT_path)
Profile_GT_MTCs_w_IT = json_processing.read(Profile_GT_MTCs_w_IT_path)
raw_dir = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_w_IT/raw/"

package_statement = config.PACKAGE_STATEMENT
Junit_STATEMENT = config.JUNIT_STATEMENT
GT_ITrans_wo_dir = config.GT_ITRANS_WO_DIR
GT_ITrans_w_dir = config.GT_ITRANS_W_DIR
benchmark_src_dir = config.BENCHMARK_SRC_DIR

GT_CLASS_SUFFIX = config.GT_CLASS_SUFFIX
ITRANS_GENERATED_IT_DIR = config.ITRANS_GENERATED_IT_DIR
PATH_ITRANS_COMPILE_INFO = config.PATH_ITRANS_COMPILE_INFO

ITRANS_CACHE_DIR = config.ITRANS_CACHE_DIR
ITRANS_CACHE_GENERATED_TRANS_DIR = config.ITRANS_CACHE_GENERATED_TRANS_DIR

from utility.request_LLMs import model_symbols, symbols_model
from construct_prompt import Templates
# symbols_model: w, g3, g4, s2, qw, ml, dp
Setting = {
    # !!! MODIFY
    "model": f"{symbols_model['g3']}", 
    "Prompt_template":"5-1", # normal: 5-1, ablation input pairs: 4-1
    "number_of_request": 5,

    "number_of_shot":0,
    "temperature": 0.2,
    "overwritePreviousPromptResults":False,
    "overwritePreviousEvaluationResults":True,
    "skipCompileIfExist": False,
    "skipExecuteIfExist": False,
    "valid_Sinput_4_validation": True, # False: valid pairInputs 4 validation
    "parallel_size": 18,
    "index_of_request": 0,
    "test_generated_ITrans": ["O", "L"], # O: original test inputs, D: diff testing (for cases where original_MTC success), L:  LLM-generated test inputs based tests 
    
    # # !!! MODIFY, running
    "result_collect": True,
    "parallel": False,
    "one_by_one": False,
    "ablation": "", # No: "" , AIP: "_RQ1Baseline"/"_AblationinputPairs", ARF: "_AblationRefine", AVL: "_AblationValidate"
}

# switch, for refinement
switch = False
all_evaluation_result_of_generated_ITrans_function_path = f"{OUTPUT_DIR}trans/validation_generated_ITrans_{Setting['model']}_T{Setting['Prompt_template']}_Shot{Setting['number_of_shot']}_R{Setting['number_of_request']}_Temprature{Setting['temperature']}{Setting['ablation']}.json"


class transGenerator():
    @staticmethod
    def get_cache_dir(index_of_request):
        Setting['index_of_request'] = index_of_request
        cache_dir_name_for_this_setting = f"{Setting['model']}_T{Setting['Prompt_template']}_Shot{Setting['number_of_shot']}_Temprature{Setting['temperature']}_{Setting['index_of_request']}"
        return cache_dir_name_for_this_setting

    def __init__(self, index_of_request, MTC_item):
        Setting['index_of_request'] = index_of_request
        # cache_dir_name_for_this_setting = f"{Setting['model']}_T{Setting['Prompt_template']}_Shot{Setting['number_of_shot']}_Temprature{Setting['temperature']}_{Setting['index_of_request']}"
        # cache_dir_for_this_setting = f"{inputTrans_poj_dir}/cache/{cache_dir_name_for_this_setting}/"
        cache_dir_name_for_this_setting = transGenerator.get_cache_dir(index_of_request)
        cache_dir_for_this_setting = f"{config.ITRANS_CACHE_GENERATED_TRANS_DIR}{cache_dir_name_for_this_setting}/"
        Crafted_prompts_dir = f"{cache_dir_for_this_setting}prompts/"
        
        prompt_generated_ITrans_dir = f"{cache_dir_for_this_setting}generated_ITrans/"
        prompt_results_content_dir = f"{cache_dir_for_this_setting}prompts_results_content/"
        prompts_results_raw_dir = f"{cache_dir_for_this_setting}prompts_results_raw/"

        evaluation_execution_log_dir = f"{cache_dir_for_this_setting}exe_result/"
        evaluation_result_of_generated_ITrans_function_path = f"{cache_dir_for_this_setting}evaluation_generated_ITrans.json"
        compilation_log_dir = f"{cache_dir_for_this_setting}compilation_log/"
        
        file_processing.creatFolder_IfExistPass(cache_dir_for_this_setting)
        file_processing.creatFolder_IfExistPass(Crafted_prompts_dir)
        file_processing.creatFolder_IfExistPass(prompt_generated_ITrans_dir)
        file_processing.creatFolder_IfExistPass(prompt_results_content_dir)
        file_processing.creatFolder_IfExistPass(prompts_results_raw_dir)
        file_processing.creatFolder_IfExistPass(compilation_log_dir)
        file_processing.creatFolder_IfExistPass(evaluation_execution_log_dir)

        self.Setting = Setting
        self.prompt_template = Templates[Setting["Prompt_template"]]
        self.index_of_request = index_of_request
        self.MTC_item = MTC_item
        self.cache_dir_name_for_this_setting = cache_dir_name_for_this_setting
        self.cache_dir_for_this_setting = cache_dir_for_this_setting
        self.Crafted_prompts_dir = Crafted_prompts_dir
        self.prompt_generated_ITrans_dir = prompt_generated_ITrans_dir
        # self.cache_generated_valid_inputs_testing_Trans_dir = cache_generated_valid_inputs_testing_Trans_dir
        self.prompt_results_content_dir = prompt_results_content_dir
        self.prompts_results_raw_dir = prompts_results_raw_dir

        self.evaluation_result_of_generated_ITrans_function_path = evaluation_result_of_generated_ITrans_function_path
        self.compilation_log_dir = compilation_log_dir
        self.evaluation_execution_log_dir = evaluation_execution_log_dir

        self.few_shot_info = []
        self.few_shot_info_path = ""

        self.LLMI_input_generation_result = None
        self.LLMI_input_generation_result = generate_Inputs_with_LLMs.generate_inputs_for_one(MTC_item, generate_Inputs_with_LLMs.Setting, just_collect_result=True)
        self.LLMI_input_generation_result_for_evaluation = None
        self.LLMI_input_generation_result_for_evaluation = generate_Inputs_with_LLMs.generate_inputs_for_one(MTC_item, generate_Inputs_with_LLMs.for_evaluation_setting, just_collect_result=True)
        pass
        
# 暂时弃用，使用：input generation 中的同名函数
def generate_prompt_from_profile_pre(trans_generator):
    # prepare
    MTC_item = trans_generator.MTC_item
    Crafted_prompts_dir = trans_generator.Crafted_prompts_dir

    print(f"LOG: START, generate_prompt_from_profile: {MTC_item['FQS_testMethos']}")
    prompt = Templates[Setting["Prompt_template"]]
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    FQN_of_CUT = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]

    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
    invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]
    FQS_testMethos = MTC_item["FQS_testMethos"]
    if f"{invoked_package_FQN}." not in FQS_testMethos: # 说明：invoked_package_FQN 识别有误
        test_file_path = MTC_item["test_file_path"]
        test_file = file_processing.read_TXTfile(test_file_path)
        package_line = test_file.split("\n")[:0]
        for line in test_file.split("\n"):
            if line.startswith("package "): package_line = line; break
            if line.strip().startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip()
    test_file_path = MTC_item["test_file_path"]
    test_file = file_processing.read_TXTfile(test_file_path)
    package_line = test_file.split("\n")[:0]
    for line in test_file.split("\n"):
        if line.startswith("package "): package_line = line; break
        if line.strip().startswith("package "): package_line = line; break
    invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦

    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
    # test_file_path -> .java_ITrans
    """ get: code_of_testCase """
    # ITrans_test_file_path = test_file_path.replace(".java",".java_ITrans")
    # updated test file path
    test_file_name = test_file_path.split("/")[-1]
    test_file_path = f"{raw_dir}/{test_file_name}_ITrans" # mark
    ITrans_test_file_path = test_file_path.replace(".java_ITrans",".java").replace(".java",".java_ITrans")
    # TODO: refer to central/local poj raw folder.  
    code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}_crafted", function="getMethodAndRelatedFields")
    if "empty()" in code_of_testCase:
        code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}_h", function="getMethodAndRelatedFields")
        if "empty()" in code_of_testCase:
            code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}", function="getMethodAndRelatedFields")
    code_of_testCase = code_of_testCase.replace("\n\n", "\n");
    # print( "code_of_testCase: ", code_of_testCase )

    """ get: sourceInputs and followUpInputs  """
    sourceInputsContent = MTC_item["sourceInput"]
    followUpInputsContent = MTC_item["followUpInput"]
    sourceInputs = []
    followUpInputs = []
    # countInputs = 1
    for sourceinput in sourceInputsContent:
        sourceInputs.append( f"`{sourceinput['expression']}`" )
    for followUpInput in followUpInputsContent:
        followUpInputs.append( f"`{followUpInput['expression']}`" )
    
    """ get: signature/skeleton of ITrans function """
    # if Setting["Prompt_template"] in ["2","3-1","3-2"]:
    if "type" not in MTC_item: 
        if MTC_item["withInputTransformation"]: MTC_item["type"] = "w_ITrans"
        else: MTC_item["type"] = "wo_ITrans"
    if MTC_item["type"] == "wo_ITrans":
        GT_ITrans_path = f"{GT_ITrans_wo_dir}{invoked_package_FQN.replace('.','/')}/{processed_crafted_GT_MTC_test_class_name}{GT_CLASS_SUFFIX}.java"
    elif MTC_item["type"] == "w_ITrans":
        GT_ITrans_path = f"{GT_ITrans_w_dir}{invoked_package_FQN.replace('.','/')}/{processed_crafted_GT_MTC_test_class_name}{GT_CLASS_SUFFIX}.java"
    GT_ITrans_class = file_processing.read_TXTfile(GT_ITrans_path)
    pattern = r'public static [a-zA-Z0-9_,.?()\[\]<> ]* inputTransformation[a-zA-Z0-9_,.?()\[\]<> ]*{'
    matches = re.findall(pattern, GT_ITrans_class)
    ITransFunction = "public static Object inputTransformation()"
    if len( matches ) ==0:
        print("ERROR: no inputTransformation function in GT ITrans class")
        print( f"GT_ITrans_path: {GT_ITrans_path}" )
    else:
        ITransFunction = matches[0].strip("{")

    """ get: followUpInputs (returnFormat)  """
    returnFollowUp = ""
    if len(followUpInputsContent)>1:
        FUI_expressions = []
        for followUpInput in followUpInputsContent:
            FUI_type = followUpInput["type"]
            FUI_expression = followUpInput["expression"]
            stmt = f"{FUI_type} {FUI_expression} = "
            returnFollowUp += stmt + "\n\t\t"
            FUI_expressions.append(FUI_expression)
        argumens_str = (", ").join(FUI_expressions)
        return_stmt = f"List<Object> transformed_inputs = Arrays.asList({argumens_str});\n\t\t"
        return_stmt += "return transformed_inputs;"
        returnFollowUp += return_stmt
        
    else:
        FUI_type = followUpInputsContent[0]["type"]
        FUI_expression = followUpInputsContent[0]["expression"]

        stmt = f"{FUI_type} {FUI_expression} = "
        returnFollowUp += stmt + "\n\t\t"
        returnFollowUp += f"return {FUI_expression};"


    """ replace  """
    prompt = prompt.replace("$FQNofCUT$", FQN_of_CUT)
    prompt = prompt.replace("$codeOfTestCase$", code_of_testCase)
    prompt = prompt.replace("$sourceInputs$", (",").join(sourceInputs))
    prompt = prompt.replace("$followUpInputs$", (",").join(followUpInputs))
    # prompt = prompt.replace("\n\n", "\n");prompt = prompt.replace("\n\n", "\n");prompt = prompt.replace("\n\n", "\n")
    prompt = prompt.replace("$ITransClass$", processed_crafted_GT_MTC_test_class_name)
    # prompt = prompt.replace("$ITransClass$", processed_crafted_GT_MTC_test_class_name)
    prompt = prompt.replace("$ITransFunction$", ITransFunction)
    prompt = prompt.replace("$returnTransformedInputs$", returnFollowUp)

    file_processing.write_TXTfile(path = f"{Crafted_prompts_dir}{processed_crafted_GT_MTC_test_class_name}.md", content=prompt)
    print(f"LOG: END, generate_prompt_from_profile: {MTC_item['FQS_testMethos']}")


def generate_prompt_from_profile(trans_generator):
    """prompt info & system message """
    trans_generator = construct_prompt.generate_prompt_from_profile(trans_generator, task_type="trans_generation")

    """ few shot info """
    if trans_generator.Setting["number_of_shot"]>0:
        trans_generator = construct_prompt.generate_few_shot_info(trans_generator)

    return trans_generator


def generate_ITrans_by_prompting(trans_generator):
    # prepare
    MTC_item = trans_generator.MTC_item
    Crafted_prompts_dir = trans_generator.Crafted_prompts_dir
    prompt_results_content_dir = trans_generator.prompt_results_content_dir
    prompts_results_raw_dir = trans_generator.prompts_results_raw_dir
    prompt_generated_ITrans_dir = trans_generator.prompt_generated_ITrans_dir
    system_message = trans_generator.prompt_system_message
    promt_id = trans_generator.promt_id
    prompt_path = trans_generator.prompt_path
    prompt = trans_generator.promt_content
    few_shot_info = trans_generator.few_shot_info


    # test_file_path = MTC_item["test_file_path"]
    # test_simple_name = MTC_item["test_simple_name"]
    # MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    # processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
    
    # prompt_path = f"{Crafted_prompts_dir}{processed_crafted_GT_MTC_test_class_name}.md"
    # prompt = file_processing.read_TXTfile(prompt_path)
    # promt_id = processed_crafted_GT_MTC_test_class_name
    """ prompt """
    prompt_messages_path = prompt_path.replace(".md","_messages.json")
    response_content_path = f"{prompt_results_content_dir}{promt_id}.md"
    response_content = ''
    if not Setting["overwritePreviousPromptResults"] and file_processing.pathExist(response_content_path):
        response_content = file_processing.read_TXTfile(response_content_path)
    elif "gpt" in Setting["model"].lower(): 
        response_content = request_LLMs.request_GPT(prompt, Setting["model"], promt_id, Setting["temperature"],prompts_results_raw_dir, prompt_results_content_dir, system_message, few_shot_info, prompt_messages_path)
    else:
        response_content = request_LLMs.request_fastChat(prompt, Setting["model"], promt_id, Setting["temperature"],prompts_results_raw_dir, prompt_results_content_dir, system_message, few_shot_info, prompt_messages_path)

    """ extract and post-process generated ITrans class """
    generated_class = request_LLMs.extract_generated_ITrans_class(response_content, promt_id,prompt_generated_ITrans_dir)
    if not generated_class:
        print(f"LOG: generated_class is empty, promt_id: {promt_id}")
        file_processing.write_TXTfile(path=f"{prompt_generated_ITrans_dir}{promt_id}.java", content="empty")
    else:
        generated_class = post_process_ITrans(generated_class,MTC_item)
        file_processing.write_TXTfile(path=f"{prompt_generated_ITrans_dir}{promt_id}.java", content=generated_class)


def post_process_ITrans(generated_class,MTC_item):
    """ package_statement """
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
    invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]
    FQS_testMethos = MTC_item["FQS_testMethos"]
    MTC_class_test_file = MTC_item["test_file_path"]
    MTC_class_test_file_content = file_processing.read_TXTfile(MTC_class_test_file)
    if f"{invoked_package_FQN}." not in FQS_testMethos: # 说明：invoked_package_FQN 识别有误
        # test_file = file_processing.read_TXTfile(MTC_class_test_file)
        package_line = MTC_class_test_file_content.split("\n")[:0]
        for line in MTC_class_test_file_content.split("\n"):
            if line.startswith("package "): package_line = line; break
            if line.strip().startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip()
    
    test_file_path = MTC_item["test_file_path"]
    test_file = file_processing.read_TXTfile(test_file_path)
    package_line = test_file.split("\n")[:0]
    for line in test_file.split("\n"):
        if line.startswith("package "): package_line = line; break
        if line.strip().startswith("package "): package_line = line; break
    invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦

    package_statement = f"package {invoked_package_FQN};"
    # print("LOG:generated_class 1: ", generated_class)

    # using re to identify "package [a-zA-Z0-9.]*;" and replace it with "package [a-zA-Z0-9.]*.ITrans;"
    pattern = r'package [a-zA-Z0-9.]*;'
    matches = re.findall(pattern, generated_class)
    if len( matches ) >1:
        print( "len( matches ) >1:", len(matches) )
    elif len( matches ) ==1:
        generated_class = generated_class.replace(matches[0], f"{package_statement}")
    elif len( matches ) ==0:
        generated_class = f"{package_statement}\n\n{generated_class}"
    # print("LOG:generated_class 2: ", generated_class)

    """ add junit """
    pattern = r'@Test'
    matches = re.findall(pattern, generated_class)
    if len( matches ) >0: # 说明有生成test
        if Junit_STATEMENT not in generated_class: # 说明没有import junit statement
            generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{Junit_STATEMENT}")
    # print("LOG:generated_class 2.: ", generated_class)
    """ add CUT in import statements """
    """ add Trans template needed dependency """
    if "baseline" in Setting["ablation"].lower() or "_AblationRefine" in Setting["ablation"]:
        import_dependencies_CUT = []
    else:
        import_dependencies_CUT = MTC_item["dependency"].split(";") # GT

        searched_involvded_dependencies = []
        searched_definedClassesORdependencies = []
        """ import involved depedency """
        try:
            """ get defined variables in inputTransformation function """
            # tem store the file for javaparser
            FQS_testMethos_name = FQS_testMethos.split(".")[-1].replace("()","")
            tem_store_IT_file_path = MTC_class_test_file.replace(".java",".tmp_IT")
            file_processing.write_TXTfile(path=tem_store_IT_file_path, content=generated_class)
            function = "getInvolvedClassInMethod" # getDeclaredVariablesInMethod getMethod getDeclaredVariablesInMethod
            method_name=f"inputTransformation_{FQS_testMethos_name}"
            involvedClasses = []
            involvedClass_str = java_parser.getInvolvedClassInMethod(tem_store_IT_file_path, method_name, function)
            # IntArrayList:a2;int:i;boolean:trimFlag2;List<Object>:transformed_inputs
            involvedClasses = involvedClass_str.replace(":"," ").replace("\n"," ").split(";")

            java_primitive_types = ['byte', 'short', 'int', 'long', 'float', 'double', 'boolean', 'char', 'String']
            defined_varible_Types = [ ele.split(" ")[0] for ele in involvedClasses if ele.split(" ")[0] not in java_primitive_types]
            defined_varible_Types = list(set(defined_varible_Types))
            """ add template needed dependency """
            # search the poj dir to find java file named as type
            poj_dir = MTC_class_test_file.split("src/")[0]
            files_path = file_processing.walk_FileDir(poj_dir)
            # and then, give me the fully-qualified name of this class
            if len(defined_varible_Types) > 0:
                for file in files_path:
                    if file.endswith(".java"):
                        class_name = file.split("/")[-1].replace(".java", "")
                        if class_name in defined_varible_Types:
                            file_content = file_processing.read_TXTfile(file)
                            package_line_here = file_content.split("\n")[:0]

                            for line in file_content.split("\n"):
                                if line.startswith("package "): package_line_here = line; break
                            package_FQN = package_line_here.replace('package ','').replace(';','').strip() # 最准确啦
                            class_FQN = f"{package_FQN}.{class_name}"
                            searched_involvded_dependencies.append(class_FQN)   
                            searched_definedClassesORdependencies.append(class_FQN) 
        except Exception as e:
            print("LOG: import involved depedency error: ", e)
        
        if len(searched_definedClassesORdependencies) > 0:
            print("LOG: searched_definedClassesORdependencies>0: ", searched_definedClassesORdependencies)
            if switch: # refinement: add dependency
                for ele in searched_definedClassesORdependencies:
                    if ele not in import_dependencies_CUT:
                        import_dependencies_CUT.append(ele)

    import_dependencies_template_need = [ "java.util.List", "java.util.Arrays"]
    import_dependencies = import_dependencies_CUT + import_dependencies_template_need
    import_statement = ("\n").join( [f"import {ele};" for ele in import_dependencies if f".{ele.split('.')[-1]};" not in generated_class ] ) # avoid duplicate import
    generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{import_statement}")
    # print("LOG:generated_class 3: ", generated_class)

    """ add original MTC class's dependency """
    # check if the dependency is in the generated class
    # get all import statements in MTC_class_test_file_content
    origianl_MTC_import_statements_list= []
    for line in MTC_class_test_file_content.split("\n"):
        if line.startswith("import "):
            origianl_MTC_import_statements_list.append(line)
    
    origianl_MTC_import_statements_block = ""
    for ele in origianl_MTC_import_statements_list:
        ele_class = ele.split('.')[-1]
        if f"{ele}" not in generated_class and f".{ele_class}" not in generated_class: # avoid duplicate import
            origianl_MTC_import_statements_block += f"{ele}\n"
    # origianl_MTC_import_statements_block = ("\n").join([ ele for ele in origianl_MTC_import_statements_list if f".{ele.split('.')[-1]}" not in generated_class]) # avoid duplicate import
    generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{origianl_MTC_import_statements_block}")
    # print("LOG:generated_class 4: ", generated_class)

    """ exclude irrelevant code in input transformation function """
    # # udpate, exclude irrelevant code in input transformation function
    if switch: # refinement: exclude irrelevant code in input transformation function
        generated_code_block = generated_class
        extracted_code = extract_code.variableDefExtractor(generated_code_block, followUpInputs_TypeAndVariable, extract_code_from_MTC=False).extract_variable_def_code()
        generated_class = extracted_code

    # pre_generated_class = generated_class
    # if generated_class != pre_generated_class:
    #     print("LOG: generated_class != pre_generated_class", generated_class, pre_generated_class)
    
    sourceInputsContent = MTC_item["sourceInput"]
    followUpInputsContent = MTC_item["followUpInput"]
    followUpInputs_TypeAndVariable = []
    if len(followUpInputsContent) >1:
        followUpInputs_TypeAndVariable = ["List<Object> transformed_inputs"]
    else:
        followUpInput = followUpInputsContent[0]
        followUpInputs_TypeAndVariable.append( f"{followUpInput['type']} {followUpInput['expression']}" )
    # """ get all_relevant_variables   """
    # tem store the file for javaparser
    tem_store_IT_file_path = MTC_class_test_file.replace(".java",".tmp_IT")
    file_processing.write_TXTfile(path=tem_store_IT_file_path, content=generated_class)
    FQS_testMethos_name = FQS_testMethos.split(".")[-1].replace("()","")
    function = "getMethod" # getDeclaredVariablesInMethod getMethod
    method_name=f"inputTransformation_{FQS_testMethos_name}"
    defined_varible_TypeAndname = []
    original_method_content = java_parser.get_method_body_or_related_class_field(tem_store_IT_file_path, method_name, function)
    
    all_relevant_variables =  extract_code.variableDefExtractor(original_method_content, followUpInputs_TypeAndVariable).get_all_relevant_variables()
    all_relevant_variables_str = ""
    for var in all_relevant_variables:
        all_relevant_variables_str += f'{var["type"]}/{var["name"]}:'
    all_relevant_variables_str = all_relevant_variables_str.rstrip(":")
    # """ get udpated_function   """ # to be improved with more concise implementation
    udpated_method_content = java_parser.getVaribleRelevantCode(tem_store_IT_file_path, method_name, all_relevant_variables_str.rstrip(":"), function)
    if udpated_method_content != original_method_content:
        print("LOG: udpated_method_content != original_method_content ")
        print("LOG: original_method_content:\n ", original_method_content)
        print("LOG: udpated_method_content:\n ", udpated_method_content)
        if switch:
            generated_class = generated_class.replace(original_method_content, udpated_method_content)

    return generated_class


def post_process_ITrans_pre(generated_class,MTC_item):
    """ package_statement """
    # using re to identify "package [a-zA-Z0-9.]*;" and replace it with "package [a-zA-Z0-9.]*.ITrans;"
    pattern = r'package [a-zA-Z0-9.]*;'
    matches = re.findall(pattern, generated_class)
    if len( matches ) >1:
        print( "len( matches ) >1:", len(matches) )
    elif len( matches ) ==1:
        generated_class = generated_class.replace(matches[0], f"{package_statement}")
    elif len( matches ) ==0:
        generated_class = f"{package_statement}\n\n{generated_class}"

    """ add junit """
    pattern = r'@Test'
    matches = re.findall(pattern, generated_class)
    if len( matches ) >0: # 说明有生成test
        if Junit_STATEMENT not in generated_class: # 说明没有import junit statement
            generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{Junit_STATEMENT}")

    """ add CUT in import statements """
    import_dependencies = MTC_item["dependency"].split(";")
    import_statement = ("\n").join( [f"import {ele};" for ele in import_dependencies ] )
    generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{import_statement}")

    return generated_class


# new: for testing in the original poj
def test_generated_ITrans(trans_generator, skipCompileIfExist=True):
    """
    prepare: cp GT_ITrans -> src/; and compile;if success: 
    cp generated_MTC_ITrans -> src/; and compile > .log;
    if success: do testing > .log (refer to AutoMR的做法)
    复位: cp GT_ITrans -> src/; and compile;
    """
    # prepare
    MTC_item = trans_generator.MTC_item
    prompt_generated_ITrans_dir = trans_generator.prompt_generated_ITrans_dir
    evaluation_execution_log_dir = trans_generator.evaluation_execution_log_dir
    log_dir = trans_generator.compilation_log_dir

    Test_result = {"MTC_item":MTC_item, 
                   "GTIT_compile_result": None, 
                   "generatedIT_compile_result": None, 
                   "OriginalMTC_testing_GTIT_result": None, 
                   "OriginalMTC_testing_generatedIT_result": None,
                   "ES_testing_GTIT_result": None, # 这一项很快就没意义，因为是differential testing
                   "ES_testing_generatedIT_result": None,
                   "LLMI_testing_GTIT_result": None, # LLMI: LLM generated new inputs
                   "LLMI_testing_generatedIT_result": None, # LLMI: LLM generated new inputs
                   "LLMI_testing_generatedIT_result_evaluation": None # LLMI: LLM generated new inputs for evaluation
    }
    poj_name = MTC_item["poj_name"]
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"

    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
    invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]
    FQS_testMethos = MTC_item["FQS_testMethos"]
    if f"{invoked_package_FQN}." not in FQS_testMethos: # 说明：invoked_package_FQN 识别有误
        test_file_path = MTC_item["test_file_path"]
        test_file = file_processing.read_TXTfile(test_file_path)
        package_line = test_file.split("\n")[:0]
        for line in test_file.split("\n"):
            if line.startswith("package "): package_line = line; break
            if line.strip().startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip()
    
    test_file_path = MTC_item["test_file_path"]
    test_file = file_processing.read_TXTfile(test_file_path)
    package_line = test_file.split("\n")[:0]
    for line in test_file.split("\n"):
        if line.startswith("package "): package_line = line; break
        if line.strip().startswith("package "): package_line = line; break
    invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦

    print("test generated ITrans: ", invoked_methods_FQS, processed_crafted_GT_MTC_test_class_name)
    """ testing GT ITrans """
    # exe_result = test_IT.originalMTC_test_IT(MTC_item, GTorGenerated="GT")
    # Test_result["OriginalMTC_testing_GTIT_result"] = exe_result
    # exe_result = test_IT.ES_test_IT(MTC_item, GTorGenerated="GT")
    # Test_result["ES_testing_GTIT_result"] = exe_result
    # exe_result = test_IT.Diff_test_IT(MTC_item, GTorGenerated="GT")
    # Test_result["Diff_testing_GTIT_result"] = exe_result
    # # print("LOG: GT ", "exe_result: ", exe_result)
    
    
    """ compile generated ITrans in original poj """
    poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name
    dir_of_generated_ITrans_in_original_poj = f"{poj_ITRANS_GENERATED_IT_DIR}{invoked_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(dir_of_generated_ITrans_in_original_poj)
    path_of_generated_ITrans_in_original_poj = f"{dir_of_generated_ITrans_in_original_poj}{processed_crafted_GT_MTC_test_class_name}.java"
    # 复位: rm generated ITrans in original poj
    file_processing.remove_file(path_of_generated_ITrans_in_original_poj)
    file_processing.remove_file(path_of_generated_ITrans_in_original_poj.replace(".java",".class"))
    # copy: cache -> original poj
    path_of_generated_ITrans_in_cache = f"{prompt_generated_ITrans_dir}{processed_crafted_GT_MTC_test_class_name}.java"
    file_processing.copyFile(source=path_of_generated_ITrans_in_cache,target=path_of_generated_ITrans_in_original_poj)
    # compile
    if skipCompileIfExist and file_processing.pathExist(path_of_generated_ITrans_in_cache.replace(".java",".class")):
        file_processing.copyFile(source=path_of_generated_ITrans_in_cache.replace(".java",".class"),target=path_of_generated_ITrans_in_original_poj.replace(".java",".class"))
        Test_result["generatedIT_compile_result"] = True
        print(f"Skip: {path_of_generated_ITrans_in_cache} has been compiled")
    else:
        poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
        poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
        poj_build_tool = poj_compilation_info["build_tool"][0]
        jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

        CMD_CD = f"cd {poj_dir};"
        PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)
        # path_of_generated_ITrans_in_original_poj
        # generated_dot_class_path = path_of_generated_ITrans_in_original_poj.replace(".java", ".class")
        cmd_result = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp="", Path_TestFile_to_compile = path_of_generated_ITrans_in_original_poj, PATH_JAVAC=PATH_JAVAC, log_dir=log_dir)
        if cmd_result != 0:
            Test_result["generatedIT_compile_result"] = False
        else:
            Test_result["generatedIT_compile_result"] = True
            # 放回cache中，备份一下。
            file_processing.copyFile(source=path_of_generated_ITrans_in_original_poj.replace(".java",".class") ,target=path_of_generated_ITrans_in_cache.replace(".java",".class"))

    """ testing generated ITrans """
    # OriginalMTC_testing_generatedIT_result
    exe_result = test_IT.originalMTC_test_IT(MTC_item, GTorGenerated="Generated",EXE_RESULT_DIR=evaluation_execution_log_dir)
    Test_result["OriginalMTC_testing_generatedIT_result"] = exe_result

    # LLMI_testing_generatedIT_result
    exe_result = test_IT.LLMI_test_IT(MTC_item, GTorGenerated="Generated",EXE_RESULT_DIR=evaluation_execution_log_dir, passIfexecuted=Setting["skipExecuteIfExist"], valid_Sinput_4_validation=Setting["valid_Sinput_4_validation"], LLMI_input_generation_result=trans_generator.LLMI_input_generation_result)
    Test_result["LLMI_testing_generatedIT_result"] = exe_result

    # evalution: a new group inputs for evaluating
    exe_result = test_IT.LLMI_test_IT(MTC_item, GTorGenerated="Generated",EXE_RESULT_DIR=evaluation_execution_log_dir, passIfexecuted=Setting["skipExecuteIfExist"], valid_Sinput_4_validation=Setting["valid_Sinput_4_validation"], LLMI_input_generation_result=trans_generator.LLMI_input_generation_result_for_evaluation, for_evaluation=True)
    # Test_result["LLMI_testing_generatedIT_result"] = exe_result
    Test_result["LLMI_testing_generatedIT_result_evaluation"] = exe_result
    
    # # not readly: TODO
    # exe_result = test_IT.ES_test_IT(MTC_item, GTorGenerated="Generated",EXE_RESULT_DIR=evaluation_execution_log_dir)
    # Test_result["ES_testing_generatedIT_result"] = exe_result
    # exe_result = test_IT.Diff_test_IT(MTC_item, GTorGenerated="Generated",EXE_RESULT_DIR=evaluation_execution_log_dir)
    # Test_result["Diff_testing_generatedIT_result"] = exe_result
    Test_result["ES_testing_generatedIT_result"] = None
    Test_result["Diff_testing_generatedIT_result"] = None

    """ write validation result """
    trans_validation_result = Test_result
    evaluation_result_of_generated_Trans = []
    evaluation_result_of_generated_ITrans_function_path = trans_generator.evaluation_result_of_generated_ITrans_function_path
    with file_lock:
        if file_processing.pathExist(evaluation_result_of_generated_ITrans_function_path):
            with open (evaluation_result_of_generated_ITrans_function_path, "r") as f: # 句柄打开，防止文件读写冲突。。
                evaluation_result_of_generated_Trans = json_processing.read(evaluation_result_of_generated_ITrans_function_path)
                for ele in evaluation_result_of_generated_Trans:
                    if ele["MTC_item"]["FQS_testMethos"] == MTC_item["FQS_testMethos"]:
                        evaluation_result_of_generated_Trans.remove(ele)
                evaluation_result_of_generated_Trans.append(trans_validation_result)
                json_processing.write( json_content=evaluation_result_of_generated_Trans, path=evaluation_result_of_generated_ITrans_function_path)
        else:
            evaluation_result_of_generated_Trans.append(trans_validation_result)
            json_processing.write( json_content=evaluation_result_of_generated_Trans, path=evaluation_result_of_generated_ITrans_function_path)

    """ 复位: rm generated ITrans in original poj """
    file_processing.remove_file(path_of_generated_ITrans_in_original_poj)
    file_processing.remove_file(path_of_generated_ITrans_in_original_poj.replace(".java",".class"))

    return Test_result


def parallel_generate_prompt_from_profile():
    # Create a multiprocessing Pool
    parallel_size = Setting["parallel_size"]
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    all_GT_MTCs = [ MTC_item  for  MTC_item in all_GT_MTCs if "skip" not in MTC_item or MTC_item["skip"] == False ]
    with multiprocessing.Pool(processes=parallel_size) as pool:
        # Use pool.imap or pool.map for ordered results
        pool.map(generate_prompt_from_profile, all_GT_MTCs)

def parallel_generate_ITrans_by_prompting():
    # Create a multiprocessing Pool
    parallel_size = Setting["parallel_size"]
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    all_GT_MTCs = [ MTC_item  for  MTC_item in all_GT_MTCs if "skip" not in MTC_item or MTC_item["skip"] == False ]
    with multiprocessing.Pool(processes=parallel_size) as pool:
        # Use pool.imap or pool.map for ordered results
        pool.map(generate_ITrans_by_prompting, all_GT_MTCs)

def result_collect(Setting):
    """_summary_
    collect all results
    summary:
        all_subject: x
        compilation_success: x
        validation_pass_rate (average): x
    meta_list:
        compilation_success:[FQN] // best of all candidates
        validation_pass_rate: { // best of all
            FQN: {
                "percentage" : xx%
                "num_of_test_cases": 0,
                "num_of_passed_test_cases": 0,
                "index_of_request",0
            }
        }
    two options:
        1. choose the best of all k requests
        2. choose keep all requests results for detailed analysis
    """
    evaluation_result = {
        "summary_v2":{
            "all_subject": 0,
            "subject_size (pass original MTC)":0,
            "subject_size (with generated LLMI tests)":0,
            "subject_size (generated LLMI: pass at least one test)":0,
            "subject_size (generated LLMI: pass all tests)":0,
            "generated LLMI: pass_rate (average)": None,

            "subject_size (with valid LLMI tests)":0,
            "subject_size (valid LLMI: pass at least one test)":0,
            "subject_size (valid LLMI: pass all tests)":0,
            "valid LLMI: pass_rate (average)": None,
        },
        "summary":{
            "all_subject": 0,
            "compilation_success": 0,
            "subject_size (pass original MTC)":0,
            "subject_size (with LLMI tests)":0,
            "subject_size (LLMI: pass at least one test)":0,
            "subject_size (LLMI: pass all tests)":0,
            "validation_pass_rate (average: LLMI)": None
        },
        "meta_list":{
            "compilation_success":[],
            "validation_pass_rate (o. MTC)":{},
            "subject_size (pass original MTC)":[],
            "validation_pass_rate (LLMI)":{},
            "validation_pass_rate (LLMI) list":[],
            "subject_size (with LLMI tests)":[],
            "subject_size (LLMI: pass at least one test)":[],
            "subject_size (LLMI: pass all tests)":[],
            "compilation_unsuccess":{},
            "pass_both_O_and_all_LLMI":[],
            "fail_both_O_and_all_LLMI":[],
            "pass_O_but_fail_some_LLMI":[],
            "pass_some_LLMI_but_fail_O":[],
        }
    }
    all_subject = {}
    for index_of_request in range(Setting["number_of_request"]):
        index_of_request_str = index_of_request.__str__()
        evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][index_of_request_str] = {}
        evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][index_of_request_str] = {}


        cache_dir_name_for_this_setting = transGenerator.get_cache_dir(index_of_request)
        cache_dir_for_this_setting = f"{ITRANS_CACHE_GENERATED_TRANS_DIR}{cache_dir_name_for_this_setting}/"
        generated_Trans_of_this_setting = f"{cache_dir_for_this_setting}generateTrans/"
        evaluation_result_of_generated_ITrans_function_path = f"{cache_dir_for_this_setting}evaluation_generated_ITrans.json"
        result_single = []
        if file_processing.pathExist(evaluation_result_of_generated_ITrans_function_path):
            result_single = json_processing.read(evaluation_result_of_generated_ITrans_function_path)

        for MTC_result in result_single:
            FQS_testMethos = MTC_result["MTC_item"]["FQS_testMethos"]
            generatedIT_compile_result = MTC_result["generatedIT_compile_result"]
            OriginalMTC_testing_generatedIT_result = MTC_result["OriginalMTC_testing_generatedIT_result"]
            Diff_testing_generatedIT_result = MTC_result["Diff_testing_generatedIT_result"]
            LLMI_testing_generatedIT_result = MTC_result["LLMI_testing_generatedIT_result"]
            

            if FQS_testMethos not in all_subject: all_subject[FQS_testMethos] = f'w_ITrans: {MTC_result["MTC_item"]["withInputTransformation"]}'
            # meta_list: compilation_success
            if generatedIT_compile_result and FQS_testMethos not in evaluation_result["meta_list"]["compilation_success"]:
                evaluation_result["meta_list"]["compilation_success"].append(FQS_testMethos)

            # meta_list: validation_pass_rate 
            # original MTC
            OriginalMTC_pass_percentage = None
            if generatedIT_compile_result and "O" in Setting["test_generated_ITrans"] and OriginalMTC_testing_generatedIT_result:
                num_of_test_cases = OriginalMTC_testing_generatedIT_result["num_of_test_cases"]
                num_of_passed_test_cases = OriginalMTC_testing_generatedIT_result["num_of_passed_test_cases"]
                if num_of_test_cases>0:
                    # new_percentage: original percentage may be not correct 
                    new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                    OriginalMTC_pass_percentage = new_percentage
                    result_info_item = {
                                "percentage" : new_percentage,
                                "num_of_test_cases": num_of_test_cases,
                                "num_of_passed_test_cases": num_of_passed_test_cases,
                                "index_of_request": index_of_request,
                                "dir_generated_Trans": generated_Trans_of_this_setting,
                                "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                            }
                    evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][index_of_request_str][FQS_testMethos] = result_info_item
                    if new_percentage==1.0:
                        evaluation_result["meta_list"]["subject_size (pass original MTC)"].append(FQS_testMethos)
            
            # LLMI: LLM-generated test inputs
            LLMI_pass_percentage = None
            LLMI_size = None
            if generatedIT_compile_result and "L" in Setting["test_generated_ITrans"] and LLMI_testing_generatedIT_result:
                num_of_test_cases = LLMI_testing_generatedIT_result["num_of_test_cases"]
                num_of_passed_test_cases = LLMI_testing_generatedIT_result["num_of_passed_test_cases"]
                LLMI_size = num_of_test_cases
                if num_of_test_cases>0:
                    # new_percentage: original percentage may be not correct 
                    new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                    LLMI_pass_percentage = new_percentage
                    result_info_item = {
                                "percentage" : new_percentage,
                                "num_of_test_cases": num_of_test_cases,
                                "num_of_passed_test_cases": num_of_passed_test_cases,
                                "index_of_request": index_of_request,
                                "dir_generated_Trans": generated_Trans_of_this_setting,
                                "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                            }
                    evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][index_of_request_str][FQS_testMethos] = result_info_item
                    evaluation_result["meta_list"]["subject_size (with LLMI tests)"].append(FQS_testMethos)
                    if new_percentage==1.0:
                        evaluation_result["meta_list"]["subject_size (LLMI: pass all tests)"].append(FQS_testMethos)

            # differential testing, TODO
            # if generatedIT_compile_result and Setting["test_generated_ITrans"]=="D" and OriginalMTC_testing_generatedIT_result and Diff_testing_generatedIT_result:
            #     flag_collect_test_result=True
            #     num_of_test_cases = Diff_testing_generatedIT_result["num_of_test_cases"]
            #     num_of_passed_test_cases = Diff_testing_generatedIT_result["num_of_passed_test_cases"]
                        
            # meta list: option2, choose keep all requests results
            if LLMI_pass_percentage != None and OriginalMTC_pass_percentage != None:
                info_item = {"MTC": FQS_testMethos, "index_of_request": index_of_request,
                             "LLMI_size": LLMI_size, "LLMI_pass_percentage": LLMI_pass_percentage, "OriginalMTC_pass_percentage": OriginalMTC_pass_percentage}
                if LLMI_pass_percentage==1.0 and OriginalMTC_pass_percentage==1.0:
                    evaluation_result["meta_list"]["pass_both_O_and_all_LLMI"].append(info_item)
                if LLMI_pass_percentage==0.0 and OriginalMTC_pass_percentage<1.0: # in theory, OriginalMTC_pass_percentage==0/1
                    evaluation_result["meta_list"]["fail_both_O_and_all_LLMI"].append(info_item)
                if LLMI_pass_percentage<1.0 and OriginalMTC_pass_percentage==1.0:
                    evaluation_result["meta_list"]["pass_O_but_fail_some_LLMI"].append(info_item)
                if LLMI_pass_percentage>0.0 and OriginalMTC_pass_percentage<1.0:
                    evaluation_result["meta_list"]["pass_some_LLMI_but_fail_O"].append(info_item)
                if LLMI_pass_percentage>0.0:
                    evaluation_result["meta_list"]["subject_size (LLMI: pass at least one test)"].append(FQS_testMethos)
                evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"].append(LLMI_pass_percentage)

    # summary, the best result of all requests
    evaluation_result["summary"]["all_subject"] = len(all_subject)
    evaluation_result["summary"]["compilation_success"] = len(evaluation_result["meta_list"]["compilation_success"])
    evaluation_result["summary"]["subject_size (pass original MTC)"]  = len( set( evaluation_result["meta_list"]["subject_size (pass original MTC)"] ) )
    evaluation_result["summary"]["subject_size (with LLMI tests)"]  = len( set( evaluation_result["meta_list"]["subject_size (with LLMI tests)"] ) )
    evaluation_result["summary"]["subject_size (LLMI: pass at least one test)"]  = len( set( evaluation_result["meta_list"]["subject_size (LLMI: pass at least one test)"] ) )
    evaluation_result["summary"]["subject_size (LLMI: pass all tests)"]  = len( set( evaluation_result["meta_list"]["subject_size (LLMI: pass all tests)"] ) )
    evaluation_result["summary"]["validation_pass_rate (average: LLMI)"] = sum(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])/len(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])

    for ele in all_subject.keys():
        if ele not in evaluation_result["meta_list"]["compilation_success"]:
            evaluation_result["meta_list"]["compilation_unsuccess"][ele] = all_subject[ele]
    json_processing.write( json_content=evaluation_result, path=all_evaluation_result_of_generated_ITrans_function_path)

def result_collect_the_best_k(Setting, just_collect_results=False):
    """_summary_
    collect all results
    summary:
        all_subject: x
        compilation_success: x
        validation_pass_rate (average): x
    meta_list:
        compilation_success:[FQN] // best of all candidates
        validation_pass_rate: { // best of all
            FQN: {
                "percentage" : xx%
                "num_of_test_cases": 0,
                "num_of_passed_test_cases": 0,
                "index_of_request",0
            }
        }
    two options:
        1. choose the best of all k requests
        2. choose keep all requests results for detailed analysis
    """
    evaluation_result = {
        "summary_validation":{
            "all_subject": 0,
            "compilation_success": 0,
            "subject_size (pass original MTC)":0,
            "subject_size (with LLMI tests)":0,
            "subject_size (LLMI: pass at least one test)":0,
            "subject_size (LLMI: pass all tests)":0,
            "validation_pass_rate (average: LLMI)": None,
            "validation_pass_rate (average: LLMI+OMTC)": None,
            "subject_size (pass original MTC, but fail LLMI)":0,
            # "validation_pass_rate (average: o. MTC)": None,
            # "validation_pass_rate (average: LLMI)": None
            "subject_size (pass at least one Sinput: OMTCorLLMI)":0,
            "subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)":0,
        },
        "summary_evaluation":{
            "all_subject": 0,
            "compilation_success": 0,
            "subject_size (pass original MTC)":0,
            "subject_size (with LLMI tests)":0,
            "subject_size (LLMI: pass at least one test)":0,
            "subject_size (LLMI: pass all tests)":0,
            "pass_rate (average: LLMI)": None,
            "pass_rate (average: LLMI+OMTC)": None,
            "subject_size (pass original MTC, but fail LLMI)":0,
            # "validation_pass_rate (average: o. MTC)": None,
            # "validation_pass_rate (average: LLMI)": None
            "subject_size (pass at least one Sinput: OMTCorLLMI)":0,
            "subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)":0,
        },
        "meta_list":{
            "compilation_success":[],
            "validation_pass_rate (o. MTC)":{},
            "subject_size (pass original MTC)":[],

            "validation_pass_rate (LLMI)":{},
            "validation_pass_rate (LLMI) list":[],

            "subject_size (with LLMI tests)":[],
            "subject_size (LLMI: pass at least one test)": [],
            "subject_size (LLMI: pass all tests)":[],

            "compilation_unsuccess":{},

            "pass_both_O_and_all_LLMI":[],
            "fail_both_O_and_all_LLMI":[],
            "pass_O_but_fail_some_LLMI":[],
            "pass_some_LLMI_but_fail_O":[],

            "subject_size (pass at least one Sinput: OMTCorLLMI)":[],
            "subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)":[],
        },
        "meta_list_evaluation":{
            "evaluation_pass_rate (LLMI)": {},
            "evaluation_pass_rate (LLMI) list":[],
            # "subject_size (pass original MTC)": [],
            "subject_size (with LLMI tests)":[],
            "subject_size (LLMI: pass at least one test)": [],
            "subject_size (LLMI: pass all tests)":[],

            "pass_both_O_and_all_LLMI":[],
            "fail_both_O_and_all_LLMI":[],
            "pass_O_but_fail_some_LLMI":[],
            "pass_some_LLMI_but_fail_O":[],
        },

        "effectiveness_evaluation":{
            "summary_validation": {
                "valid_Sinput":0 ,
                "valid_Sinput_w_LLM_FUinput_only":0, 
                "valid_Sinput_w_Trans_FUinput_only":0, 
                "valid_Sinput_w_LLMandTrans_FUinput":0, 
                "valid_Sinput_wo_LLMorTrans_FUinput":0, 
                "valid_Sinput_wo_LLM_FUinput":0,
                "valid_Sinput_wo_LLM_but_with_Trans_FUinput":0,
                "Trans_success_rate":0,
                "LLM_success_rate":0
            },
            "summary_evaluation": {
                "valid_Sinput":0 ,
                "valid_Sinput_w_LLM_FUinput_only":0, 
                "valid_Sinput_w_Trans_FUinput_only":0, 
                "valid_Sinput_w_LLMandTrans_FUinput":0, 
                "valid_Sinput_wo_LLMorTrans_FUinput":0, 
                "valid_Sinput_wo_LLM_FUinput":0,
                "valid_Sinput_wo_LLM_but_with_Trans_FUinput":0,
                "Trans_success_rate":0,
                "LLM_success_rate":0
            },
            "meta_list_validation": {
                "valid_Sinput_w_LLM_FUinput_only": {},
                "valid_Sinput_w_Trans_FUinput_only": {},
                "valid_Sinput_w_LLMandTrans_FUinput": {},
                "valid_Sinput_wo_LLMorTrans_FUinput": {},
                "valid_Sinput_wo_LLM_FUinput":{},
                "valid_Sinput_wo_LLM_but_with_Trans_FUinput":{},
            },
            "meta_list_evaluation": {
                "valid_Sinput_w_LLM_FUinput_only": {},
                "valid_Sinput_w_Trans_FUinput_only": {},
                "valid_Sinput_w_LLMandTrans_FUinput": {},
                "valid_Sinput_wo_LLMorTrans_FUinput": {},
                "valid_Sinput_wo_LLM_FUinput":{},
                "valid_Sinput_wo_LLM_but_with_Trans_FUinput":{},
            }
        }
    }
    all_subject = {}
    random_MTC_best_idex = {} # for ablatio_study
    for index_of_request in range(Setting["number_of_request"]):
        cache_dir_name_for_this_setting = transGenerator.get_cache_dir(index_of_request)
        cache_dir_for_this_setting = f"{ITRANS_CACHE_GENERATED_TRANS_DIR}{cache_dir_name_for_this_setting}/"
        generated_Trans_of_this_setting = f"{cache_dir_for_this_setting}generateTrans/"
        evaluation_result_of_generated_ITrans_function_path = f"{cache_dir_for_this_setting}evaluation_generated_ITrans.json"
        result_single = []
        if file_processing.pathExist(evaluation_result_of_generated_ITrans_function_path):
            result_single = json_processing.read(evaluation_result_of_generated_ITrans_function_path)

        for MTC_result in result_single:
            FQS_testMethos = MTC_result["MTC_item"]["FQS_testMethos"]
            if FQS_testMethos not in random_MTC_best_idex: 
                # random index from 0~4
                random_best_index = random.randint(0,Setting["number_of_request"]-1) # hardcoded [0,4]
                random_MTC_best_idex[FQS_testMethos] = random_best_index
            generatedIT_compile_result = MTC_result["generatedIT_compile_result"]
            OriginalMTC_testing_generatedIT_result = MTC_result["OriginalMTC_testing_generatedIT_result"]
            Diff_testing_generatedIT_result = MTC_result["Diff_testing_generatedIT_result"]
            LLMI_testing_generatedIT_result = MTC_result["LLMI_testing_generatedIT_result"]
            LLMI_testing_generatedIT_result_evaluation = MTC_result["LLMI_testing_generatedIT_result_evaluation"]

            
            if FQS_testMethos not in all_subject: all_subject[FQS_testMethos] = f'w_ITrans: {MTC_result["MTC_item"]["withInputTransformation"]}'
            # meta_list: compilation_success
            if generatedIT_compile_result and FQS_testMethos not in evaluation_result["meta_list"]["compilation_success"]:
                evaluation_result["meta_list"]["compilation_success"].append(FQS_testMethos)

            # meta_list: validation_pass_rate 
            # original MTC
            OriginalMTC_pass_percentage = None
            if generatedIT_compile_result and "O" in Setting["test_generated_ITrans"] and OriginalMTC_testing_generatedIT_result:
                num_of_test_cases = OriginalMTC_testing_generatedIT_result["num_of_test_cases"]
                num_of_passed_test_cases = OriginalMTC_testing_generatedIT_result["num_of_passed_test_cases"]
                if num_of_test_cases>0:
                    # new_percentage: original percentage may be not correct 
                    new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                    OriginalMTC_pass_percentage = new_percentage
                    result_info_item = {
                                "percentage" : new_percentage,
                                "num_of_test_cases": num_of_test_cases,
                                "num_of_passed_test_cases": num_of_passed_test_cases,
                                "index_of_request": index_of_request,
                                "dir_generated_Trans": generated_Trans_of_this_setting,
                                "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                            }

                    if FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"]:
                        existing_percentage = evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"]
                        if new_percentage > existing_percentage: # previous try
                            evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos] = result_info_item
                    else:
                        evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos] = result_info_item
                    if new_percentage==1.0:
                        # evaluation_result["summary_validation"]["subject_size (pass original MTC)"] += 1
                        evaluation_result["meta_list"]["subject_size (pass original MTC)"].append(FQS_testMethos)
            
            # LLMI: LLM-generated test inputs (validation)
            LLMI_pass_percentage = -1
            LLMI_size = None
            flag_best_one = 0 # 0：False, 1: replace, 2: append
            if generatedIT_compile_result and "L" in Setting["test_generated_ITrans"] and LLMI_testing_generatedIT_result:
                num_of_test_cases = LLMI_testing_generatedIT_result["num_of_test_cases"]
                num_of_passed_test_cases = LLMI_testing_generatedIT_result["num_of_passed_test_cases"]
                failure_info = list( LLMI_testing_generatedIT_result["failure_info"].keys() )
                failure_test_cases_list = []
                for test_class_FQN in LLMI_testing_generatedIT_result["failure_info"].keys():
                    failure_test_cases_list.extend( list(LLMI_testing_generatedIT_result["failure_info"][test_class_FQN].keys()) )
                passed_test_cases_list = []
                for ele_list in LLMI_testing_generatedIT_result["passed_test_cases_list"]:
                    for ele_ in ele_list: passed_test_cases_list.append(ele_)
                passed_test_cases_list = list(set( passed_test_cases_list ))
                LLMI_size = num_of_test_cases # TO mind: if no LLMi in the validation step, how to do? [TODO]

                if num_of_test_cases>0:
                    # new_percentage: original percentage may be not correct 
                    new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                    LLMI_pass_percentage = new_percentage
                    result_info_item = { # validation_result_info_item
                                "percentage" : new_percentage,
                                "num_of_test_cases": num_of_test_cases,
                                "num_of_passed_test_cases": num_of_passed_test_cases,
                                "index_of_request": index_of_request,
                                "dir_generated_Trans": generated_Trans_of_this_setting,
                                "failure_info": failure_info,
                                "failure_test_cases_list": failure_test_cases_list,
                                "passed_test_cases_list": passed_test_cases_list,
                                "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                            }
                    if FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"]:
                        existing_percentage = evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos][0]["percentage"]
                        if new_percentage > existing_percentage: # """ 进行替换, best k """
                            evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos] = [result_info_item]; flag_best_one = 1
                        if new_percentage == existing_percentage:
                            evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos].append(result_info_item); flag_best_one = 2
                    else:
                        evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos] = [result_info_item]; flag_best_one = 1

                    # evaluation_result["summary_validation"]["subject_size (with LLMI tests)"] += 1
                    evaluation_result["meta_list"]["subject_size (with LLMI tests)"].append(FQS_testMethos)
                    if new_percentage==1.0:
                        # evaluation_result["summary_validation"]["subject_size (LLMI: pass all tests)"] += 1
                        evaluation_result["meta_list"]["subject_size (LLMI: pass all tests)"].append(FQS_testMethos)


            
            # LLMI: LLM-generated test inputs (evaluation) LLMI_testing_generatedIT_result_evaluation
            if generatedIT_compile_result and LLMI_testing_generatedIT_result_evaluation:            
                # if ablation, and is the random best one, put it; 
                # if ablation, is not the random best one, skip; 
                # if not ablation,就走常规流程
                if Setting["ablation"] == "_AblationValidate":
                    if index_of_request == random_MTC_best_idex[FQS_testMethos]:
                        if generatedIT_compile_result and LLMI_testing_generatedIT_result_evaluation:
                            num_of_test_cases = LLMI_testing_generatedIT_result_evaluation["num_of_test_cases"]
                            num_of_passed_test_cases = LLMI_testing_generatedIT_result_evaluation["num_of_passed_test_cases"]
                            failure_info = list( LLMI_testing_generatedIT_result_evaluation["failure_info"].keys() )
                            failure_test_cases_list = []
                            for test_class_FQN in LLMI_testing_generatedIT_result_evaluation["failure_info"].keys():
                                failure_test_cases_list.extend( list(LLMI_testing_generatedIT_result_evaluation["failure_info"][test_class_FQN].keys()) )
                            passed_test_cases_list = []
                            for ele_list in LLMI_testing_generatedIT_result_evaluation["passed_test_cases_list"]:
                                for ele_ in ele_list: passed_test_cases_list.append(ele_)
                            passed_test_cases_list = list(set( passed_test_cases_list ))
                            LLMI_size = num_of_test_cases
                            evaluation_result_info_item = {
                                        "percentage" : new_percentage,
                                        "num_of_test_cases": num_of_test_cases,
                                        "num_of_passed_test_cases": num_of_passed_test_cases,
                                        "index_of_request": index_of_request,
                                        "dir_generated_Trans": generated_Trans_of_this_setting,
                                        "failure_info": failure_info,
                                        "failure_test_cases_list": failure_test_cases_list,
                                        "passed_test_cases_list": passed_test_cases_list,
                                        "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                                    }
                            new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                            evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos] = [evaluation_result_info_item]

                        # post-process
                        # evaluation_result["summary_validation"]["subject_size (with LLMI tests)"] += 1
                        evaluation_result["meta_list_evaluation"]["subject_size (with LLMI tests)"].append(FQS_testMethos)
                        if new_percentage==1.0:
                            # evaluation_result["summary_validation"]["subject_size (LLMI: pass all tests)"] += 1
                            evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass all tests)"].append(FQS_testMethos)
                                
                        flag_best_one = 0
                else: # 正常的流程 
                    # means the best one in validation; OR  may be no Sinput in the validaition (只能都选进来，后面再选最好哒) 
                    if (flag_best_one>0) or \
                        (FQS_testMethos not in evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"]): 

                        num_of_test_cases = LLMI_testing_generatedIT_result_evaluation["num_of_test_cases"]
                        num_of_passed_test_cases = LLMI_testing_generatedIT_result_evaluation["num_of_passed_test_cases"]
                        failure_info = list( LLMI_testing_generatedIT_result_evaluation["failure_info"].keys() )
                        failure_test_cases_list = []
                        for test_class_FQN in LLMI_testing_generatedIT_result_evaluation["failure_info"].keys():
                            failure_test_cases_list.extend( list(LLMI_testing_generatedIT_result_evaluation["failure_info"][test_class_FQN].keys()) )
                        passed_test_cases_list = []
                        for ele_list in LLMI_testing_generatedIT_result_evaluation["passed_test_cases_list"]:
                            for ele_ in ele_list: passed_test_cases_list.append(ele_)
                        passed_test_cases_list = list(set( passed_test_cases_list ))
                        LLMI_size = num_of_test_cases

                        # if num_of_test_cases>0:
                        # new_percentage: original percentage may be not correct 
                        new_percentage = num_of_passed_test_cases/num_of_test_cases if num_of_test_cases>0 else 0
                        LLMI_pass_percentage = new_percentage
                        evaluation_result_info_item = {
                                    "percentage" : new_percentage,
                                    "num_of_test_cases": num_of_test_cases,
                                    "num_of_passed_test_cases": num_of_passed_test_cases,
                                    "index_of_request": index_of_request,
                                    "dir_generated_Trans": generated_Trans_of_this_setting,
                                    "failure_info": failure_info,
                                    "failure_test_cases_list": failure_test_cases_list,
                                    "passed_test_cases_list": passed_test_cases_list,
                                    "withInputTransformation": MTC_result['MTC_item']['withInputTransformation']
                                }
                        
                        if FQS_testMethos in evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"]: # 在这里，选一个最好的吧 
                            existing_percentage = evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos][0]["percentage"]
                            if new_percentage > existing_percentage: 
                                evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos] = [evaluation_result_info_item]
                            if new_percentage == existing_percentage:
                                evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos].append(evaluation_result_info_item)
                        else:
                            evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos] = [evaluation_result_info_item]

                        # evaluation_result["summary_validation"]["subject_size (with LLMI tests)"] += 1
                        evaluation_result["meta_list_evaluation"]["subject_size (with LLMI tests)"].append(FQS_testMethos)
                        if new_percentage==1.0:
                            # evaluation_result["summary_validation"]["subject_size (LLMI: pass all tests)"] += 1
                            evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass all tests)"].append(FQS_testMethos)
                                
                        flag_best_one = 0
            # differential testing, TODO
            # if generatedIT_compile_result and Setting["test_generated_ITrans"]=="D" and OriginalMTC_testing_generatedIT_result and Diff_testing_generatedIT_result:
            #     flag_collect_test_result=True
            #     num_of_test_cases = Diff_testing_generatedIT_result["num_of_test_cases"]
            #     num_of_passed_test_cases = Diff_testing_generatedIT_result["num_of_passed_test_cases"]

 

    """ collect: effectiveness of generating follow-up inputs (validation results) """ #all_subject[FQS_testMethos]
    LLMI_input_generation_result = generate_Inputs_with_LLMs.result_collect(generate_Inputs_with_LLMs.Setting)# change 
    # LLMI_input_generation_result_for_evaluation = generate_Inputs_with_LLMs.result_collect( generate_Inputs_with_LLMs.for_evaluation_setting)

    # for FQS_testMethos in all_subject.keys(): # option1: all subjects
    # for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"].keys(): # option2: MTCs with  compilable generated ITrans (generatedIT_compile_result)
    # for FQS_testMethos in all_subject.keys(): # option1: all subjects
    for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"].keys() : 
        if evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"]<1: continue # option3: MTCs with Trans which passes o. MTC
        # tem
        # if FQS_testMethos not in LLMI_input_generation_result["meta_list"]["subject_compilableORvalid_Sinput_size"].keys(): continue # 240608 tem
        """  """
        # take that in the valiadation result:
        if FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"].keys():
            result_info_item = evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos][0] #暂时取第一个
            CUT_name = FQS_testMethos.split("(")[0].split(".")[-2]
            passed_test_cases_list = result_info_item["passed_test_cases_list"]         # Trans passed
            # failure_test_cases_list = result_info_item["failure_test_cases_list"]       # Trans failed
        else:
            passed_test_cases_list = []
            # failure_test_cases_list = []
        # LLMI_input_generation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos] # LLM generated FUinput
        CUT_name = FQS_testMethos.split("(")[0].split(".")[-2]
        valid_Sinput_item_list = LLMI_input_generation_result["meta_list"]["subject_compilableORvalid_Sinput_size"][FQS_testMethos]["valid_Sinput"]
        valid_Sinput_item_list = [ ele.replace(f"{CUT_name}_","") for ele in valid_Sinput_item_list ]
        valid_Sinput_w_LLM_FUinput_item_list = LLMI_input_generation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos]["valid_inputs"]
        valid_Sinput_w_LLM_FUinput_item_list = [ ele.replace(f"{CUT_name}_","") for ele in valid_Sinput_w_LLM_FUinput_item_list ]
        valid_Sinput_w_Trans_FUinput_item_list = passed_test_cases_list
        
        # checking
        # if len(valid_Sinput_w_LLM_FUinput_item_list) < len(valid_Sinput_item_list):
        #     print("correct")
        # valid_Sinput_item_list cover valid_Sinput_w_LLM_FUinput_item_list and valid_Sinput_w_Trans_FUinput_item_list
        if len( set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_item_list)) > 0:
            valid_Sinput_w_LLM_FUinput_item_list = [ ele for ele in valid_Sinput_w_LLM_FUinput_item_list if ele in valid_Sinput_item_list]  
            print("incorrect", FQS_testMethos, "LLM_FUinput more")
        if len( set(valid_Sinput_w_Trans_FUinput_item_list) - set(valid_Sinput_item_list)) > 0:
            valid_Sinput_w_Trans_FUinput_item_list = [ ele for ele in valid_Sinput_w_Trans_FUinput_item_list if ele in valid_Sinput_item_list]  
            print("incorrect", FQS_testMethos,  "Trans_FUinput more")

        valid_Sinput_w_LLM_FUinput_only = list( set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_w_Trans_FUinput_only = list( set(valid_Sinput_w_Trans_FUinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list))
        valid_Sinput_w_LLMandTrans_FUinput = list( set(valid_Sinput_w_LLM_FUinput_item_list) & set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_wo_LLMorTrans_FUinput = list( set(valid_Sinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_wo_LLM_FUinput = list( set(valid_Sinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list) )
        valid_Sinput_wo_LLM_but_with_Trans_FUinput = list( set(set(valid_Sinput_item_list)-set(valid_Sinput_w_LLM_FUinput_item_list)) & set(valid_Sinput_w_Trans_FUinput_item_list))

        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_w_LLM_FUinput_only"][FQS_testMethos] = valid_Sinput_w_LLM_FUinput_only
        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_w_Trans_FUinput_only"][FQS_testMethos] = valid_Sinput_w_Trans_FUinput_only
        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_w_LLMandTrans_FUinput"][FQS_testMethos] = valid_Sinput_w_LLMandTrans_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_wo_LLMorTrans_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLMorTrans_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_wo_LLM_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLM_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_validation"]["valid_Sinput_wo_LLM_but_with_Trans_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLM_but_with_Trans_FUinput

        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput"] += len(valid_Sinput_item_list)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_LLM_FUinput_only"] += len(valid_Sinput_w_LLM_FUinput_only)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_Trans_FUinput_only"] += len(valid_Sinput_w_Trans_FUinput_only)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_LLMandTrans_FUinput"] += len(valid_Sinput_w_LLMandTrans_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_wo_LLMorTrans_FUinput"] += len(valid_Sinput_wo_LLMorTrans_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_wo_LLM_FUinput"] += len(valid_Sinput_wo_LLM_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_wo_LLM_but_with_Trans_FUinput"] += len(valid_Sinput_wo_LLM_but_with_Trans_FUinput)

    all_valid_Sinput = evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput"]
    all_valid_Sinput_w_Trans_FUinput_only = evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_Trans_FUinput_only"] 
    all_valid_Sinput_w_LLMandTrans_FUinput = evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_LLMandTrans_FUinput"]
    all_valid_Sinput_w_LLM_FUinput_only = evaluation_result["effectiveness_evaluation"]["summary_validation"]["valid_Sinput_w_LLM_FUinput_only"]
    
    all_valid_Sinput_w_Trans_FUinput = (all_valid_Sinput_w_Trans_FUinput_only + all_valid_Sinput_w_LLMandTrans_FUinput)
    all_valid_Sinput_w_LLM_FUinput = all_valid_Sinput_w_LLM_FUinput_only + all_valid_Sinput_w_LLMandTrans_FUinput
    evaluation_result["effectiveness_evaluation"]["summary_validation"]["Trans_success_rate"] = f"{all_valid_Sinput_w_Trans_FUinput/ all_valid_Sinput} ({all_valid_Sinput_w_Trans_FUinput}/{all_valid_Sinput})" 
    evaluation_result["effectiveness_evaluation"]["summary_validation"]["LLM_success_rate"] =  f"{all_valid_Sinput_w_LLM_FUinput / all_valid_Sinput} ({all_valid_Sinput_w_LLM_FUinput}/{all_valid_Sinput})" 

    
    """ collect: effectiveness of generating follow-up inputs (evaluation results) """ #all_subject[FQS_testMethos]
    # LLMI_input_generation_result = generate_Inputs_with_LLMs.result_collect(generate_Inputs_with_LLMs.Setting)# change 
    LLMI_input_generation_result_for_evaluation = generate_Inputs_with_LLMs.result_collect( generate_Inputs_with_LLMs.for_evaluation_setting)
    # for FQS_testMethos in all_subject.keys(): # option1: all subjects
    # for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"].keys(): # option2: MTCs with  compilable generated ITrans (generatedIT_compile_result)
    for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"].keys() : 
        # if evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"]<1: continue # option3: MTCs with Trans which passes o. MTC
        
        """  """
        # take taht in the evalution result 
        if FQS_testMethos in evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"].keys():
            result_info_item = evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos][0] #暂时取第一个
            CUT_name = FQS_testMethos.split("(")[0].split(".")[-2]
            passed_test_cases_list = result_info_item["passed_test_cases_list"]         # Trans passed
            # failure_test_cases_list = result_info_item["failure_test_cases_list"]       # Trans failed
        else:
            passed_test_cases_list = []
            # failure_test_cases_list = []
        # LLMI_input_generation_result_for_evaluation["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos] # LLM generated FUinput
        valid_Sinput_item_list = LLMI_input_generation_result_for_evaluation["meta_list"]["subject_compilableORvalid_Sinput_size"][FQS_testMethos]["valid_Sinput"]
        valid_Sinput_item_list = [ ele.replace(f"{CUT_name}_","") for ele in valid_Sinput_item_list ]
        valid_Sinput_w_LLM_FUinput_item_list = LLMI_input_generation_result_for_evaluation["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos]["valid_inputs"]
        valid_Sinput_w_LLM_FUinput_item_list = [ ele.replace(f"{CUT_name}_","") for ele in valid_Sinput_w_LLM_FUinput_item_list ]
        valid_Sinput_w_Trans_FUinput_item_list = passed_test_cases_list

        # checking
        # if len(valid_Sinput_w_LLM_FUinput_item_list) < len(valid_Sinput_item_list):
        #     print("correct")
        # valid_Sinput_item_list cover valid_Sinput_w_LLM_FUinput_item_list and valid_Sinput_w_Trans_FUinput_item_list
        if len( set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_item_list)) > 0:
            valid_Sinput_w_LLM_FUinput_item_list = [ ele for ele in valid_Sinput_w_LLM_FUinput_item_list if ele in valid_Sinput_item_list]  
            print("incorrect", FQS_testMethos, "LLM_FUinput more")
        if len( set(valid_Sinput_w_Trans_FUinput_item_list) - set(valid_Sinput_item_list)) > 0:
            valid_Sinput_w_Trans_FUinput_item_list = [ ele for ele in valid_Sinput_w_Trans_FUinput_item_list if ele in valid_Sinput_item_list]  
            print("incorrect", FQS_testMethos,  "Trans_FUinput more")

        valid_Sinput_w_LLM_FUinput_only = list( set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_w_Trans_FUinput_only = list( set(valid_Sinput_w_Trans_FUinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list))
        valid_Sinput_w_LLMandTrans_FUinput = list( set(valid_Sinput_w_LLM_FUinput_item_list) & set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_wo_LLMorTrans_FUinput = list( set(valid_Sinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list) - set(valid_Sinput_w_Trans_FUinput_item_list))
        valid_Sinput_wo_LLM_FUinput = list( set(valid_Sinput_item_list) - set(valid_Sinput_w_LLM_FUinput_item_list) )
        valid_Sinput_wo_LLM_but_with_Trans_FUinput = list( set(set(valid_Sinput_item_list)-set(valid_Sinput_w_LLM_FUinput_item_list)) & set(valid_Sinput_w_Trans_FUinput_item_list))

        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_w_LLM_FUinput_only"][FQS_testMethos] = valid_Sinput_w_LLM_FUinput_only
        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_w_Trans_FUinput_only"][FQS_testMethos] = valid_Sinput_w_Trans_FUinput_only
        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_w_LLMandTrans_FUinput"][FQS_testMethos] = valid_Sinput_w_LLMandTrans_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_wo_LLMorTrans_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLMorTrans_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_wo_LLM_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLM_FUinput
        evaluation_result["effectiveness_evaluation"]["meta_list_evaluation"]["valid_Sinput_wo_LLM_but_with_Trans_FUinput"][FQS_testMethos] = valid_Sinput_wo_LLM_but_with_Trans_FUinput

        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput"] += len(valid_Sinput_item_list)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_LLM_FUinput_only"] += len(valid_Sinput_w_LLM_FUinput_only)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_Trans_FUinput_only"] += len(valid_Sinput_w_Trans_FUinput_only)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_LLMandTrans_FUinput"] += len(valid_Sinput_w_LLMandTrans_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_wo_LLMorTrans_FUinput"] += len(valid_Sinput_wo_LLMorTrans_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_wo_LLM_FUinput"] += len(valid_Sinput_wo_LLM_FUinput)
        evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_wo_LLM_but_with_Trans_FUinput"] += len(valid_Sinput_wo_LLM_but_with_Trans_FUinput)

    all_valid_Sinput = evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput"]
    all_valid_Sinput_w_Trans_FUinput_only = evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_Trans_FUinput_only"] 
    all_valid_Sinput_w_LLMandTrans_FUinput = evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_LLMandTrans_FUinput"]
    all_valid_Sinput_w_LLM_FUinput_only = evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["valid_Sinput_w_LLM_FUinput_only"]
    
    all_valid_Sinput_w_Trans_FUinput = (all_valid_Sinput_w_Trans_FUinput_only + all_valid_Sinput_w_LLMandTrans_FUinput)
    all_valid_Sinput_w_LLM_FUinput = all_valid_Sinput_w_LLM_FUinput_only + all_valid_Sinput_w_LLMandTrans_FUinput
    evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["Trans_success_rate"] = f"{all_valid_Sinput_w_Trans_FUinput/ all_valid_Sinput} ({all_valid_Sinput_w_Trans_FUinput}/{all_valid_Sinput})" 
    evaluation_result["effectiveness_evaluation"]["summary_evaluation"]["LLM_success_rate"] =  f"{all_valid_Sinput_w_LLM_FUinput / all_valid_Sinput} ({all_valid_Sinput_w_LLM_FUinput}/{all_valid_Sinput})" 


    """ summary: validation """
    for MTC_result in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"]:
        OriginalMTC_pass_percentage = None
        LLMI_pass_percentage = None
        FQS_testMethos = MTC_result
        
        OriginalMTC_pass_percentage = evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"]
        if FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"]:
            LLMI_pass_percentage = evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos][0]["percentage"] # 里面都是一样的percentage，暂时取第一个
        if LLMI_pass_percentage != None and OriginalMTC_pass_percentage != None:
            info_item = {"MTC": FQS_testMethos, "index_of_request": index_of_request,
                            "LLMI_size": LLMI_size, "LLMI_pass_percentage": LLMI_pass_percentage, "OriginalMTC_pass_percentage": OriginalMTC_pass_percentage}
            if LLMI_pass_percentage==1.0 and OriginalMTC_pass_percentage==1.0:
                evaluation_result["meta_list"]["pass_both_O_and_all_LLMI"].append(info_item)
            if LLMI_pass_percentage==0.0 and OriginalMTC_pass_percentage<1.0: # in theory, OriginalMTC_pass_percentage==0/1
                evaluation_result["meta_list"]["fail_both_O_and_all_LLMI"].append(info_item)
            if LLMI_pass_percentage<1.0 and OriginalMTC_pass_percentage==1.0:
                evaluation_result["meta_list"]["pass_O_but_fail_some_LLMI"].append(info_item)
            if LLMI_pass_percentage>0.0 and OriginalMTC_pass_percentage<1.0:
                evaluation_result["meta_list"]["pass_some_LLMI_but_fail_O"].append(info_item)
            if LLMI_pass_percentage>0.0:
                evaluation_result["meta_list"]["subject_size (LLMI: pass at least one test)"].append(FQS_testMethos)
            evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"].append(LLMI_pass_percentage)

    # summary_validation, the best result of all requests
    evaluation_result["summary_validation"]["all_subject"] = len(all_subject)
    evaluation_result["summary_validation"]["compilation_success"] = len(evaluation_result["meta_list"]["compilation_success"])
    evaluation_result["summary_validation"]["subject_size (LLMI: pass all tests)"]  = len( set( evaluation_result["meta_list"]["subject_size (LLMI: pass all tests)"] ) )
    evaluation_result["summary_validation"]["subject_size (with LLMI tests)"]  = len( set( evaluation_result["meta_list"]["subject_size (with LLMI tests)"] ) )
    evaluation_result["summary_validation"]["subject_size (pass original MTC)"]  = len( set( evaluation_result["meta_list"]["subject_size (pass original MTC)"] ) )
    evaluation_result["summary_validation"]["subject_size (pass original MTC, but fail LLMI)"]  = len( evaluation_result["meta_list"]["pass_O_but_fail_some_LLMI"] )
    evaluation_result["summary_validation"]["subject_size (LLMI: pass at least one test)"]  = len( set( evaluation_result["meta_list"]["subject_size (LLMI: pass at least one test)"] ) )
    evaluation_result["summary_validation"]["validation_pass_rate (average: LLMI)"] = sum(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])/len(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])

    # pass at least one experimental Sinput: list(passOMTC).extend(passAtLeastOneLLMI)
    set_pass_at_least_one = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).union( set(evaluation_result["meta_list"]["subject_size (LLMI: pass at least one test)"]) )
    evaluation_result["summary_validation"]["subject_size (pass at least one Sinput: OMTCorLLMI)"]  = len( set_pass_at_least_one )
    evaluation_result["meta_list"]["subject_size (pass at least one Sinput: OMTCorLLMI)"] = list( set_pass_at_least_one )
    # subject: pass all experimental Sinputs: if w/ LLMI, list(passOMTC and passAllLLMI); if w/0 LLMI, list(passOMTC)
    set_subjects_w_LLMI_and_pass_all = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).intersection( set(evaluation_result["meta_list"]["subject_size (LLMI: pass all tests)"]) )
    set_subjects_wo_LLMI_and_pass_all = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).difference( set(evaluation_result["meta_list"]["subject_size (with LLMI tests)"]) )
    
    evaluation_result["summary_validation"]["subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)"] = len(set_subjects_w_LLMI_and_pass_all.union(set_subjects_wo_LLMI_and_pass_all) ) 
    evaluation_result["meta_list"]["subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)"] = list( set_subjects_w_LLMI_and_pass_all.union(set_subjects_wo_LLMI_and_pass_all) )

    evaluation_result["summary_validation"]["validation_pass_rate (average: LLMI+OMTC)"] = (sum(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])+len(set_subjects_wo_LLMI_and_pass_all)) / (len(evaluation_result["meta_list"]["validation_pass_rate (LLMI) list"])+len(set_subjects_wo_LLMI_and_pass_all))


    # evaluation_result["summary_validation"]["validation_pass_rate (average: o. MTC)"] = sum([evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"] for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"]])/len(evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"])
    # evaluation_result["summary_validation"]["validation_pass_rate (average: LLMI)"] = sum([evaluation_result["meta_list"]["validation_pass_rate (LLMI)"][FQS_testMethos]["percentage"] for FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (LLMI)"]])/len(evaluation_result["meta_list"]["validation_pass_rate (LLMI)"])
    for ele in all_subject.keys(): # validation
        if ele not in evaluation_result["meta_list"]["compilation_success"]:
            evaluation_result["meta_list"]["compilation_unsuccess"][ele] = all_subject[ele]
    
    """ summary: evaluation """
    # for FQS_testMethos in all_subject.keys():
    for MTC_result in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"]:
        OriginalMTC_pass_percentage = None
        LLMI_pass_percentage = None
        FQS_testMethos = MTC_result
        
        if FQS_testMethos in evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"]: # 只有 validation时，跑了一下：
            OriginalMTC_pass_percentage = evaluation_result["meta_list"]["validation_pass_rate (o. MTC)"][FQS_testMethos]["percentage"]
        if FQS_testMethos in evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"]:
            LLMI_pass_percentage = evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI)"][FQS_testMethos][0]["percentage"] # 里面都是一样的percentage，暂时取第一个

        if LLMI_pass_percentage != None and OriginalMTC_pass_percentage != None: # 应该没问题：OriginalMTC_pass_percentage可以 <1
            info_item = {"MTC": FQS_testMethos, "index_of_request": index_of_request,
                            "LLMI_size": LLMI_size, "LLMI_pass_percentage": LLMI_pass_percentage, "OriginalMTC_pass_percentage": OriginalMTC_pass_percentage}
            if LLMI_pass_percentage==1.0 and OriginalMTC_pass_percentage==1.0:
                evaluation_result["meta_list_evaluation"]["pass_both_O_and_all_LLMI"].append(info_item)
            if LLMI_pass_percentage==0.0 and OriginalMTC_pass_percentage<1.0: # in theory, OriginalMTC_pass_percentage==0/1
                evaluation_result["meta_list_evaluation"]["fail_both_O_and_all_LLMI"].append(info_item)
            if LLMI_pass_percentage<1.0 and OriginalMTC_pass_percentage==1.0:
                evaluation_result["meta_list_evaluation"]["pass_O_but_fail_some_LLMI"].append(info_item)
            if LLMI_pass_percentage>0.0 and OriginalMTC_pass_percentage<1.0:
                evaluation_result["meta_list_evaluation"]["pass_some_LLMI_but_fail_O"].append(info_item)
            if LLMI_pass_percentage>0.0:
                evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass at least one test)"].append(FQS_testMethos)
            evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI) list"].append(LLMI_pass_percentage)

    # summary, the best result of all requests
    evaluation_result["summary_evaluation"]["all_subject"] = len(all_subject)
    evaluation_result["summary_evaluation"]["compilation_success"] = len(evaluation_result["meta_list"]["compilation_success"])
    evaluation_result["summary_evaluation"]["subject_size (LLMI: pass all tests)"]  = len( set( evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass all tests)"] ) )
    evaluation_result["summary_evaluation"]["subject_size (with LLMI tests)"]  = len( set( evaluation_result["meta_list_evaluation"]["subject_size (with LLMI tests)"] ) )
    evaluation_result["summary_evaluation"]["subject_size (pass original MTC)"]  = len( set( evaluation_result["meta_list"]["subject_size (pass original MTC)"] ) )
    evaluation_result["summary_evaluation"]["subject_size (pass original MTC, but fail LLMI)"]  = len( evaluation_result["meta_list_evaluation"]["pass_O_but_fail_some_LLMI"] )
    evaluation_result["summary_evaluation"]["subject_size (LLMI: pass at least one test)"]  = len( set( evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass at least one test)"] ) )
    evaluation_result["summary_evaluation"]["pass_rate (average: LLMI)"] = sum(evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI) list"])/len(evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI) list"])

    # pass at least one experimental Sinput: list(passOMTC).extend(passAtLeastOneLLMI)
    set_pass_at_least_one = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).union( set(evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass at least one test)"]) )
    evaluation_result["summary_evaluation"]["subject_size (pass at least one Sinput: OMTCorLLMI)"]  = len( set_pass_at_least_one )
    evaluation_result["meta_list_evaluation"]["subject_size (pass at least one Sinput: OMTCorLLMI)"] = list( set_pass_at_least_one )
    # subject: pass all experimental Sinputs: if w/ LLMI, list(passOMTC and passAllLLMI); if w/0 LLMI, list(passOMTC)
    set_subjects_w_LLMI_and_pass_all = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).intersection( set(evaluation_result["meta_list_evaluation"]["subject_size (LLMI: pass all tests)"]) )
    set_subjects_wo_LLMI_and_pass_all = set(evaluation_result["meta_list"]["subject_size (pass original MTC)"]).difference( set(evaluation_result["meta_list_evaluation"]["subject_size (with LLMI tests)"]) )
    evaluation_result["summary_evaluation"]["subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)"] = len(set_subjects_w_LLMI_and_pass_all.union(set_subjects_wo_LLMI_and_pass_all) ) 
    evaluation_result["meta_list_evaluation"]["subject_size (pass all Sinputs: OMTCandLLMI, LLMI can be none)"] = list( set_subjects_w_LLMI_and_pass_all.union(set_subjects_wo_LLMI_and_pass_all) )

    evaluation_result["summary_evaluation"]["pass_rate (average: LLMI+OMTC)"] = (sum(evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI) list"])+len(set_subjects_wo_LLMI_and_pass_all)) / (len(evaluation_result["meta_list_evaluation"]["evaluation_pass_rate (LLMI) list"])+len(set_subjects_wo_LLMI_and_pass_all))

    if not just_collect_results:
        json_processing.write( json_content=evaluation_result, path=all_evaluation_result_of_generated_ITrans_function_path.replace(".json","_best_k.json"))
    return evaluation_result


def main_task(task):
    index_of_request = task["index_of_request"]
    MTC_item = task["MTC_item"]
    print(f"Processing, index_of_request: {index_of_request}, MTC_item: {MTC_item['FQS_testMethos']}")

    print('+++ START: generate_prompt_from_profile ', MTC_item["FQS_testMethos"])
    trans_generator = transGenerator(index_of_request, MTC_item)
    generate_prompt_from_profile(trans_generator)
    print('+++ START: generate_Trans_by_prompting ', MTC_item["FQS_testMethos"])
    generate_ITrans_by_prompting(trans_generator)
    print('+++ START: validate_generated_Trans ', MTC_item["FQS_testMethos"])
    test_generated_ITrans(trans_generator, skipCompileIfExist=Setting["skipCompileIfExist"])

def parallel():
    parallel_size = Setting["parallel_size"]
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    tasks = []
    for index_of_request in range(Setting["number_of_request"]):
        for MTC_item in all_GT_MTCs:
            if "skip" in MTC_item and MTC_item["skip"] == True: continue
            # if "com.alibaba.fastjson2.internal.processor.maps.Map" not in MTC_item["FQS_testMethos"]: continue # for debug
            tasks.append({"index_of_request": index_of_request, "MTC_item": MTC_item})

    with multiprocessing.Pool(processes=parallel_size) as pool:
        # Use pool.imap or pool.map for ordered results
        pool.map(main_task, tasks)

def one_by_one(FQS_testMethos=None):
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    count = 0
    for index_of_request in range(Setting["number_of_request"]):
        for MTC_item in all_GT_MTCs:
            if FQS_testMethos and FQS_testMethos not in MTC_item["FQS_testMethos"]: continue
            print(f"Processing, index_of_request: {index_of_request}, MTC_item: {MTC_item['FQS_testMethos']}")
            
            print('+++ START: generate_prompt_from_profile ', MTC_item["FQS_testMethos"])
            trans_generator = transGenerator(index_of_request, MTC_item)
            generate_prompt_from_profile(trans_generator)
            print('+++ START: generate_Trans_by_prompting ', MTC_item["FQS_testMethos"])
            generate_ITrans_by_prompting(trans_generator)
            print('+++ START: validate_generated_Trans ', MTC_item["FQS_testMethos"])
            test_generated_ITrans(trans_generator, skipCompileIfExist=Setting["skipCompileIfExist"])

if __name__ == "__main__":
    # FQS_testMethos = "org.datagear.util.version.VersionTest.stringOfTest()"
    # one_by_one(FQS_testMethos)

    one_by_one()
