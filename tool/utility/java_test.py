import datetime
import json, os, sys
_PROJECT_NAME = "InputTrans"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

import config
from utility import java_file_processing, file_processing, json_processing, compile_java_poj

# execute test case after compile

PATH_JUNIT4_JAR = config.PATH_JUNIT4_JAR
PATH_JUNIT5_JAR = config.PATH_JUNIT5_JAR
PATH_HAMCREST_CORE_JAR = config.PATH_HAMCREST_CORE_JAR
PATH_JUNIT5_STANDALONE_JAR = config.PATH_JUNIT5_STANDALONE_JAR
JUNIT_JARS_CP_str = f"{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}"

PATH_ES_RUNTIME_JAR = config.PATH_ES_RUNTIME_JAR

more_potential_dependency_jars = "  TODO/.m2/repository/org/slf4j/slf4j-api/2.0.0/slf4j-api-2.0.0.jar:  TODO/.m2/repository/org/apache/logging/log4j/log4j-api/2.1/log4j-api-2.1.jar:  TODO/.m2/repository/com/google/guava/guava/33.0.0-jre/guava-33.0.0-jre.jar:  TODO/.m2/repository/com/fasterxml/jackson/core/jackson-databind/2.4.0/jackson-databind-2.4.0.jar:  TODO/.m2/repository/com/fasterxml/jackson/core/jackson-core/2.12.1/jackson-core-2.12.1.jar:  TODO/.m2/repository/org/springframework/spring-test/5.3.26/spring-test-5.3.26.jar:  TODO/data/ITrans/projects/thingsboard____thingsboard/dao/target/dependency/commons-logging-1.2.jar:  TODO/.m2/repository/org/springframework/spring-core/5.3.2/spring-core-5.3.26.jar:arex-instrumentation-api/target/dependency/jackson-annotations-2.13.1.jar:arex-instrumentation-api/target/dependency/gson-2.10.1.jar:misc/extra/target/dependency/vecmath-1.5.2.jar"

def test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool="maven", addtional_classpath="", ifExeResult_skip=True, extra_cp=''):
    if not file_processing.pathExist(Path_test_file):
        print("skip, because of Path_test_file not existing: ", Path_test_file)
        return {}

    if ifExeResult_skip and file_processing.pathExist(Path_execution_result): 
        print("skip, because of existing: ", target_class_FQN, Path_execution_result)
        return {}
    
    DIR_POJ = poj_dir
    CMD_CD_POJ_DIR = f"cd {DIR_POJ} ;"
    class_relative_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
    class_relative_dir_list = [ f"./{ele}" for ele in class_relative_dir_list ]
    all_poj_class_dir_str = (":").join( class_relative_dir_list )
    EXE_RESULT = {}


    FullyQuilfiedName_targetCUTClass = target_class_FQN
    Name_targetCUTClass =FullyQuilfiedName_targetCUTClass.split(".")[-1]
    FullyQuilfiedName_prefix = ".".join(FullyQuilfiedName_targetCUTClass.split(".")[:-1])
    PATH_JAVA = compile_java_poj.get_jdk_path(jdk_version)

    junit_type = 4
    # for junit 5
    if "org.junit.jupiter.api" in file_processing.read_TXTfile(Path_test_file):
        junit_type = 5

        # java -jar   TODO/software/junit/junit-platform-console-standalone-1.10.0.jar --class-path=  TODO/software/junit/junit-platform-console-standalone-1.10.0.jar:  TODO/.m2/repository/org/slf4j/slf4j-api/2.0.0/slf4j-api-2.0.0.jar --select-class=com.github.kagkarlsson.scheduler.ExecutionTest >   TODO/data/AutoMR/projects/kagkarlsson____db-scheduler/AutoMR/test_exe/com.github.kagkarlsson.scheduler.ExecutionTest.log 2>&1
        CMD_RUN_TESTS = f"{CMD_CD_POJ_DIR} {PATH_JAVA} -XX:ActiveProcessorCount=10 -jar {PATH_JUNIT5_STANDALONE_JAR} --class-path=./:{all_poj_class_dir_str}:{JUNIT_JARS_CP_str}:{more_potential_dependency_jars}:{extra_cp} --select-class={FullyQuilfiedName_targetCUTClass} > {Path_execution_log} 2>&1"
        CMD_RUN_TESTS_res = os.system( CMD_RUN_TESTS )
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{poj_dir} cve_exe_cmd: {CMD_RUN_TESTS_res}  CMD_RUN_TEST-CASE: {CMD_RUN_TESTS}') 

    # for junit 4
    else:
        CMD_RUN_TESTS = f"{CMD_CD_POJ_DIR} {PATH_JAVA} -XX:ActiveProcessorCount=10 -classpath ./:{all_poj_class_dir_str}:{JUNIT_JARS_CP_str}:{more_potential_dependency_jars}:{extra_cp} org.junit.runner.JUnitCore {FullyQuilfiedName_targetCUTClass} > {Path_execution_log} 2>&1"
        CMD_RUN_TESTS_res = os.system( CMD_RUN_TESTS )
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{poj_dir} cve_exe_cmd: {CMD_RUN_TESTS_res}  CMD_RUN_TEST-CASE: {CMD_RUN_TESTS}')    
    
    if not file_processing.pathExist(Path_execution_log): 
        print("ERROR: not file_processing.pathExist(Path_test_execution_log)", Path_execution_log);
        return EXE_RESULT
    os.system( f"echo \"CMD: {CMD_RUN_TESTS}\" >> {Path_execution_log}" )
    if Path_test_file:
        test_file_content = file_processing.read_TXTfile(Path_test_file)
        os.system( f"echo \"file path: \n{Path_test_file}\" >> {Path_execution_log}" )
        os.system( f"echo \"file content: \n{test_file_content}\" >> {Path_execution_log}" )
    print("java_file_processing.analyze_test_exe_result: ", f"java_file_processing.analyze_test_exe_result('{Path_execution_log}','{Path_test_file}','{junit_type}')")
    exe_result = java_file_processing.analyze_test_exe_result(Path_execution_log, Path_Test_file=Path_test_file, junit_type=junit_type)

    EXE_RESULT[FullyQuilfiedName_targetCUTClass] = exe_result
    json_processing.write(json_content=EXE_RESULT, path=Path_execution_result)
    return EXE_RESULT


def compile_test_class_general(poj_build_tool, TASK_POJ_NAMR, CMD_CD, DIR_POJ, CP_jar_path, extra_cp, Path_TestFile_to_compile, PATH_JAVAC, log_dir=False, log_file_suffix=""):
    class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
    all_class_dir_str = (":").join( class_dir_list )
    CLASS_PATHS = f"{extra_cp}:{all_class_dir_str}:{CP_jar_path}"
    Dir_ClassPath = f"{CLASS_PATHS}:{PATH_ES_RUNTIME_JAR}:{JUNIT_JARS_CP_str}:{more_potential_dependency_jars}"
    if log_dir:
        log_file_name = Path_TestFile_to_compile.split("/")[-1].replace(".java", "")
        CMD_COMPILE_test_class = f"{CMD_CD} {PATH_JAVAC} {Path_TestFile_to_compile} -cp .:{Dir_ClassPath} > {log_dir}/{log_file_name}_compile_{log_file_suffix}.log 2>&1"
    else:
        CMD_COMPILE_test_class = f"{CMD_CD} {PATH_JAVAC} {Path_TestFile_to_compile} -cp .:{Dir_ClassPath}"
    CMD_COMPILE_test_class_res = os.system( CMD_COMPILE_test_class )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{TASK_POJ_NAMR}  cve_exe_cmd: {CMD_COMPILE_test_class_res} Path_TestFile_to_compile: {Path_TestFile_to_compile} CMD_COMPILE_test_class: {CMD_COMPILE_test_class}')

    # generated_dot_class_path = Path_TestFile_to_compile.replace(".java", ".class")
    # if CMD_COMPILE_test_class_res==0:
    #     return generated_dot_class_path
    # else:
    #     return None
    return CMD_COMPILE_test_class_res