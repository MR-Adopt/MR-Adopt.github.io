"""
"""
import multiprocessing
import os, sys
import time
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing, java_parser, compile_java_poj, java_test, request_LLMs
import construct_prompt
import extract_code

import test_IT
import config
import re, datetime
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

Profile_GT_MTCs_wo_IT = json_processing.read(Profile_GT_MTCs_wo_IT_path)
Profile_GT_MTCs_w_IT = json_processing.read(Profile_GT_MTCs_w_IT_path)

GT_CLASS_SUFFIX = config.GT_CLASS_SUFFIX
HARDCODED_CLASS_SUFFIX = config.HARDCODED_CLASS_SUFFIX
VALID_INPUT_CLASS_SUFFIX = config.VALID_INPUT_CLASS_SUFFIX

ITRANS_MTCIT_DIR = config.ITRANS_MTCIT_DIR
ITRANS_GT_DIR = config.ITRANS_GT_DIR
ITRANS_RAW_DIR = config.ITRANS_RAW_DIR
ITRANS_GENERATED_IT_DIR = config.ITRANS_GENERATED_IT_DIR
ITRANS_GENERATED_INPUTS_DIR = config.ITRANS_GENERATED_INPUTS_DIR
PATH_ITRANS_COMPILE_INFO = config.PATH_ITRANS_COMPILE_INFO

ITRANS_CACHE_DIR = config.ITRANS_CACHE_DIR
ITRANS_CACHE_GENERATED_TRANS_DIR = config.ITRANS_CACHE_GENERATED_TRANS_DIR
ITRANS_CACHE_GENERATED_INPUTS_DIR = config.ITRANS_CACHE_GENERATED_INPUTS_DIR

all_valid_Sinput = json_processing.read(f"all_valid_Sinput.json")

from utility.request_LLMs import model_symbols, symbols_model
from construct_prompt import Templates
# symbols_model: w, g3, g4, s2, qw, ml, dp
# 稳定版
Setting = {
    # !!! MODIFY
    "model": f"{symbols_model['g3']}",
    "number_of_request": 1,
    
    "strategy": 2, # 1: generate input pairs, 2: generate source and then corresponding follow-up input
    "Prompt_template":"i5-1", # stragety2: 5-1 起步 
    "number_of_shot":0,

    # !!! MODIFY
    "number_of_candidate": "five", # number of candidate inputs in each request 
    "temperature":0.2,
    "overwritePreviousPromptResults":False,
    "overwritePreviousValidationResults":True, # validate tests
    "skipCompileIfExist": False,
    # "skipPromptGenerationIfExist": True, # 不太行，因为需要加载一些 input_generator 的信息
    "parallel_size": 4,
    "index_of_request": 0,
    "validate_generated_Inputs": "O", # O: original test inputs, D: diff testing (for cases where original_MTC success)  
    # running
    
    # !!! MODIFY
    "result_collect": True,
    "parallel": True,
    "one_by_one": False,
    "eval": "",         # No: "" , effectEval: "_effectivenssEvaluation",
    "ablation": "",     # No: "" , noRefinement: "_ablateRefinement",

}

for_evaluation_setting = Setting.copy()
for_evaluation_setting.update({
    "model": f"{symbols_model['qw']}",
    "strategy": 2, # 1: generate input pairs, 2: generate source and then corresponding follow-up input
    "Prompt_template":"i5-1", # stragety2: 5-1 起步 

    "number_of_shot":0,
    "number_of_request": 10,
    "number_of_candidate": "five", # number of candidate inputs in each request 
    "temperature":0.2,
    "eval": ""
})

all_evaluation_result_of_generated_inputs_function_path = f"{OUTPUT_DIR}inputs/validation_generated_Inputs_T{Setting['Prompt_template']}_Shot{Setting['number_of_shot']}_R{Setting['number_of_request']}_Temprature{Setting['temperature']}_{Setting['model']}_Stra{Setting['strategy']}{Setting['eval']}{Setting['ablation']}.json"


class inputGenerator():
    generated_inputs_dir_name = "generated_inputs"
    generated_valid_inputs_testing_Trans_dir_name = "generated_valid_inputs_testing_Trans"

    @staticmethod
    def get_cache_dir(index_of_request, Setting):
        Setting['index_of_request'] = index_of_request
        # cache_dir_name_for_this_setting = f"{Setting['model']}_T{Setting['Prompt_template']}_Shot{Setting['number_of_shot']}_Temprature{Setting['temperature']}_{Setting['index_of_request']}" # to use
        cache_dir_name_for_this_setting = f"{Setting['model']}_T{Setting['Prompt_template']}_Temprature{Setting['temperature']}_{Setting['index_of_request']}{Setting['eval']}"
        return cache_dir_name_for_this_setting

    def __init__(self, index_of_request,MTC_item):
        # global Setting
        Setting['index_of_request'] = index_of_request
        cache_dir_name_for_this_setting = inputGenerator.get_cache_dir(index_of_request, Setting)
        cache_dir_for_this_setting = f"{config.ITRANS_CACHE_GENERATED_INPUTS_DIR}{cache_dir_name_for_this_setting}/"

        # prompt
        Crafted_prompts_dir = f"{cache_dir_for_this_setting}prompts/"
        prompt_results_content_dir = f"{cache_dir_for_this_setting}prompts_results_content/"
        prompts_results_raw_dir = f"{cache_dir_for_this_setting}prompts_results_raw/"
        self.Crafted_promptsS_dir = f"{cache_dir_for_this_setting}promptsS/"
        self.promptS_results_content_dir = f"{cache_dir_for_this_setting}promptsS_results_content/"
        self.promptsS_results_raw_dir = f"{cache_dir_for_this_setting}promptsS_results_raw/"
        self.Crafted_promptsF_dir = f"{cache_dir_for_this_setting}promptsF/"
        self.promptF_results_content_dir = f"{cache_dir_for_this_setting}promptsF_results_content/"
        self.promptsF_results_raw_dir = f"{cache_dir_for_this_setting}promptsF_results_raw/"
        # generated inputs based MTCs
        prompt_generated_inputs_dir = f"{cache_dir_for_this_setting}{inputGenerator.generated_inputs_dir_name}/"
        cache_generated_valid_inputs_testing_Trans_dir = f"{cache_dir_for_this_setting}{inputGenerator.generated_valid_inputs_testing_Trans_dir_name}/"
        
        validation_log_dir = f"{cache_dir_for_this_setting}exe_result/"
        validation_result_of_generated_inputs_path = f"{cache_dir_for_this_setting}evaluation_generated_inputs.json"
        compilation_log_dir = f"{cache_dir_for_this_setting}compilation_log/"
        generated_inputs_path = f"{cache_dir_for_this_setting}generated_inputs.json"

        file_processing.creatFolder_recursively_IfExistPass(cache_dir_for_this_setting)
        file_processing.creatFolder_recursively_IfExistPass(prompt_generated_inputs_dir)
        file_processing.creatFolder_recursively_IfExistPass(cache_generated_valid_inputs_testing_Trans_dir)
        file_processing.creatFolder_recursively_IfExistPass(compilation_log_dir)
        file_processing.creatFolder_recursively_IfExistPass(validation_log_dir)
        if Setting["strategy"]==1:
            file_processing.creatFolder_recursively_IfExistPass(Crafted_prompts_dir)
            file_processing.creatFolder_recursively_IfExistPass(prompt_results_content_dir)
            file_processing.creatFolder_recursively_IfExistPass(prompts_results_raw_dir)
        elif Setting["strategy"]==2:
            file_processing.creatFolder_recursively_IfExistPass(self.Crafted_promptsS_dir);file_processing.creatFolder_recursively_IfExistPass(self.promptS_results_content_dir);file_processing.creatFolder_recursively_IfExistPass(self.promptsS_results_raw_dir)
            file_processing.creatFolder_recursively_IfExistPass(self.Crafted_promptsF_dir);file_processing.creatFolder_recursively_IfExistPass(self.promptF_results_content_dir);file_processing.creatFolder_recursively_IfExistPass(self.promptsF_results_raw_dir)

            # TODO generated inputs dirs / lalala


        self.Setting = Setting
        self.strategy = Setting["strategy"]
        self.base_prompt_template_symbols = Setting["Prompt_template"] # not the one used
        self.prompt_template_symbols = None                             # the one used actually
        # self.prompt_template = Templates[Setting["Prompt_template"]]
        self.prompt_template = None
        self.number_of_candidate = Setting["number_of_candidate"]
        self.index_of_request = index_of_request
        self.cache_dir_name_for_this_setting = cache_dir_name_for_this_setting
        self.cache_dir_for_this_setting = cache_dir_for_this_setting
        self.Crafted_prompts_dir = Crafted_prompts_dir
        self.prompt_generated_inputs_dir = prompt_generated_inputs_dir
        self.cache_generated_valid_inputs_testing_Trans_dir = cache_generated_valid_inputs_testing_Trans_dir
        self.prompt_results_content_dir = prompt_results_content_dir
        self.prompts_results_raw_dir = prompts_results_raw_dir
        self.input_type_to_generate = None
        
        self.generated_inputs_path = generated_inputs_path
        self.validation_log_dir = validation_log_dir
        self.validation_result_of_generated_inputs_path = validation_result_of_generated_inputs_path
        self.compilation_log_dir = compilation_log_dir
        self.MTC_item = MTC_item

        self.MTChClass = ""
        self.MTChMethod = ""
        self.prompt_path = ""
        self.promt_id = ""
        self.promt_content = ""
        self.prompt_system_message = "you are a helpful programming assistant"
        self.inputSTMTs = ""
        self.input_type_to_generate = "P" # "P": pair / "S": source / "F": follow-up]
        self.sourceInputs_TypeAndVariable = []
        self.followUpInputs_TypeAndVariable = []

        self.generated_input_code_blocks = []

        self.invoked_package_FQN = ""
        self.generated_inputs_package_FQN = ""
        self.generated_inputs_class_FQN = ""
        self.generated_inputs_folder_name = ""
        self.generated_valid_inputs_class_FQN = ""
        self.generated_valid_inputs_folder_name = ""
        self.generated_inputs_validation_result = None
        self.Test_result = None
        self.path_of_generated_inputs_in_original_poj = ""
        self.path_of_generated_MTChClass_list = []

        

        # LLM generated
        self.generated_input_blocks = []
        self.generated_input_blocks_unique = []
        self.generated_Sinput_blocks = []
        self.generated_Sinput_blocks_unique = []
        self.postprocessed_generated_input_blocks = []
        self.postprocessed_generated_input_blocks_unique = []

        self.generated_input_relatedSTMTs = []
        self.testCase_with_generated_new_input = ""
        self.path_of_generated_MTChClass = ""

        self.generated_inputs_items = {}
        # generated_inputs_item[generated_class_name_FQN] = {
        #             "generated_input_blockid": generated_input_blockid,
        #             "path_of_class_with_generated_test_input": path_of_class_with_generated_test_input,
        #             "generated_class_name": new_test_class_name,
        #             "generated_test_method_name": new_test_method_name
        #         })


def get_GT_Trans(MTC_item, type="function_header"):
    """
        type="function" / 
            "class_file_content": include import statements and package statements
            "class_definition": no import statements
            "function_header": 
    """
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    poj_name = MTC_item["poj_name"]
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
    
    test_file = file_processing.read_TXTfile(test_file_path)
    package_line = test_file.split("\n")[:0]
    for line in test_file.split("\n"):
        if line.startswith("package "): package_line = line; break
        if line.strip().startswith("package "): package_line = line; break
    invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦
    
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
    class_name = processed_crafted_GT_MTC_test_class_name

    # if Setting["Prompt_template"] in ["2","3-1","3-2"]:
    if "type" not in MTC_item: 
        if MTC_item["withInputTransformation"]: MTC_item["type"] = "w_ITrans"
        else: MTC_item["type"] = "wo_ITrans"
    if MTC_item["type"] == "wo_ITrans":
        GT_ITrans_path = f"{GT_ITrans_wo_dir}{invoked_package_FQN.replace('.','/')}/{processed_crafted_GT_MTC_test_class_name}{GT_CLASS_SUFFIX}.java"
    elif MTC_item["type"] == "w_ITrans":
        GT_ITrans_path = f"{GT_ITrans_w_dir}{invoked_package_FQN.replace('.','/')}/{processed_crafted_GT_MTC_test_class_name}{GT_CLASS_SUFFIX}.java"
    GT_ITrans_class = file_processing.read_TXTfile(GT_ITrans_path)
    
    # get class_file_content
    GT_ITrans_class_file_content = GT_ITrans_class
    
    
    # get class_definition, no import statements
    GT_ITrans_class_def = ""
    GT_ITrans_class_def_lines = []
    flag_is_class_def = False
    for line in GT_ITrans_class.split("\n"):
        if " class " in line: # class def start
            flag_is_class_def = True
        elif line.strip().startswith("class "): # class def end
            flag_is_class_def = True
        if flag_is_class_def:
            GT_ITrans_class_def_lines.append(line)
    GT_ITrans_class_def = ("\n").join(GT_ITrans_class_def_lines)
    GT_ITrans_class_def.replace(f"{processed_crafted_GT_MTC_test_class_name}{GT_CLASS_SUFFIX}", f"{processed_crafted_GT_MTC_test_class_name}")

    # get function_header
    pattern = r'public static [a-zA-Z0-9_,.?()\[\]<> ]* inputTransformation[a-zA-Z0-9_,.?()\[\]<> ]*{'
    matches = re.findall(pattern, GT_ITrans_class)
    function_header = "public static Object inputTransformation()"
    if len( matches ) ==0:
        print("ERROR: no inputTransformation function in GT ITrans class")
        print( f"GT_ITrans_path: {GT_ITrans_path}" )
    else:
        function_header = matches[0].strip("{")


    if type=="class_file_content":
        return GT_ITrans_class_file_content
    elif type=="class_definition":
        return GT_ITrans_class_def
    elif type=="function_header":
        return function_header
    

def generate_prompt_from_profile(input_generator, task_type="input_generation"):
    print('+++ START: generate_prompt_from_profile ', input_generator.MTC_item["FQS_testMethos"])
    # pre-processing: choose the right template, the corresponding dir for prompt results
    if input_generator.input_type_to_generate.startswith("P"):
        input_generator.prompt_template_symbols = input_generator.base_prompt_template_symbols
        input_generator.prompt_template = Templates[input_generator.prompt_template_symbols]
    elif input_generator.input_type_to_generate.startswith("S"): # Pair Source Followup
        input_generator.prompt_template_symbols = input_generator.base_prompt_template_symbols+"S"

        input_generator.Crafted_prompts_dir = input_generator.Crafted_promptsS_dir
        input_generator.prompt_results_content_dir = input_generator.promptS_results_content_dir
        input_generator.prompts_results_raw_dir = input_generator.promptsS_results_raw_dir
    elif input_generator.input_type_to_generate.startswith("F"): # Pair Source Followup
        input_generator.prompt_template_symbols = input_generator.base_prompt_template_symbols+"F"

        input_generator.Crafted_prompts_dir = input_generator.Crafted_promptsF_dir
        input_generator.prompt_results_content_dir = input_generator.promptF_results_content_dir
        input_generator.prompts_results_raw_dir = input_generator.promptsF_results_raw_dir
    input_generator.prompt_template = Templates[input_generator.prompt_template_symbols]

    """prompt info & system message """
    input_generator = construct_prompt.generate_prompt_from_profile(input_generator, task_type="input_generation")

    return input_generator


def generate_Inputs_by_prompting(input_generator, skipRequestIfExist=True):
    print('+++ START: generate_Inputs_by_prompting ', input_generator.MTC_item["FQS_testMethos"])
    MTC_item = input_generator.MTC_item
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"LOG: START, generate_Inputs_by_prompting: {MTC_item['FQS_testMethos']}")
    FQS_testMethos = MTC_item["FQS_testMethos"]
    MTChClass = input_generator.MTChClass
    prompt_path = input_generator.prompt_path

    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"

    prompt_path = input_generator.prompt_path
    prompt = file_processing.read_TXTfile(prompt_path)
    promt_id = input_generator.promt_id
    prompt_results_content_dir= input_generator.prompt_results_content_dir
    prompts_results_raw_dir = input_generator.prompts_results_raw_dir
    prompt_generated_inputs_dir = input_generator.prompt_generated_inputs_dir
    system_message = input_generator.prompt_system_message
    """ prompt """
    response_content_path = f"{prompt_results_content_dir}{promt_id}.md"
    response_content = ''
    # copy the prompt from Qwen's results; HARDCODED
    if input_generator.input_type_to_generate == "Source" and "_effect" in Setting["eval"]: 
        # previous practice
        # from: get the path prompt_response of qwen, ./cache/generateInputs/CodeQwen1.5-7B-Chat_Ti5-1_Temprature0.2_3/..
        cache_dir_name_for_this_setting = inputGenerator.get_cache_dir(Setting['index_of_request'], Setting)
        cache_dir_name_for_this_setting_qw =  f"CodeQwen1.5-7B-Chat_T{Setting['Prompt_template']}_Temprature{Setting['temperature']}_{Setting['index_of_request']}"
        path_qw_prompt_response = response_content_path.replace( cache_dir_name_for_this_setting,  cache_dir_name_for_this_setting_qw)
        # to response_content_path
        # file_processing.copyFile(path_qw_prompt_response, response_content_path)
        
        # now: 2024_0604
        global all_valid_Sinput
        path_qw_prompt_response = ""
        if FQS_testMethos in all_valid_Sinput.keys():
            if len(all_valid_Sinput[FQS_testMethos]) > 0:
                if len(all_valid_Sinput[FQS_testMethos]) > 5:
                    for ele in all_valid_Sinput[FQS_testMethos][:5]:
                        Sinput_code_block = ele["Sinput_code_block"]
                        path_qw_prompt_response += f"```java \n{Sinput_code_block}\n```\n\n\n"
                    all_valid_Sinput[FQS_testMethos] = all_valid_Sinput[FQS_testMethos][5:]
                elif len(all_valid_Sinput[FQS_testMethos]) <= 5:
                    for ele in all_valid_Sinput[FQS_testMethos]:
                        Sinput_code_block = ele["Sinput_code_block"]
                        path_qw_prompt_response += f"```java \n{Sinput_code_block}\n```\n\n\n"
                    all_valid_Sinput[FQS_testMethos] = []
                    print(f"ATTENTION: all_valid_Sinput[FQS_testMethos] = [], {FQS_testMethos}")

        else:
            print(f"ATTENTION: no valid Sinput, {FQS_testMethos}")
        count = 0
        for key in all_valid_Sinput.keys():
            count += len(all_valid_Sinput[key])
        print(f"LOG: len(all_valid_Sinput) = {count}")
        file_processing.write_TXTfile(response_content_path, path_qw_prompt_response)
    if input_generator.input_type_to_generate == "Followup" and "_effect" in Setting["eval"]: 
        # TODO, if Sprompt_response is empty, then FUresponse_content=""
        Sresponse_content_path = response_content_path.replace("/promptsF_results_content/", "/promptsS_results_content/")
        Sresponse_content = file_processing.read_TXTfile(Sresponse_content_path)
        if len(Sresponse_content) < 20: # Sprompt_response is empty
            file_processing.write_TXTfile(response_content_path, "")

    if not Setting["overwritePreviousPromptResults"] and file_processing.pathExist(response_content_path):
        response_content = file_processing.read_TXTfile(response_content_path)
    elif "gpt" in Setting["model"].lower(): 
        response_content = request_LLMs.request_GPT(prompt, Setting["model"], promt_id, Setting["temperature"],prompts_results_raw_dir, prompt_results_content_dir,system_message)
    else:
        response_content = request_LLMs.request_fastChat(prompt, Setting["model"], promt_id, Setting["temperature"],prompts_results_raw_dir, prompt_results_content_dir,system_message)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"LOG: END, generate_Inputs_by_prompting: {MTC_item['FQS_testMethos']}")

    # post-processing and write
    write_generated_inputs(response_content, input_generator)
    
    

def write_generated_inputs(response_content, input_generator):
    promt_id = input_generator.promt_id
    prompt_generated_inputs_dir = input_generator.prompt_generated_inputs_dir
    strategy = input_generator.strategy
    sourceInputs_TypeAndVariable = input_generator.sourceInputs_TypeAndVariable
    followUpInputs_TypeAndVariable = input_generator.followUpInputs_TypeAndVariable

    # input_generator.generated_input_blocks = []
    """ extract generated code blocks """
    # generated_class = request_LLMs.extract_generated_ITrans_class(response_content, promt_id,prompt_generated_inputs_dir)
    code_blocks = request_LLMs.extract_generated_inputs_blocks(response_content)
    # print("for checking: before, code_blocks\n", code_blocks)

    if len(code_blocks)==0:
        print(f"LOG: generated_content is empty, promt_id: {promt_id}")
        # file_processing.write_TXTfile(path=path_of_class_with_generated_test_input, content="empty")
    else:
        """ post-process, and construct generated inputs based MTCs """
        if input_generator.strategy == 1:
            input_generator.generated_input_blocks = [code_blocks[-1]] # 先取最后一个, TODO
            input_generator.generated_input_blocks_unique = remove_duplicates_in_order([code_blocks[-1]])

            generated_code_block = code_blocks[-1]
            if Setting["Prompt_template"] in ["i1", "i2", "i3"]:
                generated_class = post_process_inputs(generated_code_block,input_generator)
            else:
                generated_class = post_process_inputs_when_only_return_inputsSTMTs(generated_code_block,input_generator)
        elif input_generator.strategy == 2 and input_generator.input_type_to_generate.startswith("S"):
            input_generator.generated_Sinput_blocks = code_blocks
            # input_generator.generated_Sinput_blocks_unique = remove_duplicates_in_order(code_blocks)
            post_processed_code_blocks = post_process_generated_Sinput(code_blocks, sourceInputs_TypeAndVariable, input_generator)
            input_generator.postprocessed_generated_input_blocks = post_processed_code_blocks
            input_generator.postprocessed_generated_input_blocks_unique = remove_duplicates_in_order(post_processed_code_blocks)

        elif input_generator.strategy == 2 and input_generator.input_type_to_generate.startswith("F"):
            input_generator.generated_input_blocks = code_blocks
            input_generator.generated_input_blocks_unique = remove_duplicates_in_order(code_blocks)

        
        # write file
        for index_of_block in range(len(input_generator.generated_input_blocks_unique)):
            # some setting
            generated_input_blockid  = f"{promt_id}{index_of_block}"
            path_of_class_with_generated_test_input = f"{prompt_generated_inputs_dir}{generated_input_blockid}.java"
            invoked_package_FQN = input_generator.invoked_package_FQN
            new_test_class_name = f"{input_generator.MTChClass}{index_of_block}"
            new_test_method_name = f"{input_generator.MTChMethod}Test{index_of_block}"
            generated_inputs_package_FQN = f"{invoked_package_FQN}"
            # input_generator.generated_inputs_package_FQN = generated_inputs_package_FQN
            generated_inputs_class_FQN = f"{generated_inputs_package_FQN}.{new_test_class_name}"
            # input_generator.generated_inputs_class_FQN = generated_inputs_class_FQN

            generated_code_block = input_generator.generated_input_blocks_unique[index_of_block]
            generated_class = post_process_inputs_when_only_return_inputsSTMTs(generated_code_block,input_generator, new_test_method_name, new_test_class_name)
            file_processing.write_TXTfile(path=path_of_class_with_generated_test_input, content=generated_class)
            # extracted_code = extract_code.extract_stmts_of_declaring_variables(sourceInputs_TypeAndVariable+followUpInputs_TypeAndVariable, generated_code_block)
            extracted_code = extract_code.variableDefExtractor(generated_code_block, sourceInputs_TypeAndVariable+followUpInputs_TypeAndVariable, input_generator= input_generator, extract_code_from_MTC=False).extract_variable_def_code()

            # input_generator.path_of_generated_MTChClass_list.append(path_of_class_with_generated_test_input)
            input_generator.generated_inputs_items[generated_inputs_class_FQN]={
                "generated_input_blockid": generated_input_blockid,
                "path_of_class_with_generated_test_input": path_of_class_with_generated_test_input,
                "generated_class_name": new_test_class_name,
                "generated_test_method_name": new_test_method_name,
                "generated_inputs_package_FQN": generated_inputs_package_FQN,
                "generated_inputs_class_FQN": generated_inputs_class_FQN,
                "LLM_generated_code_block": generated_code_block,
                "extracted_code": extracted_code
            }

    """ write generation result """
    generated_inputs_for_this_MTC = []
    all_generated_inputs = {}
    generated_inputs_path = input_generator.generated_inputs_path
    MTC_item = input_generator.MTC_item
    FQS_testMethos =  MTC_item["FQS_testMethos"]

    # get data
    # format, delete the white space before each line
    generated_inputs_for_this_MTC = {}
    post_processed_generated_inputs = {}
    all_generated_inputs_for_this_MTC = []
    original_h_inputs = [line.strip() for line in input_generator.inputSTMTs.split("\n")] 
    for code_block in code_blocks:
        all_generated_inputs_for_this_MTC.append([line.strip() for line in code_block.split("\n")])

    generated_inputs_class_FQNs = []
    for generated_inputs_class_FQN in input_generator.generated_inputs_items:
        LLM_generated_code_block = input_generator.generated_inputs_items[generated_inputs_class_FQN]["LLM_generated_code_block"]
        extracted_code = input_generator.generated_inputs_items[generated_inputs_class_FQN]["extracted_code"]

        generated_inputs_class_FQNs.append( generated_inputs_class_FQN )
        generated_inputs_for_this_MTC[generated_inputs_class_FQN] = [line.strip() for line in LLM_generated_code_block.split("\n")] 
        post_processed_generated_inputs[generated_inputs_class_FQN] = [line.strip() for line in extracted_code.split("\n")]  
    
    # MTC_with_processed_generated_inputs = [input_generator.testCase_with_generated_new_input]
    with file_lock: 
        if file_processing.pathExist(generated_inputs_path) and len( file_processing.read_TXTfile(generated_inputs_path) )>0:
            print("LOG: generated_inputs_path: ", generated_inputs_path)
            all_generated_inputs = json_processing.read(generated_inputs_path)
            if FQS_testMethos in all_generated_inputs:
                all_generated_inputs.pop(FQS_testMethos)
            all_generated_inputs[FQS_testMethos] = {
                "generated_inputs_class": generated_inputs_class_FQNs,
                "generated_all_blocks": all_generated_inputs_for_this_MTC,
                "selected": generated_inputs_for_this_MTC,       
                "processed_generated": post_processed_generated_inputs, 
                # "MTC_with_processed": MTC_with_processed_generated_inputs, 
                "original_h": original_h_inputs}
            json_processing.write( json_content=all_generated_inputs, path=generated_inputs_path)
        else:
            all_generated_inputs[FQS_testMethos] = {
                "generated_inputs_class": generated_inputs_class_FQNs,
                "generated_all_blocks": all_generated_inputs_for_this_MTC,
                "selected": generated_inputs_for_this_MTC,       
                "processed_generated": post_processed_generated_inputs, 
                # "MTC_with_processed": MTC_with_processed_generated_inputs, 
                "original_h": original_h_inputs}
            json_processing.write( json_content=all_generated_inputs, path=generated_inputs_path)


def remove_duplicates_in_order(input_list):
    output_list = []
    formated_output_list = []
    for item in input_list:
        formated_item = [ line.strip() for line in item.split("\n")]
        if item not in output_list and formated_item not in formated_output_list:
            output_list.append(item)
            formated_output_list.append(formated_item)
    return output_list

def post_process_generated_Sinput(input_list, sourceInputs_TypeAndVariable, input_generator):
    output_list = []
    for block in input_list:
        # def_stmts = extract_code.extract_stmts_of_declaring_variables(sourceInputs_TypeAndVariable, block)
        def_stmts =  extract_code.variableDefExtractor(block, sourceInputs_TypeAndVariable, input_generator= input_generator, extract_code_from_MTC=False).extract_variable_def_code()
        output_list.append(def_stmts    )
    return output_list


def post_process_inputs_when_only_return_inputsSTMTs(generated_content,input_generator, new_test_method_name="", new_test_class_name=""):
    """ 
        以MTC_h_only_test_class_file_path为基底进行修改，防止需要 helper methods
    """
    # print("for checking: before, generated_content\n", generated_content)
    MTC_item = input_generator.MTC_item
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    FQS_testMethos = MTC_item["FQS_testMethos"]
    model_symbol = model_symbols[Setting["model"]]
    input_generator.generated_inputs_folder_name  = model_symbol
    pre_processed_MTC_h_code = input_generator.pre_processed_MTC_h_code

    sourceInputs_TypeAndVariable = input_generator.sourceInputs_TypeAndVariable
    followUpInputs_TypeAndVariable = input_generator.followUpInputs_TypeAndVariable

    """ some settings """
    invoked_package_FQN = input_generator.invoked_package_FQN
    generated_inputs_package_FQN = f"{invoked_package_FQN}"
    input_generator.generated_inputs_package_FQN = generated_inputs_package_FQN
    generated_inputs_class_FQN = f"{generated_inputs_package_FQN}.{input_generator.MTChClass}"
    input_generator.generated_inputs_class_FQN = generated_inputs_class_FQN

    """ get: content of MTC_h_only_test_class """
    # MTC_h_only_test_file_path
    MTC_h_only_test_file_path = input_generator.MTC_h_only_test_file_path
    MTC_h_only_class_name = MTC_h_only_test_file_path.split("/")[-1].replace(".java", "")
    MTC_h_method_name = f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}" # GT: crafted MTC_h_method_name
    # replace a method with another method
    generated_class = java_parser.replace_method(file_path=MTC_h_only_test_file_path, method_name=MTC_h_method_name, function="replaceMethod", new_method_declaration=pre_processed_MTC_h_code)

    """ extract&replace generated_input_statements from generated content """

    # get generated inputSTMTs, TODO: 防止Trans比较复杂，无法只用一句statements生成inputs‘ potential solution: 从第一个 inputs generation statement开始，至最后一个input statement。 # OR solution: only extract inputs related statements, 
    generated_inputSTMTs = ""
    generated_inputSTMTs_dict = {}
    lines_of_generated_content = generated_content.split("\n")
    for line_index in range(len(lines_of_generated_content)):
        line = lines_of_generated_content[line_index]
        if "=" not in line: continue # not varible declaration line
        for ele in sourceInputs_TypeAndVariable + followUpInputs_TypeAndVariable:
            if line.strip().startswith(ele) and line.split("=")[0].strip() == ele: # 有且仅有 ele， 防止是 ele* 这种
                generated_inputSTMTs += f"{line}\n"
                generated_inputSTMTs_dict[ele] = line

    variable_def_extractor = extract_code.variableDefExtractor(generated_content, sourceInputs_TypeAndVariable + followUpInputs_TypeAndVariable, input_generator= input_generator, extract_code_from_MTC=False)
    generated_inputSTMTs = variable_def_extractor.extract_variable_def_code()
    generated_inputSTMTs_lines = generated_inputSTMTs.split("\n")
    generated_inputSTMTs_dict = variable_def_extractor.varible_and_its_direct_def

    # only generated_inputSTMTs_lines will beused later, generated_inputSTMTs_lines is not 
    print("for checking: before, generated_inputSTMTs\n", generated_inputSTMTs)
    before_ = generated_inputSTMTs
    if "_ablateRefinement" in Setting["ablation"]:
        generated_inputSTMTs = generated_content
        generated_inputSTMTs_lines = generated_inputSTMTs.split("\n")
        generated_inputSTMTs_dict = variable_def_extractor.varible_and_its_direct_def
    print("for checking: after, generated_inputSTMTs\n", generated_inputSTMTs)
    if before_ != generated_inputSTMTs: 
        print("for checking: before_ != generated_inputSTMTs")

    # inputSTMTs_in_MTC_h_class = extract_code.variableDefExtractor(generated_class, sourceInputs_TypeAndVariable + followUpInputs_TypeAndVariable, input_generator= input_generator).extract_variable_def_code()
    extrator = extract_code.variableDefExtractor(pre_processed_MTC_h_code, sourceInputs_TypeAndVariable + followUpInputs_TypeAndVariable, input_generator= input_generator)
    inputSTMTs_in_MTC_h_class = extrator.extract_variable_def_code()
    inputSTMTs_in_MTC_h_class_lines = [ line.strip() for line in inputSTMTs_in_MTC_h_class.split("\n")] # formated ... 


    # delete original inputSTMTs
    print( "before: generated_class: ", generated_class )
    generated_class = generated_class.replace(pre_processed_MTC_h_code, generated_inputSTMTs) # ?
    # lines_of_generated_class = generated_class.split("\n")
    # for line_index in range(len(lines_of_generated_class)):
    #     line = lines_of_generated_class[line_index]
    #     if "=" not in line: continue # not varible declaration line
    #     for ele in sourceInputs_TypeAndVariable + followUpInputs_TypeAndVariable:
    #         if line.strip().startswith(ele) and line.split("=")[0].strip() == ele: # 有且仅有 ele， 防止是 ele* 这种
    #             lines_of_generated_class[line_index] = ""   # 先删掉
    #             if ele in generated_inputSTMTs_dict:     
    #                 # lines_of_generated_class[line_index] = f"{line.split(ele)[0]}{generated_inputSTMTs_dict[ele].strip()}"      # 再替换
    #                 lines_of_generated_class[line_index] = f"{line.split(ele)[0]}{generated_inputSTMTs_dict[ele]}"              # 再替换, 多一个缩进，便于看出哪些是新内容
    #             else:   # if a input is not generated
    #                 pass  # 暂时pass，等到编译时会报错
    # generated_class = ("\n").join(lines_of_generated_class)

    # 这里可以借用 input_generator.MTChClass / MTChxName
    original_MTC_simple_name = f"{test_simple_name}"

    lines_of_generated_class = generated_class.split("\n")
    lines_of_updated_generated_class = []
    flag_this_test_case_to_discard = False
    flag_lines_to_discard = False
    flag_already_inserted = False
    for line_index in range(len(lines_of_generated_class)):
        line = lines_of_generated_class[line_index]
        formated_line = line.strip()
        # flag_this_test_case_to_discard, 防止误伤其他 setup method
        if f"void {original_MTC_simple_name}" in line: 
            flag_this_test_case_to_discard = True
        if flag_this_test_case_to_discard and "}" == formated_line: # 该test case 结束
            flag_this_test_case_to_discard = False

        
        # flag_this_test_case_to_discard: 防止误伤其他 setup method
        # line in inputSTMTs_in_MTC_h_class_lines: 说明是原来的inputSTMTs start
        if flag_this_test_case_to_discard and formated_line in inputSTMTs_in_MTC_h_class_lines: 
            flag_lines_to_discard = True 
            continue # so , no lines_of_updated_generated_class.append(line)

        # not flag_already_inserted： 未曾insert 过，确保只insert一次
        # line in inputSTMTs_in_MTC_h_class_lines: 说明是原来的inputSTMTs end，这已经不想干的一行了。。。
        if not flag_already_inserted and flag_lines_to_discard and formated_line not in inputSTMTs_in_MTC_h_class_lines: 
            lines_of_updated_generated_class.extend(generated_inputSTMTs_lines)# insert generated_inputSTMTs
            flag_lines_to_discard = False
            flag_already_inserted = True
        # if formated_line not in inputSTMTs_in_MTC_h_class_lines: # 防止重复。。。
        # hardcode special cases: 
        if ("String str2 = JSON.toJSONString(v01);" in line and FQS_testMethos == "com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest.test()") \
            or ("String str2 = JSON.toJSONString(v01);" in line and FQS_testMethos == "com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest.test1()")\
            or ("String input = sb.toString();" in line and FQS_testMethos == "org.tsugi.util.Base64DoubleUrlEncodeSafeTest.testAllNonSurrogateCodePoints()")\
            or ('String encoded2 = "AQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRobHB0eHyAhIiMkJSYnKCkqKywtLi8wMTIzNDU2Nzg5Ojs8PT4_QEFCQ0RFRkdISUpLTE1OT1BRUlNUVVZXWFlaW1xdXl9gYWJj";' in line and FQS_testMethos == "org.tsugi.util.Base64DoubleUrlEncodeSafeTest.testAllNonSurrogateCodePoints()")\
            or ("String message = encryptedValue;" in line and FQS_testMethos == "com.vladmihalcea.hpjp.util.CryptoUtilsTest.testPerformanceUsingCache()")\
            or ("Class<?> clazz = Long.class;" in line and FQS_testMethos == "com.vladmihalcea.hpjp.util.CryptoUtilsTest.testPerformanceUsingCache()")\
            or ("MySqlInsertStatement sqlStatement2 = (MySqlInsertStatement) SQLUtils.parseSingleStatement(sql, DbType.mysql, true);" in line and FQS_testMethos == "com.alibaba.druid.bvt.sql.mysql.issues.Issue5686.test_column_comment()")\
            or ( "YearHalf test2 = YearHalf.of(year2, half2);" in line and FQS_testMethos == "org.threeten.extra.TestYearHalf.test_of_int_int()"):
            continue # not append such line
        lines_of_updated_generated_class.append(line)

    generated_class = ("\n").join(lines_of_updated_generated_class)
    print( "after: generated_class: ", generated_class )

    """ change class and method name """
    # 这里可以借用 input_generator.MTChClass / MTChxName
    original_MTC_simple_name = f"{test_simple_name}"
    # change class name
    if new_test_class_name == "": new_test_class_name = f"{input_generator.MTChClass}"    
    generated_class = generated_class.replace(f"{MTC_h_only_class_name}", f"{new_test_class_name}")
    # change method name: original_MTC_simple_name -> MTChxName
    if new_test_method_name == "": new_test_method_name = f"{input_generator.MTChMethod}"
    generated_class = generated_class.replace(f"void {original_MTC_simple_name}", f"void {new_test_method_name}")
    # print( "generated_class: ", generated_class )

    # input_generator.generated_input_relatedSTMTs = [generated_inputSTMTs_dict[ele].strip() for ele in generated_inputSTMTs_dict.keys()]
    return generated_class


def post_process_inputs(generated_class,input_generator):
    index_of_request = input_generator.index_of_request
    MTC_item = input_generator.MTC_item
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    model_symbol = model_symbols[Setting["model"]]
    input_generator.generated_inputs_folder_name  = model_symbol

    """ package_statement """
    invoked_package_FQN = input_generator.invoked_package_FQN
    # generated_inputs_package_FQN = f"{model_symbol}.{invoked_package_FQN}"
    generated_inputs_package_FQN = f"{invoked_package_FQN}"
    input_generator.generated_inputs_package_FQN = generated_inputs_package_FQN
    generated_inputs_class_FQN = f"{generated_inputs_package_FQN}.{input_generator.MTChClass}"
    input_generator.generated_inputs_class_FQN = generated_inputs_class_FQN
    package_statement = f"package {generated_inputs_package_FQN};"
    
    # """ add junit """
    # pattern = r'@Test'
    # matches = re.findall(pattern, generated_class)
    # if len( matches ) >0: # 说明有生成test
    #     if Junit_STATEMENT not in generated_class: # 说明没有import junit statement
    #         generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{Junit_STATEMENT}")

    # """ add CUT in import statements """
    # import_dependencies = MTC_item["dependency"].split(";")
    # import_statement = ("\n").join( [f"import {ele};" for ele in import_dependencies ] )
    # generated_class = generated_class.replace(f"{package_statement}", f"{package_statement}\n\n{import_statement}")
        
    """ add import statements from crafted MTC_h_only_test_class_file_path """
    # identify original import statements
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    poj_name = MTC_item["poj_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    class_name = f"{MTC_test_class_name}_{test_simple_name}"
    poj_ITRANS_MTC_ITrans_DIR = ITRANS_MTCIT_DIR % poj_name

    MTC_h_only_test_class_name = f"{class_name}{HARDCODED_CLASS_SUFFIX}Test"
    MTCITrans_only_test_class_dir = f"{poj_ITRANS_MTC_ITrans_DIR}{invoked_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(MTCITrans_only_test_class_dir)
    MTC_h_only_test_class_file_path = f"{MTCITrans_only_test_class_dir}{MTC_h_only_test_class_name}.java"

    test_file = file_processing.read_TXTfile(MTC_h_only_test_class_file_path)
    import_statements_in_original_test_file = []
    import_statements_toadd = []
    for line in test_file.split("\n"):
        # if not in genearted import statements
        if line.startswith("import ") and line not in generated_class: 
            import_statements_in_original_test_file.append(line)
            import_statements_toadd.append(line)

    import_statements_block_toadd = ("\n").join(import_statements_toadd)

    """ update generated class """
    # using re to identify "package [a-zA-Z0-9.]*;" and replace it with "package [a-zA-Z0-9.]*.ITrans;"
    pattern = r'package [a-zA-Z0-9.]*;'
    matches = re.findall(pattern, generated_class)
    if len( matches ) >1:
        print( "len( matches ) >1:", len(matches) )
    elif len( matches ) ==1: # 说明有package statement
        generated_class = generated_class.replace(matches[0], f"{package_statement}\n\n{import_statements_block_toadd}\n\n")
    elif len( matches ) ==0: # 说明没有package statement
        generated_class = f"{package_statement}\n\n{import_statements_block_toadd}\n\n{generated_class}"

    # test name changing: original_MTC_simple_name -> MTChxName
    original_MTC_simple_name = f"{test_simple_name}"
    # method_name_hardcoded = f"{MTC_test_class_name}_{test_simple_name}{HARDCODED_CLASS_SUFFIX}"
    method_name_hardcoded = f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}"
    MTChxName = f"{method_name_hardcoded}{index_of_request}"

    generated_class = generated_class.replace(f"void {original_MTC_simple_name}", f"void {MTChxName}")
    # generated_class = generated_class.replace(f"void {method_name_hardcoded}", f"void {MTChxName}")
    return generated_class


def validate_generated_Inputs_pre(input_generator, skipCompileIfExist=True):
    """
    prepare: cp GT_ITrans -> src/; and compile;if success: 
    cp generated_MTC_ITrans -> src/; and compile > .log;
    if success: do testing > .log (refer to AutoMR的做法)
    复位: cp GT_ITrans -> src/; and compile;
    """
    MTC_item = input_generator.MTC_item
    generated_inputs_folder_name = input_generator.generated_inputs_folder_name
    generated_inputs_package_FQN = input_generator.generated_inputs_package_FQN
    generated_inputs_class_FQN = input_generator.generated_inputs_class_FQN # for each generated inputs
    MTChClass = input_generator.MTChClass                                   # for each generated inputs？new test class name?
    MTChMethod = input_generator.MTChMethod                                 # for each generated inputs？new test case name?
    prompt_generated_inputs_dir = input_generator.prompt_generated_inputs_dir
    log_dir = input_generator.compilation_log_dir

    Test_result = {"MTC_item":MTC_item, 
                   "generated_inputs_compilation_result": None, 
                   "generated_inputs_validation_result": None,
                   "generated_inputs_validation_exe_detail": None,
                   "generated_Sinput_compilation_result": None, # result will be given in construct_test4ITrans_from_generated_inputs
                    "generated_Sinput_validation_result": None,
                    "generated_Sinput_validation_exe_detail": None
    }

    poj_name = MTC_item["poj_name"]
    test_file_path = MTC_item["test_file_path"]
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]

    print("test generated inputs: ", invoked_methods_FQS, MTChClass)
    """ compile generated inputs in original poj """
    # prepare dir
    poj_ITRANS_GENERATED_INPUTS_DIR = ITRANS_GENERATED_INPUTS_DIR % poj_name
    dir_of_generated_input_in_original_poj = f"{poj_ITRANS_GENERATED_INPUTS_DIR}{generated_inputs_folder_name}/{generated_inputs_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(dir_of_generated_input_in_original_poj)
    path_of_generated_inputs_in_original_poj = f"{dir_of_generated_input_in_original_poj}{MTChClass}.java"
    # 复位: rm generated ITrans in original poj
    file_processing.remove_file(path_of_generated_inputs_in_original_poj)
    file_processing.remove_file(path_of_generated_inputs_in_original_poj.replace(".java",".class"))
    # copy: cache -> original poj
    dir_of_generated_inputs_in_cache = f"{prompt_generated_inputs_dir}"
    path_of_generated_inputs_in_cache = f"{prompt_generated_inputs_dir}{MTChClass}.java"
    file_processing.copyFile(source=path_of_generated_inputs_in_cache,target=path_of_generated_inputs_in_original_poj)
    # compile
    if skipCompileIfExist and file_processing.pathExist(path_of_generated_inputs_in_cache.replace(".java",".class")):
        print(f"Skip: {path_of_generated_inputs_in_cache} has been compiled")
        Test_result["generated_inputs_compilation_result"] = True
        file_processing.copyFile(source=path_of_generated_inputs_in_cache.replace(".java",".class"),target=dir_of_generated_input_in_original_poj)        
        # copy: extra needed classes
        num = 1;extra_class_path = path_of_generated_inputs_in_cache.replace(".java",f"${num}.class")
        while file_processing.pathExist(extra_class_path):
            file_processing.copyFile(source=extra_class_path,target=dir_of_generated_input_in_original_poj)
            num += 1; extra_class_path = path_of_generated_inputs_in_cache.replace(".java",f"${num}.class")
    else:
        poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
        poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
        poj_build_tool = poj_compilation_info["build_tool"][0]
        jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

        CMD_CD = f"cd {poj_dir};"
        PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)
        # path_of_generated_ITrans_in_original_poj
        # generated_dot_class_path = path_of_generated_ITrans_in_original_poj.replace(".java", ".class")
        cmd_result = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp="", Path_TestFile_to_compile = path_of_generated_inputs_in_original_poj, PATH_JAVAC=PATH_JAVAC, log_dir=log_dir, log_file_suffix="generated_inputs")
        if cmd_result != 0:
            Test_result["generated_inputs_compilation_result"] = False
        else:
            Test_result["generated_inputs_compilation_result"] = True
            # 放回cache中，备份一下。
            file_processing.copyFile(source=path_of_generated_inputs_in_original_poj.replace(".java",".class") ,target=dir_of_generated_inputs_in_cache)
            # copy: extra needed classes
            num = 1;extra_class_path = path_of_generated_inputs_in_original_poj.replace(".java",f"${num}.class")
            while file_processing.pathExist(extra_class_path):
                file_processing.copyFile(source=extra_class_path,target=dir_of_generated_inputs_in_cache)
                num += 1; extra_class_path = path_of_generated_inputs_in_original_poj.replace(".java",f"${num}.class")

    """ validate generated inputs """
    if Test_result["generated_inputs_compilation_result"]:
        exe_result = test_IT.execute_generated_inputs(input_generator, path_of_generated_inputs_in_original_poj, target_class_FQN=input_generator.generated_inputs_class_FQN, passIfexecuted=not Setting["overwritePreviousValidationResults"], test_exe_dir_BACKUP=input_generator.validation_log_dir)
        Test_result["generated_inputs_validation_exe_detail"] = exe_result

        num_of_passed_test_cases =  exe_result
        print(f"MTChMethod: {MTChMethod}") # 检查运行是否成功
        if num_of_passed_test_cases==0 or MTChMethod not in exe_result["passed_test_cases_list"]:
            print(f"Error, failed to execute: {generated_inputs_class_FQN} ")
            Test_result["generated_inputs_validation_result"] = False
        else:
            Test_result["generated_inputs_validation_result"] = True


    """ 复位: rm generated inputs in original poj """
    # # 倒也不必，如果成功了的话；因为 FQN都是独一无二的
    # if not (Test_result["generated_inputs_compilation_result"] and Test_result["generated_inputs_validation_result"]):
    #     file_processing.remove_file(path_of_generated_inputs_in_original_poj)
    #     file_processing.remove_file(path_of_generated_inputs_in_original_poj.replace(".java",".class"))

    """ write validation result """ # can be mv
    input_validation_result = Test_result
    validation_result_of_generated_inputs = []
    validation_result_of_generated_inputs_path = input_generator.validation_result_of_generated_inputs_path
    with file_lock: 
        if file_processing.pathExist(validation_result_of_generated_inputs_path) and len( file_processing.read_TXTfile(validation_result_of_generated_inputs_path) )>0:
                validation_result_of_generated_inputs = json_processing.read(validation_result_of_generated_inputs_path)
                for ele in validation_result_of_generated_inputs:
                    if ele["MTC_item"]["FQS_testMethos"] == MTC_item["FQS_testMethos"]:
                        validation_result_of_generated_inputs.remove(ele)
                validation_result_of_generated_inputs.append(input_validation_result)
                json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)
        else:
            validation_result_of_generated_inputs.append(input_validation_result)
        json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)
    
    input_generator.generated_inputs_validation_result = Test_result["generated_inputs_validation_result"]
    input_generator.path_of_generated_inputs_in_original_poj = path_of_generated_inputs_in_original_poj
    input_generator.Test_result  = Test_result
    return Test_result


def validate_generated_Inputs(input_generator, skipCompileIfExist=True):
    """
    prepare: cp GT_ITrans -> src/; and compile;if success: 
    cp generated_MTC_ITrans -> src/; and compile > .log;
    if success: do testing > .log (refer to AutoMR的做法)
    复位: cp GT_ITrans -> src/; and compile;
    """
    MTC_item = input_generator.MTC_item
    generated_inputs_folder_name = input_generator.generated_inputs_folder_name
    generated_inputs_package_FQN = input_generator.generated_inputs_package_FQN
    MTChClass = input_generator.MTChClass

    Test_results = {
        "MTC_item":MTC_item,
        "pair_inputs": {},
        "source_only_input": {}
    }
    # Test_results["pair_inputs/source_only_input"][generated_inputs_class_FQN] = Test_result
    for generated_inputs_class_FQN in input_generator.generated_inputs_items:
        generated_inputs_item = input_generator.generated_inputs_items[generated_inputs_class_FQN]
        print("test generated inputs: ",  MTC_item["invoked_methods_FQS"], generated_inputs_item["generated_inputs_class_FQN"])
        """ compile generated inputs in original poj """

        generated_input_blockid = generated_inputs_item["generated_input_blockid"]
        path_of_class_with_generated_test_input = generated_inputs_item["path_of_class_with_generated_test_input"]
        generated_class_name = generated_inputs_item["generated_class_name"]
        generated_test_method_name = generated_inputs_item["generated_test_method_name"]
        generated_inputs_package_FQN = generated_inputs_item["generated_inputs_package_FQN"]
        # generated_inputs_class_FQN = generated_inputs_item["generated_inputs_class_FQN"]

        # MTChClass = input_generator.MTChClass                                   # for each generated inputs？new test class name?
        # MTChMethod = input_generator.MTChMethod                                 # for each generated inputs？new test case name?
        prompt_generated_inputs_dir = input_generator.prompt_generated_inputs_dir
        log_dir = input_generator.compilation_log_dir

        Test_result = {
                    "generated_inputs_compilation_result": None, 
                    "generated_inputs_validation_result": None,
                    "generated_inputs_validation_exe_detail": None,
                    "generated_Sinput_compilation_result": None, # result will be given in construct_test4ITrans_from_generated_inputs
                        "generated_Sinput_validation_result": None,
                        "generated_Sinput_validation_exe_detail": None
        }

        poj_name = MTC_item["poj_name"]
        test_file_path = MTC_item["test_file_path"]
        invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
        """ compile generated inputs in original poj """
        # prepare dir
        poj_ITRANS_GENERATED_INPUTS_DIR = ITRANS_GENERATED_INPUTS_DIR % poj_name
        dir_of_generated_input_in_original_poj = f"{poj_ITRANS_GENERATED_INPUTS_DIR}{generated_inputs_folder_name}/{generated_inputs_package_FQN.replace('.','/')}/"
        file_processing.creatFolder_recursively_IfExistPass(dir_of_generated_input_in_original_poj)
        path_of_generated_inputs_in_original_poj = f"{dir_of_generated_input_in_original_poj}{generated_class_name}.java"

        # 复位: rm generated ITrans in original poj
        file_processing.remove_file(path_of_generated_inputs_in_original_poj)
        file_processing.remove_file(path_of_generated_inputs_in_original_poj.replace(".java",".class"))
        # copy: cache -> original poj
        dir_of_generated_inputs_in_cache = f"{prompt_generated_inputs_dir}"
        path_of_generated_inputs_in_cache = f"{prompt_generated_inputs_dir}{generated_class_name}.java"
        # path_of_generated_inputs_in_cache = path_of_class_with_generated_test_input
        file_processing.copyFile(source=path_of_generated_inputs_in_cache,target=path_of_generated_inputs_in_original_poj)
        # compile
        if skipCompileIfExist and file_processing.pathExist(path_of_generated_inputs_in_cache.replace(".java",".class")):
            print(f"Skip: {path_of_generated_inputs_in_cache} has been compiled")
            Test_result["generated_inputs_compilation_result"] = True
            file_processing.copyFile(source=path_of_generated_inputs_in_cache.replace(".java",".class"),target=dir_of_generated_input_in_original_poj)        
            # copy: extra needed classes
            num = 1;extra_class_path = path_of_generated_inputs_in_cache.replace(".java",f"${num}.class")
            while file_processing.pathExist(extra_class_path):
                file_processing.copyFile(source=extra_class_path,target=dir_of_generated_input_in_original_poj)
                num += 1; extra_class_path = path_of_generated_inputs_in_cache.replace(".java",f"${num}.class")
        else:
            poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
            poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
            poj_build_tool = poj_compilation_info["build_tool"][0]
            jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

            CMD_CD = f"cd {poj_dir};"
            PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)
            # path_of_generated_ITrans_in_original_poj
            # generated_dot_class_path = path_of_generated_ITrans_in_original_poj.replace(".java", ".class")
            cmd_result = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp="", Path_TestFile_to_compile = path_of_generated_inputs_in_original_poj, PATH_JAVAC=PATH_JAVAC, log_dir=log_dir, log_file_suffix="generated_inputs")
            if cmd_result != 0:
                Test_result["generated_inputs_compilation_result"] = False
            else:
                Test_result["generated_inputs_compilation_result"] = True
                # 放回cache中，备份一下。
                file_processing.copyFile(source=path_of_generated_inputs_in_original_poj.replace(".java",".class") ,target=dir_of_generated_inputs_in_cache)
                # copy: extra needed classes
                num = 1;extra_class_path = path_of_generated_inputs_in_original_poj.replace(".java",f"${num}.class")
                while file_processing.pathExist(extra_class_path):
                    file_processing.copyFile(source=extra_class_path,target=dir_of_generated_inputs_in_cache)
                    num += 1; extra_class_path = path_of_generated_inputs_in_original_poj.replace(".java",f"${num}.class")

        """ validate generated inputs """
        if Test_result["generated_inputs_compilation_result"]:
            exe_result = test_IT.execute_generated_inputs(input_generator, path_of_generated_inputs_in_original_poj, target_class_FQN=generated_inputs_class_FQN, passIfexecuted=not Setting["overwritePreviousValidationResults"], test_exe_dir_BACKUP=input_generator.validation_log_dir)
            Test_result["generated_inputs_validation_exe_detail"] = exe_result

            num_of_passed_test_cases =  exe_result
            # print(f"MTChMethod: {generated_test_method_name}") # 检查运行是否成功
            if num_of_passed_test_cases==0 or generated_test_method_name not in exe_result["passed_test_cases_list"]:
                print(f"Error, failed to execute: {generated_inputs_class_FQN} ")
                Test_result["generated_inputs_validation_result"] = False
            else:
                Test_result["generated_inputs_validation_result"] = True


        """ 复位: rm generated inputs in original poj """
        # # 倒也不必，如果成功了的话；因为 FQN都是独一无二的
        # if not (Test_result["generated_inputs_compilation_result"] and Test_result["generated_inputs_validation_result"]):
        #     file_processing.remove_file(path_of_generated_inputs_in_original_poj)
        #     file_processing.remove_file(path_of_generated_inputs_in_original_poj.replace(".java",".class"))

        """ write validation result """ # can be mv, and to update in the correct position
        # input_validation_result = Test_result
        # validation_result_of_generated_inputs = []
        # validation_result_of_generated_inputs_path = input_generator.validation_result_of_generated_inputs_path
        # with file_lock: 
        #     if file_processing.pathExist(validation_result_of_generated_inputs_path) and len( file_processing.read_TXTfile(validation_result_of_generated_inputs_path) )>0:
        #             validation_result_of_generated_inputs = json_processing.read(validation_result_of_generated_inputs_path)
        #             for ele in validation_result_of_generated_inputs:
        #                 if ele["MTC_item"]["FQS_testMethos"] == MTC_item["FQS_testMethos"]:
        #                     validation_result_of_generated_inputs.remove(ele)
        #             validation_result_of_generated_inputs.append(input_validation_result)
        #             json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)
        #     else:
        #         validation_result_of_generated_inputs.append(input_validation_result)
        #     json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)
        
        # input_generator.generated_inputs_validation_result = Test_result["generated_inputs_validation_result"]
        # input_generator.path_of_generated_inputs_in_original_poj = path_of_generated_inputs_in_original_poj
        # input_generator.Test_result  = Test_result # to be udpated, nor correct!
        
        Test_results["pair_inputs"][generated_inputs_class_FQN] = Test_result
        input_generator.generated_inputs_items[generated_inputs_class_FQN]["path_of_generated_inputs_in_original_poj"] = path_of_generated_inputs_in_original_poj
    input_generator.Test_results = Test_results
    return Test_results


def construct_test4ITrans_from_generated_inputs(input_generator, skipCompileIfExist=True):
    """ 
        1. construct test cases for generated Trans based on generated inputs
            change package name: w.* -> wIT.*
            add the import statements of generated Trans..
            replace construct of follow-up inputs with "inputTransformation function" 
        2. compiled constructed test cases for generated Trans
    """
    # if not input_generator.generated_inputs_validation_result: return # because we need to validate the generated source input only
    MTC_item = input_generator.MTC_item
    invoked_package_FQN = input_generator.invoked_package_FQN
    cache_generated_valid_inputs_testing_Trans_dir = input_generator.cache_generated_valid_inputs_testing_Trans_dir
    MTChClass = input_generator.MTChClass
    # MTChClassValid = f"{MTChClass}{VALID_INPUT_CLASS_SUFFIX}"
    # generated_inputs_class_name = MTChClass
    # generated_valid_inputs_class_name = MTChClassValid
    # generated_inputs_class_FQN = input_generator.generated_inputs_class_FQN
    # generated_valid_inputs_class_FQN = f"{generated_inputs_class_FQN.replace(generated_inputs_class_name, generated_valid_inputs_class_name)}"
    log_dir = input_generator.compilation_log_dir
    sourceInputs_TypeAndVariable = input_generator.sourceInputs_TypeAndVariable
    followUpInputs_TypeAndVariable = input_generator.followUpInputs_TypeAndVariable


    model_symbol = model_symbols[Setting["model"]]
    poj_name = MTC_item["poj_name"]
    test_simple_name = MTC_item["test_simple_name"]
    test_file_path = MTC_item["test_file_path"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    class_name = f"{MTC_test_class_name}_{test_simple_name}"

    poj_ITRANS_RAW_DIR = ITRANS_RAW_DIR % poj_name
    poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name
    poj_ITRANS_GENERATED_INPUTS_DIR = ITRANS_GENERATED_INPUTS_DIR % poj_name

    for generated_inputs_class_FQN in input_generator.generated_inputs_items:
        generated_inputs_item = input_generator.generated_inputs_items[generated_inputs_class_FQN]
        generated_input_blockid = generated_inputs_item["generated_input_blockid"]
        path_of_class_with_generated_test_input = generated_inputs_item["path_of_class_with_generated_test_input"]
        generated_class_name = generated_inputs_item["generated_class_name"]
        generated_test_method_name = generated_inputs_item["generated_test_method_name"]
        generated_inputs_package_FQN = generated_inputs_item["generated_inputs_package_FQN"]
        # generated_inputs_class_FQN = generated_inputs_item["generated_inputs_class_FQN"]

        path_of_generated_inputs_in_original_poj = generated_inputs_item["path_of_generated_inputs_in_original_poj"]


        MTChClassValid = f"{MTChClass}{VALID_INPUT_CLASS_SUFFIX}"
        generated_inputs_class_name = generated_class_name
        generated_valid_inputs_class_name = f"{generated_class_name}{VALID_INPUT_CLASS_SUFFIX}"
        generated_valid_inputs_class_FQN = f"{generated_inputs_class_FQN.replace(generated_inputs_class_name, generated_valid_inputs_class_name)}"

        """ 1. construct test cases for generated Trans based on generated inputs """
        generated_inputs_class = file_processing.read_TXTfile(path_of_generated_inputs_in_original_poj)
        package_line = ""
        for line in generated_inputs_class.split("\n"):
            if line.startswith("package "):
                package_line = line
                break
        updated_package_line = package_line
        
        # add the import statements of generated Trans..
        import_statement = f"import {invoked_package_FQN}.{class_name};"
        if import_statement not in generated_inputs_class:
            generated_inputs_class = generated_inputs_class.replace(f"{updated_package_line}", f"{updated_package_line}\n\n{import_statement}")
        
        # replace the class name: generated_inputs_class_name -> generated_valid_inputs_class_name
        generated_inputs_class = generated_inputs_class.replace(f"class {generated_inputs_class_name} ", f"class {generated_valid_inputs_class_name} ")

        # replace construct of follow-up inputs with "inputTransformation function"
        flag_multiple_followUpInputs = False 
        sourceInputsContent = MTC_item["sourceInput"]
        followUpInputsContent = MTC_item["followUpInput"]
        followUpInputs_TypeAndVariable_dictInfo = {}
        for followUpInput in followUpInputsContent:
            TypeAndVariableStr = f"{followUpInput['type']} {followUpInput['expression']}"
            # followUpInputs_TypeAndVariable.append( f"{TypeAndVariableStr}" )
            followUpInputs_TypeAndVariable_dictInfo[TypeAndVariableStr] = { "type": followUpInput['type'], "expression": followUpInput['expression']}
        if len(followUpInputsContent)>1:
            flag_multiple_followUpInputs = True
        # transfromation function invocation statment
        args_expression = (", ").join([ sourceinput["expression"] for sourceinput in sourceInputsContent])
        trans_invocation = f"{class_name}.inputTransformation_{test_simple_name}({args_expression})"
        trans_invocation_statement = ""

        if flag_multiple_followUpInputs:
            trans_invocation_statement = f"\t\tList<Object> transformed_inputs = {trans_invocation};"
        """ replace: the construction of source and follow-up inputs """
        lines_of_testClass = generated_inputs_class.split("\n")
        lines_of_updatedTestClass = []

        # for line_index in range(len(lines_of_testClass)):
        flag_already_insert_trans_invocation_statement = False
        line_index = -1
        while line_index < len(lines_of_testClass)-1:
            line_index += 1
            line = lines_of_testClass[line_index]
            lines_of_updatedTestClass.append(line)  # 先给加进来。
            if "= " not in line: continue           # not varible declaration line

            for ele in followUpInputs_TypeAndVariable: # follow up input, declaration line
                if line.strip().startswith(ele) and line.split("=")[0].strip() == ele: # 有且仅有 ele， 防止是 ele* 这种
                    lines_of_updatedTestClass = lines_of_updatedTestClass[:-1] # remove the last line (which is the follow-up input declaration line)
                    updated_line = ""
                    if flag_multiple_followUpInputs: 
                        exe_index = followUpInputs_TypeAndVariable.index(ele)
                        # if exe_index==0: # add trans_invocation_statement
                        if not flag_already_insert_trans_invocation_statement: # add trans_invocation_statement, 先到先得
                            flag_already_insert_trans_invocation_statement = True
                            lines_of_updatedTestClass.append(trans_invocation_statement)
                        followUpInputType = followUpInputs_TypeAndVariable_dictInfo[ele]["type"]
                        followUpInputVariable = followUpInputs_TypeAndVariable_dictInfo[ele]["expression"]
                        updated_line = f'{line.split("=")[0]} = ({followUpInputType}) transformed_inputs.get({exe_index});' # 
                    else:
                        updated_line = f'{line.split("=")[0]} = {trans_invocation};' # change to trans_invocation
                    lines_of_updatedTestClass.append(updated_line)

                    if not line.strip().endswith(";"): # 如果原来的行没有分号, 说明这一行没有结束，直接连后面几行一起删掉(即：skip)，直到遇到分号行为止。
                        while True:
                            line_index += 1
                            next_line = lines_of_testClass[line_index]
                            if next_line.strip().endswith(";"): break
                    break # 一次只会有一个follow-up input的替换
                            
        generated_inputs_class = ("\n").join(lines_of_updatedTestClass)
        print("generated_inputs_class: ", generated_inputs_class) 

        """ store """ # TO Check
        generated_valid_inputs_folder_name = f"{model_symbol}4ITrans"
        input_generator.generated_valid_inputs_folder_name = generated_valid_inputs_folder_name
        # valid_inputs_testing_ITrans_package_FQN = f"{model_symbol}4ITrans.{invoked_package_FQN}"
        valid_inputs_testing_ITrans_package_FQN = f"{invoked_package_FQN}"
        dir_of_gvalid_inputs_testing_ITrans_in_original_poj = f"{poj_ITRANS_GENERATED_INPUTS_DIR}{generated_valid_inputs_folder_name}/{valid_inputs_testing_ITrans_package_FQN.replace('.','/')}/"
        file_processing.creatFolder_recursively_IfExistPass(dir_of_gvalid_inputs_testing_ITrans_in_original_poj)

        # valid_inputs_testing_ITrans_FQN = f"{valid_inputs_testing_ITrans_package_FQN}.{class_name}"
        path_of_valid_inputs_testing_ITrans_in_original_poj = f"{dir_of_gvalid_inputs_testing_ITrans_in_original_poj}{generated_valid_inputs_class_name}.java"
        file_processing.write_TXTfile(path=path_of_valid_inputs_testing_ITrans_in_original_poj, content=generated_inputs_class)
        # in the cache
        dir_of_valid_inputs_testing_ITrans_in_cache = f"{cache_generated_valid_inputs_testing_Trans_dir}"
        path_of_valid_inputs_testing_ITrans_in_cache = f"{cache_generated_valid_inputs_testing_Trans_dir}{generated_valid_inputs_class_name}.java"
        file_processing.creatFolder_recursively_IfExistPass(cache_generated_valid_inputs_testing_Trans_dir)
        file_processing.copyFile(source=path_of_valid_inputs_testing_ITrans_in_original_poj, target=path_of_valid_inputs_testing_ITrans_in_cache)
        print(f"path_of_valid_inputs_testing_ITrans_in_cache: {path_of_valid_inputs_testing_ITrans_in_cache} ")

        """ compile """ 
        compilation_result = False
        # before that, 确保 mocked generated ITrans is there.
        # cp: from raw/ to generated Trans/
        backup_mocked_generated_IT_file_path = f"{poj_ITRANS_RAW_DIR}{class_name}.java"
        backup_mocked_generated_IT_compiled_class_path = backup_mocked_generated_IT_file_path.replace(".java", ".class")

        mocked_generated_IT_class_file_path = f"{poj_ITRANS_GENERATED_IT_DIR}{invoked_package_FQN.replace('.','/')}/{class_name}.java"
        mocked_generated_IT_compiled_class_file_path = mocked_generated_IT_class_file_path.replace(".java", ".class")
        file_processing.copyFile(source=backup_mocked_generated_IT_compiled_class_path, target=mocked_generated_IT_compiled_class_file_path)

        # compile
        # path_of_valid_inputs_testing_ITrans_in_original_poj
        if skipCompileIfExist and file_processing.pathExist(path_of_valid_inputs_testing_ITrans_in_cache.replace(".java",".class")):
            file_processing.copyFile(source=path_of_valid_inputs_testing_ITrans_in_cache.replace(".java",".class"),target=path_of_valid_inputs_testing_ITrans_in_original_poj.replace(".java",".class"))
            compilation_result = True
            print(f"Skip: {path_of_valid_inputs_testing_ITrans_in_cache} has been compiled")
        else:
            poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
            poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
            poj_build_tool = poj_compilation_info["build_tool"][0]
            jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

            poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name;
            extra_cp = f"{poj_ITRANS_GENERATED_IT_DIR}"
            # extra_cp = f"{crafted_subject.poj_ITRANS_GT_DIR}:{crafted_subject.poj_ITRANS_MTC_ITrans_DIR}:{crafted_subject.poj_ITRANS_GENERATED_IT_DIR}"

            CMD_CD = f"cd {poj_dir};"
            PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)
            cmd_result = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp=extra_cp, Path_TestFile_to_compile = path_of_valid_inputs_testing_ITrans_in_original_poj, PATH_JAVAC=PATH_JAVAC, log_dir=log_dir, log_file_suffix="4ITrans")
            if cmd_result != 0:
                compilation_result = False
                # 清理
                file_processing.remove_file(path_of_valid_inputs_testing_ITrans_in_original_poj)
            else:
                compilation_result = True
                # 放回cache中，备份一下。
                file_processing.copyFile(source=path_of_valid_inputs_testing_ITrans_in_original_poj.replace(".java",".class") ,target=path_of_valid_inputs_testing_ITrans_in_cache.replace(".java",".class"))
                file_processing.copyFile(source=path_of_valid_inputs_testing_ITrans_in_original_poj,target=dir_of_valid_inputs_testing_ITrans_in_cache)
                # copy: extra needed classes
                num = 1; extra_class_path = path_of_valid_inputs_testing_ITrans_in_original_poj.replace(".java",f"${num}.class")
                while file_processing.pathExist(extra_class_path):
                    file_processing.copyFile(source=extra_class_path,target=dir_of_valid_inputs_testing_ITrans_in_cache)
                    num += 1
                    extra_class_path = path_of_valid_inputs_testing_ITrans_in_original_poj.replace(".java",f"${num}.class")

        Test_result = input_generator.Test_results["pair_inputs"][generated_inputs_class_FQN]
        # Test_results["pair_inputs/source_only_input"][generated_inputs_class_FQN] = Test_result
        Test_result["generated_Sinput_compilation_result"] = compilation_result
        # execution_result
        """ validate constructed test cases """
        # TODO: mv GT to the corresponding dir? To check
        if compilation_result:
            exe_result = test_IT.execute_generated_inputs(input_generator,path_of_valid_inputs_testing_ITrans_in_cache, target_class_FQN=generated_valid_inputs_class_FQN, passIfexecuted=not Setting["overwritePreviousValidationResults"], test_exe_dir_BACKUP=input_generator.validation_log_dir)
            Test_result["generated_Sinput_validation_exe_detail"] = exe_result

            num_of_passed_test_cases =  exe_result['num_of_passed_test_cases']
            if num_of_passed_test_cases==0 or generated_test_method_name not in exe_result["passed_test_cases_list"]:
                print(f"Error, failed to execute: {generated_valid_inputs_class_FQN} ")
                Test_result["generated_Sinput_validation_result"] = False
            else:
                Test_result["generated_Sinput_validation_result"] = True
        input_generator.Test_results["pair_inputs"][generated_inputs_class_FQN] = Test_result
        
        """ write validation result """ # can be mv, to be update in the correct place
        input_validation_result = input_generator.Test_results
        validation_result_of_generated_inputs = []
        validation_result_of_generated_inputs_path = input_generator.validation_result_of_generated_inputs_path
        with file_lock: 
            if file_processing.pathExist(validation_result_of_generated_inputs_path) and len( file_processing.read_TXTfile(validation_result_of_generated_inputs_path) )>0:
                    validation_result_of_generated_inputs = json_processing.read(validation_result_of_generated_inputs_path)
                    for ele in validation_result_of_generated_inputs:
                        if ele["MTC_item"]["FQS_testMethos"] == MTC_item["FQS_testMethos"]:
                            validation_result_of_generated_inputs.remove(ele)
                    validation_result_of_generated_inputs.append(input_validation_result)
                    json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)
            else:
                validation_result_of_generated_inputs.append(input_validation_result)
            json_processing.write( json_content=validation_result_of_generated_inputs, path=validation_result_of_generated_inputs_path)

    # return compilation_result


def duplicate_inputs_checking(Setting):
    generated_inputs_result = {}
    for index_of_request in range(Setting["number_of_request"]):
        print(f"index_of_request {index_of_request}")
        # hx = f"{HARDCODED_CLASS_SUFFIX}{index_of_request}"
        cache_dir_name_for_this_setting = inputGenerator.get_cache_dir(index_of_request, Setting)
        cache_dir_for_this_setting = f"{ITRANS_CACHE_GENERATED_INPUTS_DIR}{cache_dir_name_for_this_setting}/"
        prompt_generated_inputs_dir = f"{cache_dir_for_this_setting}generated_inputs/"
        generated_inputs_path = f"{cache_dir_for_this_setting}generated_inputs.json"
        
        generated_inputs_single_run = {} 
        if file_processing.pathExist(generated_inputs_path):
            print( f"generated_inputs_path: {generated_inputs_path}" )
            generated_inputs_single_run = json_processing.read(generated_inputs_path)
        else:
            print( f"no generated_inputs_path: {generated_inputs_path}" )

        
        
        for MTC_FQN in generated_inputs_single_run.keys():
            if "org.threeten.extra.TestYearHalf.test_parse_CharSequenceDateTimeFormatter()" in MTC_FQN and index_of_request==9: 
                pass # for debugging

            original_h_inputs_stmts = generated_inputs_single_run[MTC_FQN]["original_h"]
            for generated_inputs_class_FQN in generated_inputs_single_run[MTC_FQN]["generated_inputs_class"]:
                MTC_hx_class_name = generated_inputs_class_FQN.split(".")[-1]
                MTC_hx_class_FQN = generated_inputs_class_FQN
                if MTC_FQN not in generated_inputs_result:
                    generated_inputs_result[MTC_FQN] = {
                        "generated_inputs_class":[], 
                        "unique_generated_inputs_class":[],
                        "duiplicate_inputs_dict":{ "h": [] }, # key: unique ones, value list: duplicate ones
                        "unique_generated_inputs_list":[],
                        "generated_inputs_class_info":{}
                }
                    
                # print( f"MTC_FQN: {MTC_FQN}",f"index_of_request: {index_of_request}")
                if len(generated_inputs_single_run[MTC_FQN]["processed_generated"])==0: continue
                generated_inputs_stmts = generated_inputs_single_run[MTC_FQN]["processed_generated"][generated_inputs_class_FQN] # 取第一个
                
                generated_inputs_class = generated_inputs_result[MTC_FQN]["generated_inputs_class"]
                duiplicate_inputs_dict = generated_inputs_result[MTC_FQN]["duiplicate_inputs_dict"]
                unique_generated_inputs_class = generated_inputs_result[MTC_FQN]["unique_generated_inputs_class"]
                unique_generated_inputs_list=generated_inputs_result[MTC_FQN]["unique_generated_inputs_list"]
                generated_inputs_class_info = generated_inputs_result[MTC_FQN]["generated_inputs_class_info"]
                generated_inputs_class_info[MTC_hx_class_name] = {"path": f"{prompt_generated_inputs_dir}{MTC_hx_class_name}.java", "FQN": MTC_hx_class_FQN}
                if MTC_hx_class_name not in generated_inputs_class: generated_inputs_class.append(MTC_hx_class_name)

                # 分类
                if generated_inputs_stmts == original_h_inputs_stmts:
                    duiplicate_inputs_dict["h"].append( MTC_hx_class_name )
                elif generated_inputs_stmts not in unique_generated_inputs_list:
                    unique_generated_inputs_list.append(generated_inputs_stmts)
                    unique_generated_inputs_class.append( MTC_hx_class_name )
                    duiplicate_inputs_dict[MTC_hx_class_name] = []
                else: 
                    duiplicate_index = unique_generated_inputs_list.index(generated_inputs_stmts)
                    duiplicate_class = unique_generated_inputs_class[duiplicate_index]
                    duiplicate_inputs_dict[duiplicate_class].append( MTC_hx_class_name )
                generated_inputs_result[MTC_FQN]["duiplicate_inputs_dict"] = duiplicate_inputs_dict
                generated_inputs_result[MTC_FQN]["unique_generated_inputs_class"] = unique_generated_inputs_class
                generated_inputs_result[MTC_FQN]["unique_generated_inputs_list"] = unique_generated_inputs_list
                generated_inputs_result[MTC_FQN]["generated_inputs_class"] = generated_inputs_class
                generated_inputs_result[MTC_FQN]["generated_inputs_class_info"] = generated_inputs_class_info
        
    # change to: validation_duplication.json
    duplicate_inputs_checking_results_path = all_evaluation_result_of_generated_inputs_function_path.replace(".json", "_duplicate_inputs.json")
    json_processing.write( json_content=generated_inputs_result, path=duplicate_inputs_checking_results_path)
    return generated_inputs_result


def result_collect(Setting, result_path=None, subject_list=None):
    duplicate_inputs_checking_results = duplicate_inputs_checking(Setting)
    evaluation_result = {
        "summary_v2":{
            "generated_input_pairs": 0,
            "generated_distinct_input_pairs": 0,
            "generated_distinct_valid_input_pairs": 0,
            "success_rate (distinct_valid_input_pairs)":0,
            "generated_distinct_valid_Sinput": 0,
            "success_rate (distince_valid_Sinput)":0,
            "success_rate (valid FUinput, when given valid Sinput)":0,
            "---": "---",
            "all_subject": 0,
            "subjects with distinct valid input pairs": 0,
            "distinct valid input pairs (average)": 0,
            "subjects with distinct valid Sinput": 0,
            "distinct valid Sinput (average)": 0,
        },
        "summary":{
            "all_subject": 0,
            "subject_size (generated with compilable inputs)":0,
            "subject_size (generated with valid inputs)":0,
            "compilable_inputs_size (average)":0,
            "valid_inputs_size (average)":0,
            "validation_pass_rate (average)": 0,
            "duplicate_inputs_ratio": 0, # (1- unique_inputs/all_generated_inputs)
            "subject_size (generated with compilable Sinput)": 0,
            "subject_size (generated with valid Sinput)": 0,
            "valid_Sinput_size (average)":0,
        },
        "meta_list":{
            "subject_with_compilable_inputs":[],
            "subject_with_valid_inputs":[],
            "subject_w/o_valid_inputs":[],
            "subject_compilableORvalid_inputs_size":{},
            # "subject_and_its_compilable_inputs":{},
            # "subject_and_its_valid_inputs":{},
            "subject_with_compilable_Sinput":[],
            "subject_with_valid_Sinput":[],
            "subject_w/o_valid_Sinput":[],
            "subject_compilableORvalid_Sinput_size":{}
        }
    }

    all_subject = {}
    for index_of_request in range(Setting["number_of_request"]):
        print(f"index_of_request {index_of_request}")
        # hx = f"{HARDCODED_CLASS_SUFFIX}{index_of_request}"
        cache_dir_name_for_this_setting = inputGenerator.get_cache_dir(index_of_request, Setting)
        cache_dir_for_this_setting = f"{ITRANS_CACHE_GENERATED_INPUTS_DIR}{cache_dir_name_for_this_setting}/"
        evaluation_result_of_generated_inputs_function_path = f"{cache_dir_for_this_setting}evaluation_generated_inputs.json"
        # result on single request
        result_single = []
        if file_processing.pathExist(evaluation_result_of_generated_inputs_function_path):
            print( f"evaluation_result_of_generated_inputs_function_path: {evaluation_result_of_generated_inputs_function_path}" )
            result_single = json_processing.read(evaluation_result_of_generated_inputs_function_path)

        for MTC_result in result_single:
            FQS_testMethos = MTC_result["MTC_item"]["FQS_testMethos"]
            # if "org.threeten.extra.TestYearHalf.test_parse_CharSequenceDateTimeFormatter()" in FQS_testMethos and index_of_request==9: 
            #     pass # for debugging
            # if "org.datagear.util.version.VersionTest.isHigherThanTest" not in FQS_testMethos: continue # for debugging
            for generated_input_class in MTC_result["pair_inputs"]:
                generated_input_class_name = generated_input_class.split(".")[-1]
                generated_input_class_item = MTC_result["pair_inputs"][generated_input_class]
                generated_inputs_compilation_result = generated_input_class_item["generated_inputs_compilation_result"]
                generated_inputs_validation_result = generated_input_class_item["generated_inputs_validation_result"]

                generated_Sinput_compilation_result = generated_input_class_item["generated_Sinput_compilation_result"]
                generated_Sinput_validation_result = generated_input_class_item["generated_Sinput_validation_result"]
        
                if FQS_testMethos not in all_subject:
                    if subject_list and FQS_testMethos not in subject_list: continue
                    all_subject[FQS_testMethos] = {
                        "unique_inputs_size":0,"valid_inputs_size":0, "compilable_inputs_size":0,
                        "non_valid_compilable_inputs": [],
                        "unique_inputs":[], "valid_inputs":[], "compilable_inputs":[], "valid_inputs_info":{},
                        "valid_Sinput_size":0, "compilable_Sinput_size":0, "non_valid_compilable_Sinput": [], "non_compilable_Sinput": [], "valid_inputs_but_invalid_Sinput":[],
                        "valid_Sinput":[], "compilable_Sinput":[], "valid_Sinput_info":{}
                    }

                # duplicate input filtering
                if not generated_input_class_name in duplicate_inputs_checking_results[FQS_testMethos]["unique_generated_inputs_class"]: continue
                all_subject[FQS_testMethos]["unique_inputs_size"] += 1
                all_subject[FQS_testMethos]["unique_inputs"].append( generated_input_class_name )

                # MTC_hx_path = ""
                if generated_inputs_compilation_result:
                    evaluation_result["meta_list"]["subject_with_compilable_inputs"].append(FQS_testMethos)
                    all_subject[FQS_testMethos]["compilable_inputs_size"] += 1  
                    all_subject[FQS_testMethos]["compilable_inputs"].append( generated_input_class_name )
                if generated_inputs_compilation_result and not generated_inputs_validation_result:
                    all_subject[FQS_testMethos]["non_valid_compilable_inputs"].append( generated_input_class_name )

                if generated_Sinput_compilation_result:
                    evaluation_result["meta_list"]["subject_with_compilable_Sinput"].append(FQS_testMethos)
                    all_subject[FQS_testMethos]["compilable_Sinput_size"] += 1
                    all_subject[FQS_testMethos]["compilable_Sinput"].append( generated_input_class_name )
                if generated_Sinput_validation_result:
                    evaluation_result["meta_list"]["subject_with_valid_Sinput"].append(FQS_testMethos)
                    all_subject[FQS_testMethos]["valid_Sinput_size"] += 1
                    all_subject[FQS_testMethos]["valid_Sinput"].append( generated_input_class_name )
                    all_subject[FQS_testMethos]["valid_Sinput_info"][generated_input_class_name] = duplicate_inputs_checking_results[FQS_testMethos]["generated_inputs_class_info"][generated_input_class_name]
                if generated_Sinput_compilation_result and not generated_Sinput_validation_result:
                    all_subject[FQS_testMethos]["non_valid_compilable_Sinput"].append( generated_input_class_name )
                if not generated_Sinput_validation_result:
                    all_subject[FQS_testMethos]["non_compilable_Sinput"].append( generated_input_class_name )
                if generated_inputs_validation_result and not generated_Sinput_validation_result:
                    all_subject[FQS_testMethos]["valid_inputs_but_invalid_Sinput"].append( generated_input_class_name )

                # if generated_Sinput_validation_result:
                if generated_Sinput_validation_result and generated_inputs_validation_result: # condition: when give valid Sinput
                    evaluation_result["meta_list"]["subject_with_valid_inputs"].append(FQS_testMethos)
                    all_subject[FQS_testMethos]["valid_inputs_size"] += 1
                    all_subject[FQS_testMethos]["valid_inputs"].append( generated_input_class_name )
                    all_subject[FQS_testMethos]["valid_inputs_info"][generated_input_class_name] = duplicate_inputs_checking_results[FQS_testMethos]["generated_inputs_class_info"][generated_input_class_name]

    # summary
    evaluation_result["meta_list"]["subject_with_compilable_inputs"] = list(set(evaluation_result["meta_list"]["subject_with_compilable_inputs"]))
    evaluation_result["meta_list"]["subject_with_valid_inputs"] = list(set(evaluation_result["meta_list"]["subject_with_valid_inputs"]))
    for FQS_testMethos in all_subject:
        evaluation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos] = all_subject[FQS_testMethos]
        if FQS_testMethos not in evaluation_result["meta_list"]["subject_with_valid_inputs"]:
            evaluation_result["meta_list"]["subject_w/o_valid_inputs"].append(FQS_testMethos)
    evaluation_result["summary"]["all_subject"] = len( all_subject )
    evaluation_result["summary"]["subject_size (generated with compilable inputs)"] = len( evaluation_result["meta_list"]["subject_with_compilable_inputs"] )
    evaluation_result["summary"]["subject_size (generated with valid inputs)"] = len( evaluation_result["meta_list"]["subject_with_valid_inputs"] )
    if len(evaluation_result["meta_list"]["subject_with_compilable_inputs"])>0:
        evaluation_result["summary"]["compilable_inputs_size (average)"] = sum([all_subject[FQS_testMethos]["compilable_inputs_size"] for FQS_testMethos in all_subject])/len(evaluation_result["meta_list"]["subject_with_compilable_inputs"])
    if len(evaluation_result["meta_list"]["subject_with_valid_inputs"])>0:
        evaluation_result["summary"]["valid_inputs_size (average)"] = sum([all_subject[FQS_testMethos]["valid_inputs_size"] for FQS_testMethos in all_subject])/len( evaluation_result["meta_list"]["subject_with_valid_inputs"])
    # summary for Sinput
    evaluation_result["meta_list"]["subject_with_compilable_Sinput"] = list(set(evaluation_result["meta_list"]["subject_with_compilable_Sinput"]))
    evaluation_result["meta_list"]["subject_with_valid_Sinput"] = list(set(evaluation_result["meta_list"]["subject_with_valid_Sinput"]))
    non_valid_compilable_Sinput_dict = {}# for debug
    non_compilable_Sinput_dict = {}# for debug
    valid_inputs_but_invalid_Sinput = {} # for debug
    for FQS_testMethos in all_subject:
        evaluation_result["meta_list"]["subject_compilableORvalid_Sinput_size"][FQS_testMethos] = all_subject[FQS_testMethos]
        if FQS_testMethos not in evaluation_result["meta_list"]["subject_with_valid_Sinput"]:
            evaluation_result["meta_list"]["subject_w/o_valid_Sinput"].append(FQS_testMethos)
        if len( all_subject[FQS_testMethos]["non_valid_compilable_Sinput"])>0:
            non_valid_compilable_Sinput_dict[FQS_testMethos] = all_subject[FQS_testMethos]["non_valid_compilable_Sinput"]
        if all_subject[FQS_testMethos]["compilable_Sinput_size"] ==0:
            non_compilable_Sinput_dict[FQS_testMethos] = all_subject[FQS_testMethos]["non_compilable_Sinput"]
        if len(all_subject[FQS_testMethos]["valid_inputs_but_invalid_Sinput"])>0:
            valid_inputs_but_invalid_Sinput[FQS_testMethos] = all_subject[FQS_testMethos]["valid_inputs_but_invalid_Sinput"]
    evaluation_result["meta_list"]["subjects_w/_non_valid_compilable_Sinput_dict"] = non_valid_compilable_Sinput_dict
    evaluation_result["meta_list"]["subjects_w/o_compilable_Sinput"] = list(non_compilable_Sinput_dict.keys())
    evaluation_result["meta_list"]["subjects_valid_inputs_but_invalid_Sinput"] = list(valid_inputs_but_invalid_Sinput.keys())

    evaluation_result["summary"]["subject_size (generated with compilable Sinput)"] = len( evaluation_result["meta_list"]["subject_with_compilable_Sinput"] )
    evaluation_result["summary"]["subject_size (generated with valid Sinput)"] = len( evaluation_result["meta_list"]["subject_with_valid_Sinput"] )
    if len(evaluation_result["meta_list"]["subject_with_compilable_Sinput"])>0:
        evaluation_result["summary"]["compilable_Sinput_size (average)"] = sum([all_subject[FQS_testMethos]["compilable_Sinput_size"] for FQS_testMethos in all_subject])/len(evaluation_result["meta_list"]["subject_with_compilable_Sinput"])
    if len(evaluation_result["meta_list"]["subject_with_valid_Sinput"])>0:
        evaluation_result["summary"]["valid_Sinput_size (average)"] = sum([all_subject[FQS_testMethos]["valid_Sinput_size"] for FQS_testMethos in all_subject])/len( evaluation_result["meta_list"]["subject_with_valid_Sinput"])
    # diff
    evaluation_result["meta_list"]["subject_with_compiable_inputs_but_no_compilable_Sinput"] = list( set(evaluation_result["meta_list"]["subject_with_compilable_inputs"]) - set(evaluation_result["meta_list"]["subject_with_compilable_Sinput"]) )

    # duplicate_inputs_ratio
    all_generated_inputs = 0
    all_unique_inputs = 0
    for FQS_testMethos in duplicate_inputs_checking_results:
        all_generated_inputs += len(duplicate_inputs_checking_results[FQS_testMethos]["generated_inputs_class"])
        all_unique_inputs += len(duplicate_inputs_checking_results[FQS_testMethos]["unique_generated_inputs_class"])
    evaluation_result["summary"]["duplicate_inputs_ratio"] = f"{1- all_unique_inputs/all_generated_inputs} ({all_generated_inputs - all_unique_inputs}/{all_generated_inputs})"

    distinct_input_size = sum([all_subject[FQS_testMethos]["unique_inputs_size"] for FQS_testMethos in all_subject])
    valid_input_size = sum([all_subject[FQS_testMethos]["valid_inputs_size"] for FQS_testMethos in all_subject])
    rate = valid_input_size/all_generated_inputs
    evaluation_result["summary"]["validation_pass_rate (average)"] = f"{rate} ({valid_input_size}/{all_generated_inputs})"

    valid_Sinput_size = sum([all_subject[FQS_testMethos]["valid_Sinput_size"] for FQS_testMethos in all_subject])
    # print("all_generated_inputs: ", all_generated_inputs , "distinct_input_size: ", distinct_input_size, "all_unique_inputs: ", all_unique_inputs)
    # summary_v2, 方便预览
    evaluation_result["summary_v2"]["generated_input_pairs"] = all_generated_inputs
    evaluation_result["summary_v2"]["generated_distinct_input_pairs"] = distinct_input_size
    evaluation_result["summary_v2"]["generated_distinct_valid_input_pairs"] = valid_input_size
    evaluation_result["summary_v2"]["success_rate (distinct_valid_input_pairs)"] = f"{valid_input_size/all_generated_inputs} ({valid_input_size}/{all_generated_inputs})" 
    evaluation_result["summary_v2"]["generated_distinct_valid_Sinput"] = valid_Sinput_size
    evaluation_result["summary_v2"]["success_rate (distince_valid_Sinput)"] = f"{valid_Sinput_size/all_generated_inputs} ({valid_Sinput_size}/{all_generated_inputs})" 
    if valid_Sinput_size==0:
        evaluation_result["summary_v2"]["success_rate (valid FUinput, when given valid Sinput)"] =  f"({valid_input_size}/0)" 
    else:
        evaluation_result["summary_v2"]["success_rate (valid FUinput, when given valid Sinput)"] =  f"{valid_input_size/valid_Sinput_size} ({valid_input_size}/{valid_Sinput_size})" 

    # "success_rate (valid FUinput, when given valid Sinput )"

    evaluation_result["summary_v2"]["all_subject"] = len( all_subject )
    evaluation_result["summary_v2"]["subjects with distinct valid input pairs"] = len( evaluation_result["meta_list"]["subject_with_valid_inputs"] )
    evaluation_result["summary_v2"]["distinct valid input pairs (average)"] = evaluation_result["summary"]["valid_inputs_size (average)"]
    evaluation_result["summary_v2"]["subjects with distinct valid Sinput"] = len( evaluation_result["meta_list"]["subject_with_valid_Sinput"] )
    evaluation_result["summary_v2"]["distinct valid Sinput (average)"] = evaluation_result["summary"]["valid_Sinput_size (average)"]

    if result_path:
        json_processing.write( json_content=evaluation_result, path=result_path)
    return evaluation_result


def main_task(task):
    index_of_request = task["index_of_request"]
    MTC_item = task["MTC_item"]
    print(f"Processing, index_of_request: {index_of_request}, MTC_item: {MTC_item['FQS_testMethos']}")
        
    input_generator = inputGenerator(index_of_request, MTC_item)
    if input_generator.strategy == 1:
        input_generator.input_type_to_generate = "Pair"
        generate_prompt_from_profile(input_generator)
        generate_Inputs_by_prompting(input_generator)
    elif input_generator.strategy == 2:
        input_generator.input_type_to_generate = "Source"
        generate_prompt_from_profile(input_generator)
        generate_Inputs_by_prompting(input_generator)
        input_generator.input_type_to_generate = "Followup"
        generate_prompt_from_profile(input_generator) # MAKR: stop here: extract generated inputs (follow the same operation of validation/post-processing.)
        generate_Inputs_by_prompting(input_generator)

    print('+++ START: validate_generated_Inputs ', index_of_request, MTC_item["FQS_testMethos"])
    validate_generated_Inputs(input_generator, skipCompileIfExist=Setting["skipCompileIfExist"])
    print('+++ START: construct_test4ITrans_from_generated_inputs ', index_of_request, MTC_item["FQS_testMethos"])
    construct_test4ITrans_from_generated_inputs(input_generator, skipCompileIfExist=Setting["skipCompileIfExist"])
    

def parallel():
    parallel_size = Setting["parallel_size"]
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    tasks = []
    for index_of_request in range(Setting["number_of_request"]):
        for MTC_item in all_GT_MTCs:
            if "skip" in MTC_item and MTC_item["skip"] == True: continue
            # if MTC_item["FQS_testMethos"] not in special_rerun: continue # for debug
            tasks.append({"index_of_request": index_of_request, "MTC_item": MTC_item})

    with multiprocessing.Pool(processes=parallel_size) as pool:
        # Use pool.imap or pool.map for ordered results
        validation_result_of_generated_inputs = pool.map(main_task, tasks)
    

# special_rerun = ['cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupportTest.testGetPlugin()', 'com.alibaba.druid.bvt.sql.mysql.issues.Issue5686.test_column_comment()', 'com.dslplatform.json.DateTest.localTimeBoundary()', 'com.thealgorithms.datastructures.crdt.ORSetTest.testCompareDifferentSets()', 'io.arex.inst.runtime.serializer.SerializerTest.testNestedList()', 'org.apache.druid.msq.exec.WorkerStorageParametersTest.test_WorkerStorageParameter_createInstance()', 'org.ethereum.rpc.FilterTest.testGetNewEvents()', 'org.ojalgo.data.transform.DiscreteFourierTransformTest.testShiftAndRevertEven()', 'org.threeten.extra.TestYearHalf.test_of_int_int()', 'org.threeten.extra.TestYearHalf.test_parse_CharSequenceDateTimeFormatter()']
special_rerun = ['cn.hippo4j.core.executor.plugin.manager.ThreadPoolPluginSupportTest.testGetPlugin()', 'com.alibaba.druid.bvt.sql.mysql.issues.Issue5686.test_column_comment()', 'com.dslplatform.json.DateTest.localTimeBoundary()', 'org.apache.druid.msq.exec.WorkerStorageParametersTest.test_WorkerStorageParameter_createInstance()', 'org.ethereum.rpc.FilterTest.testGetNewEvents()', 'org.threeten.extra.TestYearHalf.test_parse_CharSequenceDateTimeFormatter()']


def collect_all_valid_Sinput():
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    inputs_evaluation_result_path = "  TODO/workProjects/InputTrans/output/inputs/_0603/validation_generated_Inputs_Ti5-1_Shot0_R10_Temprature0.2_CodeQwen1.5-7B-Chat_Stra2.json"
    inputs_evaluation_result = json_processing.read(inputs_evaluation_result_path)
    all_valid_Sinput = {}

    for FQS_testMethos in inputs_evaluation_result["meta_list"]["subject_compilableORvalid_Sinput_size"]:

        sourceInputs_TypeAndVariable =[]
        for MTC_item in all_GT_MTCs:       
            if FQS_testMethos not in MTC_item["FQS_testMethos"]: continue
            """ get: sourceInputs and followUpInputs  """
            sourceInputsContent = MTC_item["sourceInput"]
            followUpInputsContent = MTC_item["followUpInput"]
            sourceInputs = [];
            followUpInputs = []; 
            # countInputs = 1
            for sourceinput in sourceInputsContent:
                sourceInputs.append( f"`{sourceinput['expression']}`" )
                sourceInputs_TypeAndVariable.append( f"{sourceinput['type']} {sourceinput['expression']}" )

        # total reuslt
        valid_Sinput_info = inputs_evaluation_result["meta_list"]["subject_compilableORvalid_Sinput_size"][FQS_testMethos]["valid_Sinput_info"]

        # individual result
        for valid_inputs_test_name in valid_Sinput_info:
            valid_inputs_info = valid_Sinput_info[valid_inputs_test_name]
            path = valid_inputs_info["path"]
            FQN = valid_inputs_info["FQN"]

            # void zonedDateTimeBoundary_h0Test0()
            # test_file_content = file_processing.read_TXTfile(path)

            folder = path.split("/generated_inputs/")[0]
            generated_input_each_index_path = f"{folder}/generated_inputs.json"
            generated_input_each_index = json_processing.read(generated_input_each_index_path)
            input_pairs_code_list = generated_input_each_index[FQS_testMethos]["processed_generated"][FQN]
            input_pairs_code_block = "\n".join(input_pairs_code_list)
            Sinput_code_block = extract_code.variableDefExtractor(input_pairs_code_block, sourceInputs_TypeAndVariable).extract_variable_def_code()

            item = {
                "test_inputs_FQN": FQN,
                "input_pairs_code_block": input_pairs_code_block,
                "Sinput_code_block": Sinput_code_block
            }
            # write
            if FQS_testMethos not in all_valid_Sinput:
                all_valid_Sinput[FQS_testMethos] = [item]
            else:
                all_valid_Sinput[FQS_testMethos].append(item)
    count = 0
    for FQS_testMethos in all_valid_Sinput:
        count += len(all_valid_Sinput[FQS_testMethos])
    print("count: ", count)
    json_processing.write( json_content=all_valid_Sinput, path="all_valid_Sinput.json")


def one_by_one(FQS_testMethos=None):
    count = 0 
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    for index_of_request in range(Setting["number_of_request"]):
        for MTC_item in all_GT_MTCs:
            if FQS_testMethos and FQS_testMethos not in MTC_item["FQS_testMethos"]: continue
            index_of_this_MTC = all_GT_MTCs.index(MTC_item)
            print( f"Processing: {index_of_request}, {index_of_this_MTC}/{len(all_GT_MTCs)}, {MTC_item['FQS_testMethos']}")
            
            input_generator = inputGenerator(index_of_request, MTC_item)
            if input_generator.strategy == 1:
                input_generator.input_type_to_generate = "Pair"
                generate_prompt_from_profile(input_generator)
                generate_Inputs_by_prompting(input_generator)
            elif input_generator.strategy == 2:
                input_generator.input_type_to_generate = "Source"
                generate_prompt_from_profile(input_generator)
                generate_Inputs_by_prompting(input_generator)
                input_generator.input_type_to_generate = "Followup"
                generate_prompt_from_profile(input_generator)
                generate_Inputs_by_prompting(input_generator)

            print('+++ START: validate_generated_Inputs ', index_of_request, MTC_item["FQS_testMethos"])
            validate_generated_Inputs(input_generator, skipCompileIfExist=Setting["skipCompileIfExist"])
            print('+++ START: construct_test4ITrans_from_generated_inputs ', index_of_request, MTC_item["FQS_testMethos"])
            construct_test4ITrans_from_generated_inputs(input_generator, skipCompileIfExist=Setting["skipCompileIfExist"])
            


    # result_collect(Setting, result_path=all_evaluation_result_of_generated_inputs_function_path)
    


def generate_inputs_for_one(MTC_item, Setting=None, just_collect_result=True):
    parallel_size = Setting["parallel_size"]
    if MTC_item:
        FQS_testMethos = MTC_item["FQS_testMethos"]

    if not just_collect_result:
        tasks = []
        for index_of_request in range(Setting["number_of_request"]):
            tasks.append({"index_of_request": index_of_request, "MTC_item": MTC_item})
        with multiprocessing.Pool(processes=parallel_size) as pool:
            # Use pool.imap or pool.map for ordered results
            validation_result_of_generated_inputs = pool.map(main_task, tasks)
    input_generation_result = result_collect(Setting, subject_list=[FQS_testMethos])
    return input_generation_result

def test_generate_inputs_for_one():
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    for MTC_item in all_GT_MTCs:
        if "skip" in MTC_item and MTC_item["skip"] == True: continue
        print('Processing: ', MTC_item["FQS_testMethos"])
        generate_inputs_for_one(MTC_item, Setting)
        break


if __name__ == "__main__":
    # FQS_testMethos = "org.datagear.util.version.VersionTest.stringOfTest()"
    # one_by_one(FQS_testMethos)

    one_by_one()