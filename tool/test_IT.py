import os, sys
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing, Evosuite_runner_general, java_file_processing, compile_java_poj, java_test
import generate_Inputs_with_LLMs

import GT_processing
import config 

import datetime
import re



maven_benchmark_poj_dir = config.BENCHMARK_DIR
Generated_ES_TEST_DIR = config.ES_GENERATED_TEST_DIR

PATH_JAVA = config.PATH_JAVA_8 
ES_TEST_EXE_RESULT_DIR = config.ES_TEST_EXE_RESULT_DIR
CRAFTED_MTC_IT_TEST_EXE_RESULT_DIR = config.CRAFTED_MTC_IT_TEST_EXE_RESULT_DIR
# should be consistent with that in GT_processing.py
# should move generate_test_cases_evosuite() / generate_test_cases_randoop() to this file
suffix_single_test="_ESTest" # for ES generated test
suffix_merged_tests=""
suffix_diff_test="_DiffTest" # for differential testing

PATH_JAVA = config.PATH_JAVA_11 # 这里在运行 class时，选择 11; 以防有的class是由8编译的 

test_dir_to_place_crafted_MTC_ITrans = GT_processing.test_dir_to_place_crafted_MTC_ITrans

GT_ITrans_wo_dir = config.GT_ITRANS_WO_DIR
GT_ITrans_w_dir = config.GT_ITRANS_W_DIR
GT_CLASS_SUFFIX = config.GT_CLASS_SUFFIX
PACKAGE_STATEMENT = config.PACKAGE_STATEMENT

PATH_EVOSUITE_JAR = config.PATH_EVOSUITE_JAR
PATH_ES_RUNTIME_JAR = config.PATH_ES_RUNTIME_JAR
PATH_JUNIT4_JAR = config.PATH_JUNIT4_JAR

DIR_m2 = config.DIR_MAVEN_M2_REPO_USER_HOME
PATH_ITRANS_COMPILE_INFO = config.PATH_ITRANS_COMPILE_INFO
ITRANS_EVOSUITE_TESTS_DIR = config.ITRANS_EVOSUITE_TESTS_DIR
ITRANS_MTCIT_DIR = config.ITRANS_MTCIT_DIR
ITRANS_GT_DIR = config.ITRANS_GT_DIR
ITRANS_GENERATED_IT_DIR = config.ITRANS_GENERATED_IT_DIR
ITRANS_GENERATED_INPUTS_DIR = config.ITRANS_GENERATED_INPUTS_DIR
ITRANS_GENERATED_LLMI_TEST_DIR = config.ITRANS_GENERATED_LLMI_TEST_DIR

VALID_INPUT_CLASS_SUFFIX = config.VALID_INPUT_CLASS_SUFFIX

""""
class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
all_class_dir_str = (":").join( class_dir_list )
Dir_ClassPath = f"{CLASS_PATHS}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}"
CLASS_PATHS = f"{Generated_ES_TEST_DIR}:{all_class_dir_str}:{CP_jar_path}"
"""


# generate tests for GT ITrans function (in original poj)
def generate_test_cases_in_original_poj(crafted_subject, skip_ESTest_generation=0):   
    """_summary_

    Args:
        crafted_subject (_type_): _description_
        skip_ESTest_generation (int, optional): _description_. Defaults to 0.
            ==1: skip, when merged file exiting
            ==2: skip, when diff file exiting
    """
    MTC_item = crafted_subject.MTC_item
    test_file_path = MTC_item["test_file_path"]
    poj_name = MTC_item["poj_name"]
    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"

    CD_CMD = f"cd {poj_dir}; "
    test_simple_name = MTC_item["test_simple_name"]
    original_MTC_test_file_path = MTC_item["test_file_path"]
    test_class_name = original_MTC_test_file_path.split("/")[-1].replace(".java", "")
    TARGET_CLASS = crafted_subject.IT_GT_only_test_class_FQN # target class
    
    poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
    poj_build_tool = poj_compilation_info["build_tool"][0]
    jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]
    # for run EvoSuite, 因为ES目前只支持到 java 11, https://github.com/EvoSuite/evosuite/issues/433
    PATH_JAVA = compile_java_poj.get_jdk_path(11) 
    # for compile ES generated tests, if jdk >11, may jave issues ...
    PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)

    # poj_name = MTC_item["poj_name"]
    # dependency_jars_list = MTC_item["pom"].split(";")
    # dependency_jars_paths = []
    # for dependency_jar_item in dependency_jars_list:
    #     groupID = dependency_jar_item.split(":")[0]
    #     artifactID = dependency_jar_item.split(":")[1]
    #     version = dependency_jar_item.split(":")[2]
    #     jar_name = f"{artifactID}-{version}.jar"
    #     if len(dependency_jar_item.split(":")) ==4 and "test" in dependency_jar_item.split(":")[3]:
    #         jar_name = f"{artifactID}-{version}-tests.jar"
    #     if len(dependency_jar_item.split(":")) ==4 and "dependencies" in dependency_jar_item.split(":")[3]:
    #         jar_name = f"{artifactID}-{version}-{dependency_jar_item.split(':')[3]}.jar"
    #     jar_path = f"{DIR_m2}/{groupID.replace('.','/')}/{artifactID.replace('.','/')}/{version}/{jar_name}"
    #     dependency_jars_paths.append(jar_path)
    # dependency_all_jars_path = (":").join(dependency_jars_paths)
    
    Generated_ES_TEST_DIR = ITRANS_EVOSUITE_TESTS_DIR % poj_name
    file_processing.creatFolder_recursively_IfExistPass(Generated_ES_TEST_DIR)
    extra_cp = f"{crafted_subject.poj_ITRANS_GT_DIR}:{Generated_ES_TEST_DIR}"

    Path_generatedESTestFile = Generated_ES_TEST_DIR + TARGET_CLASS.replace(".","/") + f"{suffix_single_test}.java"
    if skip_ESTest_generation == 1 and file_processing.pathExist(Path_generatedESTestFile):
        print(f"skip_ESTest_generation == 1 and file_processing.pathExist(Path_generatedESTestFile): {Path_generatedESTestFile}")
        return
    else:
        Evosuite_runner_general.generally_generate_fixed_amountORiteration_test_cases(poj_build_tool=poj_build_tool, test_amount=10086, max_iteration_Evo=10, TASK_POJ_NAMR=poj_name, CMD_CD=CD_CMD, PATH_JAVA=PATH_JAVA, TARGET_CLASS=TARGET_CLASS, CP_jar_path=extra_cp, DIR_POJ=poj_dir, Generated_ES_TEST_DIR=Generated_ES_TEST_DIR, suffix_single_test="_ESTest", suffix_merged_tests="", withoutAssertion=False, overWriteExistingTestFile=False, PATH_JAVAC=PATH_JAVAC)
    """ generate_differential_testing """
    Path_diffESTestFile = generate_differential_testing(TARGET_CLASS,MTC_item)
    # compile 
    Evosuite_runner_general.compile_test_class(poj_build_tool="maven", TASK_POJ_NAMR="poj_name", CMD_CD=f"cd {maven_benchmark_poj_dir};", CP_jar_path=extra_cp, DIR_POJ=maven_benchmark_poj_dir, Generated_ES_TEST_DIR=Generated_ES_TEST_DIR, Path_TestFile_to_compile=Path_diffESTestFile)
    print(f"Path_diffESTestFile: {Path_diffESTestFile}")


def generate_differential_testing(TARGET_CLASS,MTC_item):
    """_summary_
    create differential testing 
        * _ ESTest.java -> _ DiffTest.java 
        * comment other assertion statements; (line by line)
        * import com.dataset.GT.{MTCITrans_class}_ GT;
        * 搜索：invocation的返回值类型
            * Type name =  line.split(f"= {MTCITrans_class}.inputTransformation(")
            * Type name_count += MTCITrans_class.inputTransformation()
            * Type name_count_GT += MTCITrans_class_GT.inputTransformation()
            * assertEquals( output1_GT, name_count )
        * & compile
    """

    diffESTestContent_lines = []

    mergedESTestName =  TARGET_CLASS.replace(".","/") + f"{suffix_single_test}{suffix_merged_tests}"
    diffESTestName = TARGET_CLASS.replace(".","/") + f"{suffix_diff_test}"
    Path_mergedESTestFile = Generated_ES_TEST_DIR + f"{mergedESTestName}.java"
    if not file_processing.pathExist(Path_mergedESTestFile): return
    mergedESTestContent = file_processing.read_TXTfile(Path_mergedESTestFile)
    # class _ ESTest -> class _ DiffTest 
    mergedESTestContent = mergedESTestContent.replace(f"class {mergedESTestName.split('/')[-1]}", f"class {diffESTestName.split('/')[-1]}")
    Path_diffESTestFile = Path_mergedESTestFile.replace(f"{mergedESTestName}.java", f"{diffESTestName}.java")


    TARGET_CLASS_name = TARGET_CLASS.split(".")[-1]
    TARGET_GT_CLASS_name = f"{TARGET_CLASS_name}{GT_CLASS_SUFFIX}"
    ITrans_invocation_str = f"{TARGET_CLASS_name}.inputTransformation(" # no GT_suffix

    # get ITransFunction_return_type
    ITransFunction_return_type = "";
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
    if MTC_item["type"] == "wo_ITrans":
        GT_ITrans_path = f"{GT_ITrans_wo_dir}{processed_crafted_GT_MTC_test_class_name}.java"
    elif MTC_item["type"] == "w_ITrans":
        GT_ITrans_path = f"{GT_ITrans_w_dir}{processed_crafted_GT_MTC_test_class_name}.java"
    GT_ITrans_class = file_processing.read_TXTfile(GT_ITrans_path)
    pattern = r'public static [a-zA-Z0-9_,.?()\[\]<> ]* inputTransformation[a-zA-Z0-9_,.?()\[\]<> ]*{'
    matches = re.findall(pattern, GT_ITrans_class)
    ITransFunction = "public static Object inputTransformation()"
    if len( matches ) ==0:
        print("ERROR: no inputTransformation function in GT ITrans class")
        print( f"GT_ITrans_path: {GT_ITrans_path}" )
    else:
        ITransFunction = matches[0].strip("{")
    ITransFunction_return_type = ITransFunction.split(" ")[2]


    # insert GT_ITrans_invocation and assertEquals( output1_GT, output1 )
    count = 10000
    for line in mergedESTestContent.split("\n"):
        if f"{ITrans_invocation_str}" in line:
            added_GT_ITrans_invocation_line = "";
            added_assertion_invocation_line = "";
            
            if " = " not in line: # without return value
                # updated_line = f" {return_type} IToutputs_{count} = {line}" 
                line = line.replace( line.strip(), f"{ITransFunction_return_type} IToutputs_{count} = {line.strip()}")
                count += 1

            return_value_type_varible_str = line.split(f" = ")[0]
            return_value_type_varible_str = return_value_type_varible_str.strip()

            # output1_GT = MTCITrans_class_GT.inputTransformation()  
            return_value_type_varible_GT_str = f"{return_value_type_varible_str}_GT"
            added_GT_ITrans_invocation_line = line.replace(f"{return_value_type_varible_str}", f"{return_value_type_varible_GT_str}") # return value type and variable name
            added_GT_ITrans_invocation_line = added_GT_ITrans_invocation_line.replace(f"{TARGET_CLASS_name}.inputTransformation(", f"{TARGET_GT_CLASS_name}.inputTransformation(") # method invocation
            
            # assertEquals( output1_GT, output1 )
            return_varible_str = return_value_type_varible_str.split(" ")[-1]
            return_varible_GT_str = return_value_type_varible_GT_str.split(" ")[-1]
            added_assertion_invocation_line = f"assertEquals( {return_varible_GT_str}, {return_varible_str} );"

            updated_line = line 
            diffESTestContent_lines.append(updated_line)
            diffESTestContent_lines.append(added_GT_ITrans_invocation_line)
            diffESTestContent_lines.append(added_assertion_invocation_line)
        elif line.strip().startswith("assert"):
            diffESTestContent_lines.append(f"// {line}")
        else:
            diffESTestContent_lines.append(line)
    diffESTestContent = "\n".join(diffESTestContent_lines)

    # import com.dataset.GT.{MTCITrans_class}_ GT;
    import_GT_Class = f"import com.dataset.GT.{TARGET_GT_CLASS_name};"
    diffESTestContent = diffESTestContent.replace(PACKAGE_STATEMENT,f"{PACKAGE_STATEMENT}\n\n{import_GT_Class}")
    file_processing.write_TXTfile(path=Path_diffESTestFile, content=diffESTestContent)

    return Path_diffESTestFile

# for local poj: inputtrans
def originalMTC_test_IT_pre(MTC_item, GTorGenerated, POJ_DIR=config.BENCHMARK_DIR, EXE_RESULT_DIR = CRAFTED_MTC_IT_TEST_EXE_RESULT_DIR):
    """
    Args:
        MTC_item (_type_): _description_
        GTorGenerated (_type_): "GT" ITrans function or LLM-"Generated" ITrans function
        POJ_DIR (_type_, optional): _description_. Defaults to config.BENCHMARK_DIR.

    Returns:
        _type_: _description_
    """
    # profile
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"

    # run test
    Dir_ClassPath = GT_processing.get_classpath(MTC_item, POJ_DIR)
    #generate_test_cases_evosuite Dir_ClassPath = f".:evosuite-tests:{all_class_dir_str}:{PATH_EVOSUITE_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}"
    FQN_test_class = f"com.dataset.{processed_crafted_GT_MTC_test_class_name}"
    Path_exe_test_log = f"{EXE_RESULT_DIR}{processed_crafted_GT_MTC_test_class_name}_{GTorGenerated}.log"
    file_processing.creatFolder_IfExistPass(EXE_RESULT_DIR)

    CMD_CD = f"cd {config.BENCHMARK_DIR};"
    CMD_RUN_EVOSUITE_GENERATED_TESTS = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=10 -cp {Dir_ClassPath} org.junit.runner.JUnitCore {FQN_test_class} > {Path_exe_test_log} 2>&1"
    CMD_RUN_EVOSUITE_GENERATED_TESTS_res = os.system( CMD_RUN_EVOSUITE_GENERATED_TESTS )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{FQN_test_class}  cve_exe_cmd: {CMD_RUN_EVOSUITE_GENERATED_TESTS_res}  CMD: {CMD_RUN_EVOSUITE_GENERATED_TESTS}')
    
    # get execution result
    if not file_processing.pathExist(Path_exe_test_log): 
        print("ERROR: not file_processing.pathExist(Path_output_of_run_GeneratedESTestFile)", Path_exe_test_log)
        return False
    print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log)
    # print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    # exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log,Path_GeneratedESTestFile,FullyQuilfiedName_targetAutoMRMethod, assertionLineNums)
    # print( exe_result ) 
    return exe_result

def originalMTC_test_IT(MTC_item, GTorGenerated, POJ_DIR=config.BENCHMARK_DIR, EXE_RESULT_DIR = CRAFTED_MTC_IT_TEST_EXE_RESULT_DIR):
    """
    Args:
        MTC_item (_type_): _description_
        GTorGenerated (_type_): "GT" ITrans function or LLM-"Generated" ITrans function
        POJ_DIR (_type_, optional): _description_. Defaults to config.BENCHMARK_DIR.

    Returns:
        _type_: _description_
    """
    # profile
    test_file_path = MTC_item["test_file_path"]
    poj_name = MTC_item["poj_name"]
    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
    # poj_compilation_info = json_processing.read( f"{poj_dir}AutoMR/compile_info.json" )
    poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
    poj_build_tool = poj_compilation_info["build_tool"][0]
    jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

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

    poj_ITRANS_MTC_ITrans_DIR = ITRANS_MTCIT_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_MTC_ITrans_DIR)
    poj_ITRANS_GT_DIR = ITRANS_GT_DIR % poj_name
    poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name

    test_exe_dir = f"{test_file_path.split('/projects/')[0]}/projects/{poj_name}/AutoMR/test_exe/"
    file_processing.creatFolder_recursively_IfExistPass(test_exe_dir)
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    ## 主要：
    MTCITrans_only_test_class_name = f"{MTC_test_class_name}_{test_simple_name}Test" # crafted_subject.MTCITrans_only_test_class_FQN
    MTCITrans_only_test_class_file_path = f"{poj_ITRANS_MTC_ITrans_DIR}{invoked_package_FQN.replace('.','/')}/{MTCITrans_only_test_class_name}.java" # wo
    target_class_FQN = f"{invoked_package_FQN}.{MTCITrans_only_test_class_name}"

    # Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log"
    # Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
    Path_execution_log = f"{EXE_RESULT_DIR}{target_class_FQN}.log"
    Path_execution_result = f"{EXE_RESULT_DIR}{target_class_FQN}.json"
    Path_test_file = MTCITrans_only_test_class_file_path
    extra_cp = f"{poj_ITRANS_GT_DIR}:{poj_ITRANS_MTC_ITrans_DIR}:{poj_ITRANS_GENERATED_IT_DIR}"
    # run test
    EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)
    MTC_IT_test_case_name = f"{test_simple_name}_IT"
    if MTC_IT_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
        print(f"Error, failed to execute: {target_class_FQN} ")
    else:
        execute_MTC_ITrans_result = True
    
    Path_exe_test_log = Path_execution_log
    # get execution result
    if not file_processing.pathExist(Path_exe_test_log): 
        print("ERROR: not file_processing.pathExist(Path_output_of_run_GeneratedESTestFile)", Path_exe_test_log)
        return False
    print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    # exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log)
    # print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    # exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log,Path_GeneratedESTestFile,FullyQuilfiedName_targetAutoMRMethod, assertionLineNums)
    # print( exe_result ) 
    return EXE_RESULT[target_class_FQN]

def ES_test_IT(MTC_item, GTorGenerated, POJ_DIR=config.BENCHMARK_DIR, EXE_RESULT_DIR = ES_TEST_EXE_RESULT_DIR):
    """
    Args:
        MTC_item (_type_): _description_
        GTorGenerated (_type_): "GT" ITrans function or LLM-"Generated" ITrans function
        POJ_DIR (_type_, optional): _description_. Defaults to config.BENCHMARK_DIR.

    Returns:
        _type_: _description_
    """
    # profile
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"

    # run test
    Dir_ClassPath = GT_processing.get_classpath(MTC_item, POJ_DIR)
    # Dir_ClassPath = f".:evosuite-tests:{all_class_dir_str}:{PATH_EVOSUITE_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}"
    FQN_test_class = f"com.dataset.{processed_crafted_GT_MTC_test_class_name}{suffix_single_test}"
    Path_exe_test_log = f"{EXE_RESULT_DIR}{processed_crafted_GT_MTC_test_class_name}{suffix_single_test}_{GTorGenerated}.log"
    file_processing.creatFolder_IfExistPass(EXE_RESULT_DIR)

    CMD_CD = f"cd {config.BENCHMARK_DIR};"
    CMD_RUN_EVOSUITE_GENERATED_TESTS = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=10 -cp {Dir_ClassPath} org.junit.runner.JUnitCore {FQN_test_class} > {Path_exe_test_log} 2>&1"
    CMD_RUN_EVOSUITE_GENERATED_TESTS_res = os.system( CMD_RUN_EVOSUITE_GENERATED_TESTS )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{FQN_test_class}  cve_exe_cmd: {CMD_RUN_EVOSUITE_GENERATED_TESTS_res}  CMD: {CMD_RUN_EVOSUITE_GENERATED_TESTS}')
    
    # get execution result
    if not file_processing.pathExist(Path_exe_test_log): 
        print("ERROR: not file_processing.pathExist(Path_output_of_run_GeneratedESTestFile)", Path_exe_test_log)
        return False
    exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log)
    # print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    # exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log,Path_GeneratedESTestFile,FullyQuilfiedName_targetAutoMRMethod, assertionLineNums)
    # print( exe_result ) 
    return exe_result


def Diff_test_IT(MTC_item, GTorGenerated, POJ_DIR=config.BENCHMARK_DIR, EXE_RESULT_DIR = ES_TEST_EXE_RESULT_DIR):
    """
    Args:
        MTC_item (_type_): _description_
        GTorGenerated (_type_): "GT" ITrans function or LLM-"Generated" ITrans function
        POJ_DIR (_type_, optional): _description_. Defaults to config.BENCHMARK_DIR.

    Returns:
        _type_: _description_
    """
    # profile
    test_file_path = MTC_item["test_file_path"]
    test_simple_name = MTC_item["test_simple_name"]
    MTC_test_class_name = test_file_path.split("/")[-1].replace(".java", "")
    processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"

    # run test
    Dir_ClassPath = GT_processing.get_classpath(MTC_item, POJ_DIR)
    # Dir_ClassPath = f".:evosuite-tests:{all_class_dir_str}:{PATH_EVOSUITE_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}"
    FQN_test_class = f"com.dataset.{processed_crafted_GT_MTC_test_class_name}{suffix_diff_test}"
    Path_exe_test_log = f"{EXE_RESULT_DIR}{processed_crafted_GT_MTC_test_class_name}{suffix_diff_test}_{GTorGenerated}.log"
    file_processing.creatFolder_IfExistPass(EXE_RESULT_DIR)

    CMD_CD = f"cd {config.BENCHMARK_DIR};"
    CMD_RUN_EVOSUITE_GENERATED_TESTS = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=10 -cp {Dir_ClassPath} org.junit.runner.JUnitCore {FQN_test_class} > {Path_exe_test_log} 2>&1"
    CMD_RUN_EVOSUITE_GENERATED_TESTS_res = os.system( CMD_RUN_EVOSUITE_GENERATED_TESTS )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{FQN_test_class}  cve_exe_cmd: {CMD_RUN_EVOSUITE_GENERATED_TESTS_res}  CMD: {CMD_RUN_EVOSUITE_GENERATED_TESTS}')
    
    # get execution result
    if not file_processing.pathExist(Path_exe_test_log): 
        print("ERROR: not file_processing.pathExist(Path_output_of_run_GeneratedESTestFile)", Path_exe_test_log)
        return False
    exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log)
    # print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_exe_test_log}'")
    # exe_result = java_file_processing.analyze_test_exe_result(Path_exe_test_log,Path_GeneratedESTestFile,FullyQuilfiedName_targetAutoMRMethod, assertionLineNums)
    # print( exe_result ) 
    return exe_result


def LLMI_test_IT(MTC_item, GTorGenerated, POJ_DIR=config.BENCHMARK_DIR, EXE_RESULT_DIR = None, test_exe_dir_BACKUP=False, passIfexecuted=True, valid_Sinput_4_validation=False, LLMI_input_generation_result=None, for_evaluation=False):
    """
    Args:
        MTC_item (_type_): _description_
        GTorGenerated (_type_): "GT" ITrans function or LLM-"Generated" ITrans function
        POJ_DIR (_type_, optional): _description_. Defaults to config.BENCHMARK_DIR.

    Returns:
        _type_: _description_
    """
    symbol = "LLMI_test_Trans"

    # profile
    FQS_testMethos = MTC_item["FQS_testMethos"]
    test_file_path = MTC_item["test_file_path"]
    poj_name = MTC_item["poj_name"]
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
    invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]
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

    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
    poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
    poj_build_tool = poj_compilation_info["build_tool"][0]
    jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

    poj_ITRANS_GT_DIR = ITRANS_GT_DIR % poj_name
    poj_ITRANS_MTC_ITrans_DIR = ITRANS_MTCIT_DIR % poj_name
    poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name; 
    poj_ITRANS_GENERATED_INPUTS_DIR = ITRANS_GENERATED_INPUTS_DIR % poj_name;
    poj_ITRANS_GENERATED_LLMI_TEST_DIR = ITRANS_GENERATED_LLMI_TEST_DIR % poj_name
    file_processing.creatFolder_recursively_IfExistPass(poj_ITRANS_GENERATED_LLMI_TEST_DIR)

    all_exe_result = {
        "num_of_test_cases": 0,
        "num_of_passed_test_cases": 0,
        "num_of_assertion_failed_test_cases":0, 
        "num_of_exception_thrown_test_cases":0, 
        "num_of_reach_assertion_test_cases": -1, 
        "assertionLineNums": [],
        "reach_assertion_test_cases_list":[],
        "assertion_failed_test_cases_list":[], 
        "exception_thrown_test_cases_list":[], 
        "passed_test_cases_list":[], 
        "failure_info":{}
    }

    """ 1. cp test4Trans in to corresponding dir: LLMI_test_Trans/ """
    # collect generated_valid_inputs_info
    path_of_generated_inputs_in_cache = ""
    if LLMI_input_generation_result == None:
        if for_evaluation==True:
            input_generation_result = generate_Inputs_with_LLMs.generate_inputs_for_one(MTC_item, generate_Inputs_with_LLMs.for_evaluation_setting, just_collect_result=True)
        else:
            input_generation_result = generate_Inputs_with_LLMs.generate_inputs_for_one(MTC_item, generate_Inputs_with_LLMs.Setting, just_collect_result=True) # Setting, need to be reset
    else: 
        input_generation_result = LLMI_input_generation_result
    # which one used to for validation: "valid_inputs_info" / "valid_Sinput_info"
    generated_valid_inputs_info = input_generation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos]["valid_inputs_info"] # default
    if valid_Sinput_4_validation:
        generated_valid_inputs_info = input_generation_result["meta_list"]["subject_compilableORvalid_inputs_size"][FQS_testMethos]["valid_Sinput_info"]

    if len(generated_valid_inputs_info) == 0:
        return None # non generated valid inputs

    poj_ITRANS_GENERATED_LLMI_TEST_package_dir = f"{poj_ITRANS_GENERATED_LLMI_TEST_DIR}{invoked_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(poj_ITRANS_GENERATED_LLMI_TEST_package_dir)

    for valid_input in generated_valid_inputs_info.keys():
        test_class_path = generated_valid_inputs_info[valid_input]["path"]
        target_class_FQN = generated_valid_inputs_info[valid_input]["FQN"]
        # the refactored LLMI test4Trans: 1. generated_input/ -> generated_input/ -> generated_valid_inputs_testing_Trans/ 2. class -> _valid.class
        test_class_path = test_class_path.replace(f"/{generate_Inputs_with_LLMs.inputGenerator.generated_inputs_dir_name}/", f"/{generate_Inputs_with_LLMs.inputGenerator.generated_valid_inputs_testing_Trans_dir_name}/")
        test_class_path = test_class_path.replace(".java",f"{VALID_INPUT_CLASS_SUFFIX}.java")
        target_class_FQN = f"{target_class_FQN}{VALID_INPUT_CLASS_SUFFIX}"

        test_class_file_name = test_class_path.split("/")[-1]
        test_class_path_in_origianl_poj = poj_ITRANS_GENERATED_LLMI_TEST_package_dir + test_class_file_name
        # copy
        if not file_processing.pathExist(test_class_path) or not file_processing.pathExist(test_class_path.replace(".java",".class")):
            print(f"ERROR: LLMI_test_IT, not existing valid inputs class path: {test_class_path}")
            continue 
        file_processing.copyFile(test_class_path, test_class_path_in_origianl_poj)
        # file_processing.copyFile(test_class_path.replace(".java",".class"), test_class_path_in_origianl_poj.replace(".java",".class"))
        file_processing.copyFile(test_class_path.replace(".java",".class"), poj_ITRANS_GENERATED_LLMI_TEST_package_dir)
        # copy: extra needed classes
        num = 1;extra_class_path = test_class_path.replace(".java",f"${num}.class")
        while file_processing.pathExist(extra_class_path):
            file_processing.copyFile(source=extra_class_path,target=poj_ITRANS_GENERATED_LLMI_TEST_package_dir)
            num += 1;extra_class_path = test_class_path.replace(".java",f"${num}.class")

        """ 2. run test """ 
        extra_cp = f"{poj_ITRANS_GT_DIR}:{poj_ITRANS_MTC_ITrans_DIR}:{poj_ITRANS_GENERATED_IT_DIR}:{poj_ITRANS_GENERATED_INPUTS_DIR}:{poj_ITRANS_GENERATED_INPUTS_DIR}:{poj_ITRANS_GENERATED_LLMI_TEST_DIR}"
        # 3. exe_results and log to cache (rename)
        # execute the MTC_h_only_test
        test_exe_dir = f"{EXE_RESULT_DIR}LLMI_test_Trans/"; file_processing.creatFolder_recursively_IfExistPass(test_exe_dir);
        Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log" 
        Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
        Path_test_file = test_class_path
        successful_exe = True
        EXE_RESULT = None
        if (passIfexecuted and file_processing.pathExist(Path_execution_result)):
            EXE_RESULT = json_processing.read(Path_execution_result)
            print(f"Skip: {target_class_FQN} has been executed")
        elif not (passIfexecuted and file_processing.pathExist(Path_execution_result)):
            EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)

        """ 3. collect exe test """ 
        exe_result = EXE_RESULT[target_class_FQN]
        num_of_test_cases = exe_result["num_of_test_cases"]
        num_of_passed_test_cases = exe_result["num_of_passed_test_cases"]
        passed_test_cases_list = exe_result["passed_test_cases_list"]

        all_exe_result["num_of_test_cases"] += num_of_test_cases
        all_exe_result["num_of_passed_test_cases"] += exe_result["num_of_passed_test_cases"]
        all_exe_result["num_of_assertion_failed_test_cases"] += exe_result["num_of_assertion_failed_test_cases"]
        all_exe_result["num_of_exception_thrown_test_cases"] += exe_result["num_of_exception_thrown_test_cases"]
        all_exe_result["num_of_reach_assertion_test_cases"] += exe_result["num_of_reach_assertion_test_cases"]
        all_exe_result["assertionLineNums"].append(exe_result["assertionLineNums"])
        all_exe_result["reach_assertion_test_cases_list"].append(exe_result["reach_assertion_test_cases_list"])
        all_exe_result["assertion_failed_test_cases_list"].append(exe_result["assertion_failed_test_cases_list"])
        all_exe_result["passed_test_cases_list"].append(exe_result["passed_test_cases_list"])
        if len(passed_test_cases_list) ==0 or num_of_passed_test_cases < num_of_test_cases:
            all_exe_result["failure_info"][target_class_FQN]= exe_result["failure_info"]

        # 复位： delete test4Trans in to corresponding dir
        file_processing.remove_file(test_class_path_in_origianl_poj)
        file_processing.remove_file(test_class_path_in_origianl_poj.replace(".java",".class"))
    # write all all_exe_result
    return all_exe_result
    


def execute_generated_inputs(input_generator, Path_test_file, target_class_FQN, passIfexecuted=True, test_exe_dir_BACKUP=False):
    MTC_item = input_generator.MTC_item
    MTChClass = input_generator.MTChClass
    generated_inputs_folder_name = input_generator.generated_inputs_folder_name
    generated_valid_inputs_folder_name = input_generator.generated_valid_inputs_folder_name
    
    # profile
    test_file_path = MTC_item["test_file_path"]
    poj_name = MTC_item["poj_name"]
    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
    poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
    poj_build_tool = poj_compilation_info["build_tool"][0]
    jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]

    poj_ITRANS_GT_DIR = ITRANS_GT_DIR % poj_name
    poj_ITRANS_MTC_ITrans_DIR = ITRANS_MTCIT_DIR % poj_name
    poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name; 
    poj_ITRANS_GENERATED_INPUTS_DIR = ITRANS_GENERATED_INPUTS_DIR % poj_name;

    # setting for exectute test case
    FQS_testMethos = MTC_item["FQS_testMethos"]
    test_simple_name = MTC_item["test_simple_name"]
    test_exe_dir = f"{test_file_path.split('/projects/')[0]}/projects/{poj_name}/AutoMR/test_exe/"
    file_processing.creatFolder_recursively_IfExistPass(test_exe_dir)
    extra_cp = f"{poj_ITRANS_GT_DIR}:{poj_ITRANS_MTC_ITrans_DIR}:{poj_ITRANS_GENERATED_IT_DIR}:{poj_ITRANS_GENERATED_INPUTS_DIR}:{poj_ITRANS_GENERATED_INPUTS_DIR}{generated_inputs_folder_name}:{poj_ITRANS_GENERATED_INPUTS_DIR}{generated_valid_inputs_folder_name}"

    # execute the MTC_h_only_test
    # target_class_FQN = input_generator.target_class_FQN
    Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log"
    Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
    successful_exe = True
    if (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = json_processing.read(Path_execution_result)
        print(f"Skip: {target_class_FQN} has been executed")
    elif not (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)
    if test_exe_dir_BACKUP:
        Path_execution_log_BACKUP = f"{test_exe_dir_BACKUP}{target_class_FQN}.log"
        Path_execution_result_BACKUP = f"{test_exe_dir_BACKUP}{target_class_FQN}.json"
        file_processing.copyFile(Path_execution_log, Path_execution_log_BACKUP)
        file_processing.copyFile(Path_execution_result, Path_execution_result_BACKUP)

    return EXE_RESULT[target_class_FQN]