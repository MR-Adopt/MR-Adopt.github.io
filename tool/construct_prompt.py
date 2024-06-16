"""
"""
import multiprocessing
import os, sys
import time
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing, java_parser, java_file_processing
import extract_code

import config
from codebleu import calc_codebleu
import re, datetime

inputTrans_poj_dir = config.ROOT_DIR
GT_ITrans_w_dir = config.GT_ITRANS_W_DIR
GT_ITrans_wo_dir = config.GT_ITRANS_WO_DIR
benchmark_src_dir = config.BENCHMARK_SRC_DIR

GT_CLASS_SUFFIX = config.GT_CLASS_SUFFIX
HARDCODED_CLASS_SUFFIX = config.HARDCODED_CLASS_SUFFIX
VALID_INPUT_CLASS_SUFFIX = config.VALID_INPUT_CLASS_SUFFIX
FEW_SHOT_BASE_DIR = config.FEW_SHOT_BASE_DIR



Profile_GT_MTCs_wo_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_wo_IT/profile.json"
Profile_GT_MTCs_w_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_w_IT/profile.json"
Profile_GT_MTCs_wo_IT = json_processing.read(Profile_GT_MTCs_wo_IT_path)
Profile_GT_MTCs_w_IT = json_processing.read(Profile_GT_MTCs_w_IT_path)
raw_dir = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_w_IT/raw/"

# Trans generation templates
Template5_1_path = f"{inputTrans_poj_dir}/../prompts/Template_2GenerateInputTransformation.md"

Template5_1 = file_processing.read_TXTfile(Template5_1_path)
Templates = {
            "5-1": Template5_1
             } 

# Input generation templates

for symbol in ["5-1S","5-1F"]:
    if "S" in symbol:
        Ginput_template_path = f"{inputTrans_poj_dir}/../prompts/Template_0GenerateSourceInputs.md"
    elif "F" in symbol:
        Ginput_template_path = f"{inputTrans_poj_dir}/../prompts/Template_1GenerateFollowUpInputs.md"
    Ginput_template = file_processing.read_TXTfile(Ginput_template_path)
    Templates[f"i{symbol}"] = Ginput_template

# print("LOG: Templates: ", Templates)

blocks_of_new_Sinput = "\
## New source inputN:\n\
```java\n\
<CODE TO CONSTRUCT SOURCE INPUT>\n\
```\n\
"

blocks_of_new_input_pair = "\
## Input pairN:\n\
```java\n\
<CODE TO CONSTRUCT INPUT PAIR>\n\
```\n\
"

def pre_process_MTC(code_of_testCase, MTC_item):
    updated_code_of_testCase_lines = []
    """ delete noisy assertions """
    assertionSTMT = MTC_item["assertionSTMT"]
    # 识别出真实的assertionSTMT
    if not assertionSTMT in code_of_testCase: # assertionSTMT 忽略了“message” augment
        assertionSTMT_core = assertionSTMT.split("(")[-1].split(")")[0]
        assertionSTMT = assertionSTMT_core

    # delete other assertions
    for line in code_of_testCase.split("\n"):
        # remove whitespace from the beginning and end
        if line.strip().lower().startswith("assert"):
            if assertionSTMT in line: 
                updated_code_of_testCase_lines.append(line) 
        else:
            updated_code_of_testCase_lines.append(line)
    updated_code_of_testCase = ("\n").join(updated_code_of_testCase_lines)
    return updated_code_of_testCase


def get_pre_processed_MTC_h_code(MTC_item):
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    method_name_hardcoded = f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}"
    original_MTC_simple_name = f"{test_simple_name}"

    # updated test file path
    # test_file_name = test_file_path.split("/")[-1]
    # test_file_path = f"{raw_dir}/{test_file_name}_ITrans" # mark
    ITrans_test_file_path = test_file_path.replace(".java_ITrans",".java").replace(".java",".java_ITrans")
    # TODO: refer to central/local poj raw folder.  
    print("LOG: file_path: ", ITrans_test_file_path)
    code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}", function="getMethod") #  function="getMethodAndRelatedFields" getMethod
    if "empty()" in code_of_testCase:
        code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}", function="getMethod") #  function="getMethodAndRelatedFields" getMethod
    code_of_testCase = code_of_testCase.replace("\n\n", "\n");
    # code_of_testCase = code_of_testCase.replace(method_name_hardcoded, f"{MTChxName}");
    code_of_testCase = code_of_testCase.replace(method_name_hardcoded, f"{original_MTC_simple_name}");
    # print( "code_of_testCase (before pre-process): ", code_of_testCase )
    code_of_testCase = pre_process_MTC(code_of_testCase, MTC_item)
    # print( "code_of_testCase (after pre-process): ", code_of_testCase )
    pre_processed_MTC_h_code = code_of_testCase

    return code_of_testCase


def generate_prompt_from_profile(input_generator, task_type="input_generation"):
    """
        task_type="input_generation" / "trans_generation"
    """
    # prepare
    MTC_item = input_generator.MTC_item
    Crafted_prompts_dir = input_generator.Crafted_prompts_dir
    prompt = input_generator.prompt_template
    number_of_candidate_per_request = "five"  # by default
    if "number_of_candidate" in input_generator.Setting: number_of_candidate_per_request = input_generator.Setting["number_of_candidate"]
    index_of_request = input_generator.index_of_request

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"LOG: START, generate_prompt_from_profile: {MTC_item['FQS_testMethos']}")
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    test_file_path = MTC_item["test_file_path"]
    # updated test file path
    # test_file_name = test_file_path.split("/")[-1]
    # test_file_path = f"{raw_dir}/{test_file_name}_ITrans" # mark
    # print(f"LOG: test_file_path: {test_file_path}")
    test_simple_name = MTC_item["test_simple_name"]
    FQN_of_CUT = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]

    

    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    poj_name = MTC_item["poj_name"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
    invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]
    FQS_testMethos = MTC_item["FQS_testMethos"]
    if f"{invoked_package_FQN}." not in FQS_testMethos: # 说明：invoked_package_FQN 识别有误
        test_file_path = MTC_item["test_file_path"]
        # updated test file path
        # test_file_name = test_file_path.split("/")[-1]
        # test_file_path = f"{raw_dir}/{test_file_name}_ITrans" # mark
        # print(f"LOG: test_file_path: {test_file_path}")
        test_file = file_processing.read_TXTfile(test_file_path)
        package_line = test_file.split("\n")[:0]
        for line in test_file.split("\n"):
            if line.startswith("package "): package_line = line; break
            if line.strip().startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip()
    
    test_file = file_processing.read_TXTfile(test_file_path)
    package_line = test_file.split("\n")[0]
    for line in test_file.split("\n"):
        if line.startswith("package "): package_line = line; break
        if line.strip().startswith("package "): package_line = line; break
    print(f"LOG: test_file_path: {test_file_path}", f"LOG: invoked_package_FQN: {invoked_package_FQN}")
    invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦

    input_generator.invoked_package_FQN = invoked_package_FQN



    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
    class_name = processed_crafted_GT_MTC_test_class_name
    MTChClass = f"{class_name}{HARDCODED_CLASS_SUFFIX}{index_of_request}Test"
    original_MTC_simple_name = f"{test_simple_name}"
    method_name_hardcoded = f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}"
    MTChxName = f"{method_name_hardcoded}{index_of_request}" # -> MTChxName f"{method_name_hardcoded}{index_of_request}Test{index_of_candidate}"?
    """ get the system message """
    system_message = ""
    flag_is_system_message = False
    for line in prompt.split("\n"):
        if "<SYSTEM MESSAGE: END>" in line:
            flag_is_system_message = False
        if flag_is_system_message:
            system_message += line + "\n"
        if "<SYSTEM MESSAGE: START>" in line:
            flag_is_system_message = True

    """ get: code_of_MTC_h """
    poj_ITRANS_MTCIT_DIR = config.ITRANS_MTCIT_DIR % poj_name
    MTC_h_only_test_class_name = f"{class_name}{HARDCODED_CLASS_SUFFIX}Test"
    MTC_h_only_test_file_path = f"{poj_ITRANS_MTCIT_DIR}{invoked_package_FQN.replace('.','/')}/{MTC_h_only_test_class_name}.java"
    input_generator.MTC_h_only_test_file_path = MTC_h_only_test_file_path

    # test_file_path -> .java_ITrans
    """ get: code_of_MTC_h """
    # updated test file path
    # test_file_name = test_file_path.split("/")[-1]
    # test_file_path = f"{raw_dir}/{test_file_name}_ITrans" # mark
    ITrans_test_file_path = test_file_path.replace(".java_ITrans",".java").replace(".java",".java_ITrans")

    # TODO, 用method: get_pre_processed_MTC_h_code(MTC_item)
    # ITrans_test_file_path = test_file_path.replace(".java",".java_ITrans")
    # TODO: refer to central/local poj raw folder.  
    code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}", function="getMethod") #  function="getMethodAndRelatedFields" getMethod
    if "empty()" in code_of_testCase:
        code_of_testCase = java_parser.get_method_body_or_related_class_field(file_path=ITrans_test_file_path, method_name=f"{test_simple_name}", function="getMethod") #  function="getMethodAndRelatedFields" getMethod
    code_of_testCase = code_of_testCase.replace("\n\n", "\n");
    # code_of_testCase = code_of_testCase.replace(method_name_hardcoded, f"{MTChxName}");
    code_of_testCase = code_of_testCase.replace(method_name_hardcoded, f"{original_MTC_simple_name}");
    # print( "code_of_testCase (before pre-process): ", code_of_testCase )
    code_of_testCase = pre_process_MTC(code_of_testCase, MTC_item)
    # print( "code_of_testCase (after pre-process): ", code_of_testCase )
    input_generator.pre_processed_MTC_h_code = code_of_testCase

    """ get: testName """
    testName = f"`{test_simple_name}`"

    """ get: methodInvs """
    s_methodInvs_list = []
    f_methodInvs_list = []
    methodInvs = ""

    """ get: sourceInputsTypeName and  followUpInputsTypeName"""
    sourceInputs_TypeAndVariable = []
    followUpInputs_TypeAndVariable = []
    sourceInputsTypeName = ""
    followUpInputsTypeName = ""

    """ get: sourceInputs and followUpInputs  """
    sourceInputsContent = MTC_item["sourceInput"]
    followUpInputsContent = MTC_item["followUpInput"]
    sourceInputs = [];
    followUpInputs = []; 
    # countInputs = 1
    for sourceinput in sourceInputsContent:
        sourceInputs.append( f"`{sourceinput['expression']}`" )
        sourceInputs_TypeAndVariable.append( f"{sourceinput['type']} {sourceinput['expression']}" )
        if {sourceinput['invocation']} not in s_methodInvs_list: s_methodInvs_list.append(f"`{sourceinput['invocation']}`")
    for followUpInput in followUpInputsContent:
        followUpInputs.append( f"`{followUpInput['expression']}`" )
        followUpInputs_TypeAndVariable.append( f"{followUpInput['type']} {followUpInput['expression']}" )
        if {followUpInput['invocation']} not in f_methodInvs_list: f_methodInvs_list.append(f"`{followUpInput['invocation']}`")
    methodInvs = (",").join(s_methodInvs_list) + " and " + (",").join(f_methodInvs_list)
    sourceInputsTypeName = (",").join([ f"`{ele}`" for ele in sourceInputs_TypeAndVariable])
    followUpInputsTypeName = (",").join([ f"`{ele}`" for ele in followUpInputs_TypeAndVariable])

    """ get: assertSTMT """
    assertSTMT = MTC_item["assertionSTMT"]
    if assertSTMT not in code_of_testCase:
        for line in code_of_testCase.split("\n"):
            if line.lower().strip().startswith("assert"):
                assertSTMT = line; break

    """ get: inputSTMTs """
    inputSTMTs = extract_code.variableDefExtractor(code_of_testCase, sourceInputs_TypeAndVariable+followUpInputs_TypeAndVariable, input_generator= input_generator).extract_variable_def_code()
    sInputSTMTs = extract_code.variableDefExtractor(code_of_testCase, sourceInputs_TypeAndVariable, input_generator= input_generator).extract_variable_def_code()
    
    """ mask: the construction of source and follow-up inputs """
    """  previous version 20240420
    lines_of_testCase = code_of_testCase.split("\n")
    for line_index in range(len(lines_of_testCase)):
        line = lines_of_testCase[line_index]
        if "= " not in line: continue # not varible declaration line

        for ele in sourceInputs_TypeAndVariable:
            if line.strip().startswith(ele) and line.split("=")[0].strip() == ele: # 有且仅有 ele， 防止是 ele* 这种
                lines_of_testCase[line_index] = line.split("=")[0] + "= \t// TODO: construct the input"
                inputSTMTs += f"{line}\n"
                sInputSTMTs += f"{line}\n"

        for ele in followUpInputs_TypeAndVariable:
            if line.strip().startswith(ele) and line.split("=")[0].strip() == ele: # 有且仅有 ele， 防止是 ele* 这种
                lines_of_testCase[line_index] = line.split("=")[0] + "= \t// TODO: construct the input"
                inputSTMTs += f"{line}\n"
    
    lines_of_testCase = [ f"\t{ele}" for ele in lines_of_testCase]
    testCaseLackInputConstruction = ("\n").join(lines_of_testCase)
    """
    
    """ get: the body of MUT & METHOD CONTEXT """
    # given the poj dir and FQS of the MUT, to get the test file path 
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    poj_name = MTC_item["poj_name"]
    test_file_path = MTC_item["test_file_path"]
    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"

    declarations_of_focal_methods  = []
    skeleton_of_classes = []
    for method_FQS in invoked_methods_FQS:
        method_name = method_FQS.split("(")[0].split(".")[-1]
        # print( f"LOG: poj_dir: {poj_dir}" )
        class_path = java_file_processing.find_class_file_path_by_methodFQS(poj_dir, method_FQS)
        # get the body of MUT
        # print( f"method_name: {method_name}, class_path: {class_path}, poj_dir: {poj_dir} " )
        method_declaration = java_parser.get_method_body_or_related_class_field(file_path=class_path, method_name=method_name, function="getMethod")
        if method_declaration not in declarations_of_focal_methods:
            declarations_of_focal_methods.append(method_declaration)
        """ get: METHOD CONTEXT """
        # 1. the skeleton of CUT
        class_skeleton = java_parser.get_skeleton_of_class(file_path=class_path, function="extractClassSkeleton")
        if class_skeleton not in skeleton_of_classes:
            skeleton_of_classes.append(class_skeleton)
        # 2. the skeleton of classes of input objects,
        inputs_FQN = method_FQS.split("(")[1].split(")")[0]
        for input_FQN in inputs_FQN.split(","):
            if "." not in input_FQN or input_FQN.startswith("java."):  continue # 说明非JDK version
            clear_input_FQN = input_FQN.split("<")[0]
            class_path = java_file_processing.find_class_file_path_by_methodFQS(poj_dir, clear_input_FQN)
            if class_path== None: continue # 说明当前项目下未找到

            class_skeleton = java_parser.get_skeleton_of_class(file_path=class_path, function="extractClassSkeleton")
            if class_skeleton not in skeleton_of_classes:
                skeleton_of_classes.append(class_skeleton)
    

    """ get: new source inputs blocks """
    # input_generator.generated_input_blocks  # raw, code blocks from LLMs' anwsers
    # input_generator.generated_input_blocks_unique
    # input_generator.postprocessed_generated_input_blocks
    # input_generator.postprocessed_generated_input_blocks_unique, use this one
    new_source_input_blocks_list = []
    new_source_input_blocks = ""
    if hasattr(input_generator, 'postprocessed_generated_input_blocks_unique'): # 说明是input generation (not Trans generation)
        for block in input_generator.postprocessed_generated_input_blocks_unique:
            # def_stmts = extract_code.extract_stmts_of_declaring_variables(sourceInputs_TypeAndVariable, block)
            def_stmts =  extract_code.variableDefExtractor(block, sourceInputs_TypeAndVariable, input_generator= input_generator, extract_code_from_MTC=False).extract_variable_def_code()
            block_index = input_generator.postprocessed_generated_input_blocks_unique.index(block)
            new_source_input_block = blocks_of_new_Sinput.replace("## New source inputN", f"## New source input{block_index}")
            new_source_input_block = new_source_input_block.replace("<CODE TO CONSTRUCT SOURCE INPUT>", def_stmts)
            new_source_input_blocks_list.append(new_source_input_block)
    new_source_input_blocks = ("\n").join(new_source_input_blocks_list)


    """ prompt template for Trans generation (only) """
    ITransFunction = ""
    returnFollowUp = ""
    valid_input_pairs_blocks = ""
    if task_type=="trans_generation":
        """ get: signature/skeleton of ITrans function """
        # TODO, refactor: use get_GT_Trans(MTC_item, type="function_header") 
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
        
        """ get:  <OTHER INPUT PAIRS>"""
        # 1. get valid input pairs  (from validation_.json "valid_inputs_info") generate_inputs_for_one(MTC_item, Setting)
        trans_generator = input_generator
        input_generation_result = trans_generator.LLMI_input_generation_result
        # FQS_testMethos = MTC_item["FQS_testMethos"]
        generated_valid_inputs_info = input_generation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos]["valid_inputs_info"] # default 

        valid_input_pairs_list = []
        flag_original_h_extracted = False
        for valid_inputs_className in generated_valid_inputs_info.keys():
            test_class_path = generated_valid_inputs_info[valid_inputs_className]["path"]
            target_class_FQN = generated_valid_inputs_info[valid_inputs_className]["FQN"]
            # 2. get the code statements of the valid input pairs (from /generated_inputs.json)
            # test_class_path's dir
            test_class_path_folder = test_class_path[:test_class_path.rfind("/")]
            this_setting_folder = test_class_path_folder[:test_class_path_folder.rfind("/")]
            generated_inputs_json_path = f"{this_setting_folder}/generated_inputs.json"
            generated_inputs_json = json_processing.read(generated_inputs_json_path)
            
            if not flag_original_h_extracted:
                original_h_stmt_list = generated_inputs_json[FQS_testMethos]["original_h"]
                original_h_stmts = ("\n").join(original_h_stmt_list)
                valid_input_pairs_list.append(original_h_stmts)
                flag_original_h_extracted = True
            
            valid_inputs_stmt_list = generated_inputs_json[FQS_testMethos]["processed_generated"][target_class_FQN]
            valid_inputs_stmts = ("\n").join(valid_inputs_stmt_list)
            valid_input_pairs_list.append(valid_inputs_stmts)
        # 3. format these input pairs
        valid_input_pairs_blocks = ""
        valid_input_pairs_blocks_list = []
        block_index = 0
        for valid_inputs_stmts in valid_input_pairs_list:
            block_index += 1
            valid_input_pairs_block = blocks_of_new_input_pair.replace("## Input pairN", f"## Input pair{block_index}")
            valid_input_pairs_block = valid_input_pairs_block.replace("<CODE TO CONSTRUCT INPUT PAIR>", valid_inputs_stmts)
            valid_input_pairs_blocks_list.append(valid_input_pairs_block)
        valid_input_pairs_blocks = ("\n").join(valid_input_pairs_blocks_list)

    """ replace  """
    prompt = prompt.replace("$FQNofCUT$", f"`{FQN_of_CUT}`")
    prompt = prompt.replace("$codeOfTestCase$", code_of_testCase)
    prompt = prompt.replace("$sourceInputs$", (",").join(sourceInputs))
    prompt = prompt.replace("$followUpInputs$", (",").join(followUpInputs))
    # prompt = prompt.replace("\n\n", "\n");prompt = prompt.replace("\n\n", "\n");prompt = prompt.replace("\n\n", "\n")
    prompt = prompt.replace("$MTChClass$", MTChClass)
    # prompt = prompt.replace("$testCaseLackInputConstruction$", testCaseLackInputConstruction)
    prompt = prompt.replace("$testName$", testName)
    prompt = prompt.replace("$codeOfTestCase$", code_of_testCase)
    prompt = prompt.replace("$sourceInputsTypeName$", sourceInputsTypeName)
    prompt = prompt.replace("$followUpInputsTypeName$", followUpInputsTypeName)
    prompt = prompt.replace("$inputSTMTs$", inputSTMTs.strip("\n"))
    prompt = prompt.replace("$methodInvs$", methodInvs)
    prompt = prompt.replace("$assertSTMT$", f"`{assertSTMT}`")

    # new name
    prompt = prompt.replace("<ORIGINAL TEST CASE>", code_of_testCase)
    prompt = prompt.replace("<FOCAL METHOD>", ("\n").join(declarations_of_focal_methods)) 
    prompt = prompt.replace("<METHOD CONTEXT>", ("\n\n").join(skeleton_of_classes))  
    prompt = prompt.replace("<A PAIR OF TEST INPUTS>", inputSTMTs.strip("\n"))
    prompt = prompt.replace(f"# Task Description\n<SYSTEM MESSAGE: START>\n{system_message}<SYSTEM MESSAGE: END>", "")
    prompt = prompt.replace("<N>", number_of_candidate_per_request)
    prompt = prompt.replace("<CODE TO CONSTRUCT SOURCE INPUT>", sInputSTMTs.strip("\n")) # sInputSTMTs
    prompt = prompt.replace("<NEW SOURCE INPUTS>", new_source_input_blocks) # sInputSTMTs
    

    # for trans only 
    prompt = prompt.replace("<SOURCE INPUT>", (",").join(sourceInputs))
    prompt = prompt.replace("<FOLLOW UP INPUT>", (",").join(followUpInputs))
    prompt = prompt.replace("$ITransClass$", processed_crafted_GT_MTC_test_class_name)
    prompt = prompt.replace("$ITransFunction$", ITransFunction)
    prompt = prompt.replace("$returnTransformedInputs$", returnFollowUp)
    prompt = prompt.replace("<OTHER INPUT PAIRS>", valid_input_pairs_blocks)
    

    # print( f"path: {input_generator.Crafted_prompts_dir}{MTChClass}.md" )
    prompt = prompt.strip("\n")
    if task_type=="trans_generation":
        prompt_path = f"{Crafted_prompts_dir}{processed_crafted_GT_MTC_test_class_name}.md"
        promt_id = processed_crafted_GT_MTC_test_class_name
    else: #  task_type=="input_generation":
        prompt_path = f"{Crafted_prompts_dir}{MTChClass}.md"
        promt_id = MTChClass
    file_processing.write_TXTfile(path = prompt_path, content=prompt)
    system_message_path = prompt_path.replace(".md",".system_message")
    file_processing.write_TXTfile(path = system_message_path, content=system_message)
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f"LOG: END, generate_prompt_from_profile: {MTC_item['FQS_testMethos']}")

    input_generator.MTChClass = MTChClass
    input_generator.MTChMethod = MTChxName
    input_generator.prompt_system_message = system_message
    input_generator.prompt_path = prompt_path
    input_generator.promt_id = promt_id
    input_generator.promt_content = prompt
    input_generator.inputSTMTs = inputSTMTs.strip("\n")

    input_generator.sourceInputs_TypeAndVariable = sourceInputs_TypeAndVariable
    input_generator.followUpInputs_TypeAndVariable = followUpInputs_TypeAndVariable
    
    return input_generator


def generate_few_shot_info(trans_generator):
    # 1. get this MTC
    pre_processed_MTC_h_code_this = get_pre_processed_MTC_h_code(trans_generator.MTC_item)
    FQS_testMethos_this = trans_generator.MTC_item['FQS_testMethos']

    # 2. get all MTCs with GT (w and w/o)
    """ the base to choose few shot """ 
    all_GT_MTCs = Profile_GT_MTCs_wo_IT + Profile_GT_MTCs_w_IT
    pre_processed_MTC_h_code_GTs = {}
    MTC_item_dicts = {} #FQS_testMethos: MTC id
    for MTC_item in all_GT_MTCs:
        if "skip" in MTC_item and MTC_item["skip"] == True: continue
        FQS_testMethos = MTC_item['FQS_testMethos']
        if FQS_testMethos == FQS_testMethos_this: continue # avoid select itself
        
        MTC_item_dicts[FQS_testMethos] = MTC_item
        # get the code of the MTC
        pre_processed_MTC_h_code_GT = get_pre_processed_MTC_h_code(MTC_item)
        pre_processed_MTC_h_code_GTs[FQS_testMethos] = pre_processed_MTC_h_code_GT

    # 3. get top-n CodeBLEU socres
    codebleu_scores = {}
    for FQS_testMethos in pre_processed_MTC_h_code_GTs.keys():
        pre_processed_MTC_h_code_GT = pre_processed_MTC_h_code_GTs[FQS_testMethos]
        # CodeBLEU of: pre_processed_MTC_h_code_this , pre_processed_MTC_h_code_GT
        # codebleu_result = calc_codebleu([pre_processed_MTC_h_code_GT], [pre_processed_MTC_h_code_this], lang="java", weights=(0.25, 0.25, 0.25, 0.25), tokenizer=None)
        codebleu_result = calc_codebleu([pre_processed_MTC_h_code_GT], [pre_processed_MTC_h_code_this], lang="java")
        codebleu_score = codebleu_result["codebleu"]
        codebleu_scores[FQS_testMethos] = codebleu_score
    
    # rank based on socre 
    sorted_MTC_and_CodebleuScores = sorted(codebleu_scores.items(), key=lambda x: x[1], reverse=True) # [('b', 2), ('a', 1)]
    shot_num = trans_generator.Setting["number_of_shot"]
    shot_MTCs = sorted_MTC_and_CodebleuScores[:shot_num]
    
    # get Q and A of each shot MTC
    few_shot_info = [] # [ {Q:.., A:..} , {Q:.., A:..} ]
    for FQS_testMethos, codebleu_score in shot_MTCs:
        MTC_item = MTC_item_dicts[FQS_testMethos]
        # Q: prompt for this MTC
        # trans_generator_item = transGenerator(trans_generator.index_of_request, MTC_item)
        trans_generator_item = type(trans_generator)(trans_generator.index_of_request, MTC_item) # the same as the above constructor
        print(f"LOG: type: {type(trans_generator_item)}, {trans_generator_item.MTC_item['FQS_testMethos']} ")
        trans_generator_item = generate_prompt_from_profile(trans_generator_item, task_type="trans_generation")
        Q = trans_generator_item.promt_content

        # A: the GT ITrans for this MTC
        # trans_class_def = get_GT_Trans(trans_generator_item.MTC_item, type="class_definition")
        # A = f"```java\n{trans_class_def}\n```"
        A_path = f"{FEW_SHOT_BASE_DIR}{FQS_testMethos}".split("(")[0]
        A = file_processing.read_TXTfile(A_path)
        few_shot_info.append({"Q":Q, "A":A})
        print(f"LOG: FQS_testMethos: {FQS_testMethos}")
        print(f"LOG: few_shot_info, Q:")
        print(f"{Q}")
        print(f"LOG: FQS_testMethos: {FQS_testMethos}")
        print(f"LOG: few_shot_info, A:")
        print(f"{A}")
    trans_generator.few_shot_info = few_shot_info

    # for MTC_item in all_GT_MTCs: # for manually construct few shot base
    #     # Q: prompt for this MTC
    #     trans_generator_item = transGenerator(trans_generator.index_of_request, MTC_item)
    #     trans_generator_item = generate_Inputs_with_LLMs.generate_prompt_from_profile(trans_generator_item, task_type="trans_generation")
    #     Q = trans_generator_item.promt_content

    #     # A: the GT ITrans for this MTC
    #     trans_class_def = generate_Inputs_with_LLMs.get_GT_Trans(trans_generator_item.MTC_item, type="class_definition")
    #     A = f"```java\n{trans_class_def}\n```"
    #     FQS_testMethos = MTC_item['FQS_testMethos']
    #     print(f"LOG: FQS_testMethos: {FQS_testMethos}")
    #     print(f"LOG: few_shot_info, Q:")
    #     print(f"{Q}")
    #     print(f"LOG: FQS_testMethos: {FQS_testMethos}")
    #     print(f"LOG: few_shot_info, A:")
    #     print(f"{A}")
    
    # store
    prompt_path = trans_generator.prompt_path
    few_shot_info_path = prompt_path.replace(".md",".few_shot_info.json")
    # print(f"LOG: few_shot_info_path: {few_shot_info_path}")
    json_processing.write(json_content=few_shot_info, path=few_shot_info_path)
    trans_generator.few_shot_info_path = few_shot_info_path

    return trans_generator