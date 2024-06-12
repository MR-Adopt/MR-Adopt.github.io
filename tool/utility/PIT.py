#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author:  
@Created: 2022/06/16
------------------------------------------
@Modify: 2022/06/16
------------------------------------------
@Description:


"""

import json, os, sys
import re
_PROJECT_NAME = "InputTrans"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

import datetime
import time
import csv

from utility import file_processing, json_processing, java_file_processing, compile_java_poj
import config


EXPERIMENTAL_POJS_DIR = config.AUTOMR_EXPERIMENTAL_POJS_DIR
SPLITE_STR = config.SPLITE_STR
PATH_AUTOMR_PROFILE_JSON = config.PATH_AUTOMR_PROFILE_JSON
PATH_PIT_RESULT_JSON = config.PATH_PIT_RESULT_JSON
PATH_PIT_RANDOOP_RESULT_JSON = config.PATH_PIT_RANDOOP_RESULT_JSON
PATH_AUTOMR_RANDOOP_TESTS_EXE_JSON = config.PATH_AUTOMR_RANDOOP_TESTS_EXE_JSON


PATH_MVN = config.PATH_MVN
PATH_JAVA = config.PATH_JAVA

PATH_EVOSUITE_JAR = config.PATH_EVOSUITE_JAR
PATH_ES_RUNTIME_JAR = config.PATH_ES_RUNTIME_JAR
PATH_JUNIT4_JAR = config.PATH_JUNIT4_JAR
PATH_JUNIT5_JAR = config.PATH_JUNIT5_JAR
PATH_OPENTT4J_JAR = config.PATH_OPENTT4J_JAR
PATH_HAMCREST_CORE_JAR = config.PATH_HAMCREST_CORE_JAR
PATH_PITEST_JAR = config.PATH_PITEST_JAR
PATH_PITEST_CMD_JAR = config.PATH_PITEST_CMD_JAR
PATH_PITEST_ENTRY_JAR = config.PATH_PITEST_ENTRY_JAR
PATH_PITEST_JUNIT5_PLUGIN_JAR = config.PATH_PITEST_JUNIT5_PLUGIN_JAR

PATH_JUNIT5_ENGINE_JAR = "  TODO/software/junit/junit-jupiter-engine-5.8.2.jar:  TODO/software/junit/junit-platform-engine-1.8.2.jar:  TODO/software/junit/junit-platform-launcher-1.8.2.jar"

PATH_JAVAC_11 = config.PATH_JAVAC_11
PATH_JAVA_11 = config.PATH_JAVA_11
DIR_JAVA_11 = config.DIR_JAVA_11

PATH_GRADLE_7_4 = config.PATH_GRADLE_7_4
DIR_GRADLE_USER_HOME = config.DIR_GRADLE_USER_HOME
CMD_GRADLE_7_4_WITH_PARAMETERS = f"{PATH_GRADLE_7_4} -Dgradle.user.home={DIR_GRADLE_USER_HOME} -Dorg.gradle.java.home={DIR_JAVA_11}"

PATH_JAVA = PATH_JAVA_11
PATH_JAVAC = f"{PATH_JAVA}c"


DIR_MAVEN_USER_HOME = config.DIR_MAVEN_USER_HOME
# 临时加入，解决class not found问题。。。
tem_dependency_0703 = f"{DIR_MAVEN_USER_HOME}repository/com/alibaba/fastjson/1.2.60/fastjson-1.2.60.jar:{DIR_MAVEN_USER_HOME}repository/com/google/guava/guava/21.0/guava-21.0.jar"


pit_result_item = {
    "Line_Coverage":"0/0", "Line_Coverage_float":0,
    "Generated_mutations":0, "Killed_mutations":0, "Covered_mutations":0, "Mutation_score":0.0, "Mutants_coverage(covered/all)":0.0, "Mutations_with_no_coverage":0,  
    "Test_strength":"0%", "Test_strength_float":0,
    "Num_of_test_cases":None, "MutantsAndStatus":{}, "killedMutants":[], "CoveredMutants":[],
    "CUT":None}

# def PIT_runner(poj_meta, ifPITResult_skipPITR=False, poj_build_tool="maven"):
def PIT_runner(pit_runner):
    flag_PIT_runner_exe_successful = False

    # if ifPITResult_skipPITR and file_processing.pathExist(path=PATH_PIT_RESULT_JSON % poj):
    #     flag_PIT_runner_exe_successful = True
    #     return flag_PIT_runner_exe_successful

    """ 2. 针对通过的Green cases，计算mutation coverage  """
    # cd /home1/ /data/AutoMR/projects/opentelecoms-org____jsmpp/ ; /home1/ /software/jdk1.8.0_131/bin/java -cp .:jsmpp/target/classes:jsmpp/target/test-classes:/home1/ /software/pitest/pitest-1.8.0.jar:/home1/ /software/pitest/pitest-command-line-1.8.0.jar:/home1/ /software/pitest/pitest-entry-1.8.0.jar:/home1/ /software/evosuite/evosuite-standalone-runtime-1.2.0.jar:/home1/ /software/junit/junit-4.13.2.jar:/home1/ /software/junit/junit-jupiter-api-5.8.2.jar:/home1/ /software/junit/hamcrest-core-1.3.jar org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir pit/ --targetClasses org.jsmpp.util.OctetUtil --targetTests org.jsmpp.util.OctetUtilTest_AutoMR_ESTestGreen --sourceDirs jsmpp/src/
    # CMD_CD = f"cd /home1/ /data/AutoMR/projects/{poj}/ ;"
    
    # FullyQuilfiedName_TestForCUT = "org.datagear.util.version.VersionTest_isEqualTest_hTest" # TODO
    # EXPERIMENTAL_POJS_DIR   = "  TODO/data/ITrans/projects/"
    # poj = "datageartech____datagear"
    # FullyQuilfiedName_targetCUT = "org.datagear.util.version.Version" # derived from invoked methods U dependency. but be careful
    # MTC_test_file_path = "  TODO/data/ITrans/projects/datageartech____datagear/datagear-util/src/test/java/org/datagear/util/version/VersionTest.java"
    # poj_build_tool = "maven"

    exist_then_skip = pit_runner.exist_then_skip
    FullyQuilfiedName_TestForCUT = pit_runner.FullyQuilfiedName_TestForCUT
    EXPERIMENTAL_POJS_DIR   = pit_runner.EXPERIMENTAL_POJS_DIR
    poj = pit_runner.poj
    FullyQuilfiedName_targetCUT = pit_runner.FQN_CUTs_formal
    MTC_test_file_path = pit_runner.MTC_test_file_path
    poj_build_tool = pit_runner.poj_build_tool
    extra_cp = pit_runner.extra_cp
    path_pit_result = pit_runner.path_pit_result
    keyname_id = pit_runner.keyname_id
    testMethodName_flag_and_value = pit_runner.testMethodName_flag_and_value


    DIR_POJ = EXPERIMENTAL_POJS_DIR + poj +'/'
    DIR_PIT_OUTUT = DIR_POJ + "pit/"
    CMD_CD = f"cd {DIR_POJ} ;"
    file_processing.creatFolder_IfExistPass(DIR_PIT_OUTUT)
    
    DIR_POJ_SRC =  MTC_test_file_path.split("src")[0] +'src'
    DIR_POJ_SRC = DIR_POJ + DIR_POJ_SRC.split(f"{poj}/")[-1] # /home1/  /data/AutoMR/projects/OPCFoundation____UA-Java-Legacy/...  -> DIR_POJ/...

    # Dir_ClassPath = 
    DIR_POJ_PKG = MTC_test_file_path.split("src")[0] # developper-written test_file_path
    DIR_POJ_PKG = DIR_POJ + DIR_POJ_PKG.split(f"{poj}/")[-1] # /home1/  /data/AutoMR/projects/OPCFoundation____UA-Java-Legacy/...  -> DIR_POJ/...
    class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool, specific_dependency_folder=DIR_POJ_PKG)
    all_class_dir_str = (":").join( class_dir_list )
    print("DIR_POJ_PKG: ", DIR_POJ_PKG)
    
    
    PIT_RESULT = {}
    if file_processing.pathExist(path_pit_result):
        PIT_RESULT = json_processing.read( path=path_pit_result )
        # if exist_then_skip and keyname_id in PIT_RESULT and isinstance(PIT_RESULT[keyname_id], dict) and PIT_RESULT[keyname_id]['Line_Coverage'].split("/")[0]!='0':
        #     print("exist_then_skip", keyname_id)
        #     return True
    if True:
        Path_defaultOutputCSV_of_run_PIT_for_TestForCUT = DIR_PIT_OUTUT + "mutations.csv"
        Path_output_of_run_PIT_for_TestForCUT = DIR_PIT_OUTUT + keyname_id.split(".")[-1] + ".pit_log"
        Path_outputCSV_of_run_PIT_for_TestForCUT = DIR_PIT_OUTUT + keyname_id.split(".")[-1] + ".csv"

        # try run1: without PATH_PITEST_JUNIT5_PLUGIN_JAR
        Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:evosuite-tests:{all_class_dir_str}"
        CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {Dir_ClassPath}:{extra_cp} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
        os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
        CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '1 "MSG: without PATH_PITEST_JUNIT5_PLUGIN_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
        if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
            time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
        os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
        pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)

        # try run2: with PATH_PITEST_JUNIT5_PLUGIN_JAR,
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:evosuite-tests:{all_class_dir_str}"
            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {Dir_ClassPath}:{extra_cp} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '2 "MSG: with PATH_PITEST_JUNIT5_PLUGIN_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
        
        # try run2.5: with PATH_PITEST_JUNIT5_PLUGIN_JAR, + PATH_JUNIT5_ENGINE_JAR
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:{PATH_JUNIT5_ENGINE_JAR}:evosuite-tests:{all_class_dir_str}"
            CP_content = f"{Dir_ClassPath}:{extra_cp}"
            # path_CP_content = Path_output_of_run_PIT_for_TestForCUT.replace(".pit_log", "_cp_content.txt")
            # file_processing.write_TXTfile(path=path_CP_content, content=CP_content)

            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {CP_content} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '2.5 "MSG: with PATH_PITEST_JUNIT5_PLUGIN_JAR+ PATH_JUNIT5_ENGINE_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
            
        # try run2.6: with PATH_PITEST_JUNIT5_PLUGIN_JAR, + PATH_JUNIT5_ENGINE_JAR + PATH_OPENTT4J_JAR
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_OPENTT4J_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:{PATH_JUNIT5_ENGINE_JAR}:evosuite-tests:{all_class_dir_str}"
            CP_content = f"{Dir_ClassPath}:{extra_cp}"
            # path_CP_content = Path_output_of_run_PIT_for_TestForCUT.replace(".pit_log", "_cp_content.txt")
            # file_processing.write_TXTfile(path=path_CP_content, content=CP_content)

            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {CP_content} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '2.6 "MSG: with PATH_PITEST_JUNIT5_PLUGIN_JAR+ PATH_JUNIT5_ENGINE_JAR + PATH_OPENTT4J_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)

        # try run3: with all dependency folders (可能会Arguments too long) + without PATH_PITEST_JUNIT5_PLUGIN_JAR. 
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
            all_class_dir_str = (":").join( class_dir_list )

            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:evosuite-tests:{all_class_dir_str}"
            CP_content = f"{Dir_ClassPath}:{extra_cp}"
            # path_CP_content = Path_output_of_run_PIT_for_TestForCUT.replace(".pit_log", "_cp_content.txt")
            # file_processing.write_TXTfile(path=path_CP_content, content=CP_content)
            
            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {CP_content} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '3 "MSG: all dependency folders + without PATH_PITEST_JUNIT5_PLUGIN_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
        # try run4: with all dependency folders (可能会Arguments too long) + with PATH_PITEST_JUNIT5_PLUGIN_JAR
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
            all_class_dir_str = (":").join( class_dir_list )

            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:evosuite-tests:{all_class_dir_str}"
            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {Dir_ClassPath}:{extra_cp} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '4 "MSG: all dependency folders + with PATH_PITEST_JUNIT5_PLUGIN_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
        # try run5: with all dependency folders (可能会Arguments too long) + with PATH_PITEST_JUNIT5_PLUGIN_JAR + PATH_JUNIT5_ENGINE_JAR
        if not isinstance(pit_result, dict) or (isinstance(pit_result, dict) and pit_result['Line_Coverage'].split("/")[0]=='0'): # 说明运行不成功
            class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
            all_class_dir_str = (":").join( class_dir_list )

            Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:{PATH_JUNIT5_ENGINE_JAR}:evosuite-tests:{all_class_dir_str}"
            CMD_RUN_PIT = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {Dir_ClassPath}:{extra_cp} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 {testMethodName_flag_and_value} --testPlugin junit5 --timestampedReports=false --outputFormats CSV > {Path_output_of_run_PIT_for_TestForCUT}"
            os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
            CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '5 "MSG: all dependency folders + with PATH_PITEST_JUNIT5_PLUGIN_JAR + PATH_JUNIT5_ENGINE_JAR"', f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
            if not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT):
                time.sleep(3); print( "JUST sleep", "not file_processing.pathExist(Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)", Path_defaultOutputCSV_of_run_PIT_for_TestForCUT)
            os.system( f"mv {Path_defaultOutputCSV_of_run_PIT_for_TestForCUT} {Path_outputCSV_of_run_PIT_for_TestForCUT}" )
            pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
        
                
        # else:
        #     pit_result = "COIN: no such test file to run pit"
        # print("FullyQuilfiedName_TestForCUT: ", FullyQuilfiedName_TestForCUT, pit_result)
        # PIT_RESULT[FullyQuilfiedName_TestForCUT] = pit_result
        
        new_Line_Coverage_float = 0
        # when pit_result["CUT"] is dict
        if isinstance(pit_result, dict):
            pit_result["CUT"] = FullyQuilfiedName_targetCUT
            new_Line_Coverage_float = pit_result["Line_Coverage_float"]


        # # 1 更新条件：之前的不成功
        # if keyname_id not in PIT_RESULT or ( not isinstance(PIT_RESULT[keyname_id], dict) ) or (PIT_RESULT[keyname_id]['Line_Coverage'].split("/")[0]=='0'):
        #     PIT_RESULT[keyname_id] = pit_result 
        #     print("update: PIT_RESULT[keyname_id]: ", PIT_RESULT[keyname_id])
        # # 1 更新条件：之前比较小
        # if keyname_id in PIT_RESULT and isinstance(PIT_RESULT[keyname_id], dict) and PIT_RESULT[keyname_id]['Line_Coverage'].split("/")[0]!='0':
        #     old_Line_Coverage_float = PIT_RESULT[keyname_id]["Line_Coverage_float"]
        #     if new_Line_Coverage_float > old_Line_Coverage_float:
        #         PIT_RESULT[keyname_id] = pit_result
        #         print("update: PIT_RESULT[keyname_id]: ", PIT_RESULT[keyname_id])
        #         print("new_Line_Coverage_float: ", new_Line_Coverage_float, "old_Line_Coverage_float: ", old_Line_Coverage_float)
        
        # default
        PIT_RESULT[keyname_id] = pit_result
        # TODO 
        if CMD_RUN_PIT_res==0:
            flag_PIT_runner_exe_successful = True
    json_processing.write( json_content=PIT_RESULT, path=path_pit_result)
    return flag_PIT_runner_exe_successful

def PIT_runner_Randoop(poj_meta, ifPITResult_skipPITR=False, poj_build_tool="maven"):
    flag_PIT_runner_exe_successful = False
    poj = poj_meta.poj_name

    if ifPITResult_skipPITR and file_processing.pathExist(path=PATH_PIT_RANDOOP_RESULT_JSON % poj):
        flag_PIT_runner_exe_successful = True
        return flag_PIT_runner_exe_successful

    if poj_meta.AutoMRProfile:
        AutoMRProfile = poj_meta.AutoMRProfile
    else:
        AutoMRProfile = json_processing.read( path= PATH_AUTOMR_PROFILE_JSON % poj )

    """ 1. 删掉未pass的test case -> Green，并编译  """
    # 已在前序步骤中处理

    """ 2. 针对通过的Green cases，计算mutation coverage  """
    DIR_POJ = EXPERIMENTAL_POJS_DIR + poj +'/'
    CMD_CD_POJ_DIR = f"cd {DIR_POJ} ;"
    DIR_PIT_OUTUT = DIR_POJ + "pit/"
    file_processing.creatFolder_IfExistPass(DIR_PIT_OUTUT)
    
    PIT_RESULT = {}
    # Dir_ClassPath = 
    class_relative_dir_list = java_file_processing.get_all_class_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_meta.poj_build_tool)
    all_poj_class_dir_str = (":").join( class_relative_dir_list )
    for generatedMRfilePath in AutoMRProfile.keys():
        FullyQuilfiedName_targetAutoMRClass = AutoMRProfile[generatedMRfilePath]["generatedMRClassFQN"]
        FullyQuilfiedName_targetCUT = AutoMRProfile[generatedMRfilePath]["ClassessUnderTest"]
        Name_targetAutoMRClass = FullyQuilfiedName_targetAutoMRClass.split(".")[-1]

        FullyQuilfiedName_targetCUTClass = AutoMRProfile[generatedMRfilePath]["generatedMRClassFQN"]; Name_targetCUTClass =FullyQuilfiedName_targetCUTClass.split(".")[-1]
        FullyQuilfiedName_prefix = ".".join(FullyQuilfiedName_targetCUTClass.split(".")[:-1])
        
        DIR_POJ_SRC =  generatedMRfilePath.split("src")[0] +'src'
        Dir_ClassPath = f".:{PATH_PITEST_JAR}:{PATH_PITEST_CMD_JAR}:{PATH_PITEST_ENTRY_JAR}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}:{PATH_PITEST_JUNIT5_PLUGIN_JAR}:{MRgenerator_Randoop.Randoop_output_relative_dir}:{all_poj_class_dir_str}"
        PATH_JAVA = compile_java_poj.get_jdk_path(poj_meta.jdk_version)

        # list of testClasses to run PIT
        FullyQuilfiedName_TestForCUTs = [
            f"{Name_targetAutoMRClass}{MRgenerator_Randoop.Regression_test_basename_str}0", 
            FullyQuilfiedName_targetAutoMRClass.replace(config.TOOL_NAME,config.ORIGINAL_MRCASES),
            f"{Name_targetCUTClass}{MRgenerator_Randoop.Regression_test_basename_str}0"
            ] # AutoMRClassRegressionTests, ORIGINAL_MRCASES, Randoop tests4CUT
        for FullyQuilfiedName_TestForCUT in FullyQuilfiedName_TestForCUTs:
            Path_output_of_run_PIT_for_TestForCUT = DIR_PIT_OUTUT + FullyQuilfiedName_TestForCUT.split(".")[-1] + ".pit_log"
            
            if config.TOOL_NAME in FullyQuilfiedName_TestForCUT:
                Path_TargetRD4AutoMRTestFile_regression = f"{DIR_POJ}{MRgenerator_Randoop.Randoop_output_relative_dir}{Name_targetAutoMRClass}{MRgenerator_Randoop.Regression_test_basename_str}0.java" 
                path_of_TestForCUT = Path_TargetRD4AutoMRTestFile_regression
            elif config.ORIGINAL_MRCASES in FullyQuilfiedName_TestForCUT: # special 
                path_of_TestForCUT = generatedMRfilePath.replace(f"{config.TOOL_NAME}.java",f"{config.ORIGINAL_MRCASES}.java") # Problem of "/home1", to fix
            else:
                Path_TargetRD4CUTTestFile_regression = f"{DIR_POJ}{MRgenerator_Randoop.Randoop_output_relative_dir}{Name_targetCUTClass}{MRgenerator_Randoop.Regression_test_basename_str}0.java" 
                path_of_TestForCUT = Path_TargetRD4CUTTestFile_regression
            
            ## run pit
            CMD_RUN_PIT_res = -1
            if file_processing.pathExist(path_of_TestForCUT):
                # cd xxx ; java11 -cp .:randoop-tests/:./bytekit-demo-plugin/target/classes:./demo-agent/target/classes:./demo-plugin/target/classes:./dubbo-test-instrument/target/classes:./dubbo-test-plugin-common/target/classes:./dubbo-test-plugin/target/classes:./fastjson-demo-plugin/target/classes:./one-java-agent-plugin/target/classes:./one-java-agent-plugin/target/test-classes:./one-java-agent-spy/target/classes:./one-java-agent/target/classes:./one-java-agent/target/test-classes:/home1/  /software/pitest/pitest-1.8.0.jar:/home1/  /software/pitest/pitest-command-line-1.8.0.jar:/home1/  /software/pitest/pitest-entry-1.8.0.jar:/home1/  /software/junit/junit-4.13.2.jar:/home1/  /software/junit/junit-jupiter-api-5.8.2.jar:/home1/  /software/junit/hamcrest-core-1.3.jar org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir ./pit/ --targetClasses com.alibaba.oneagent.utils.FeatureCodec --targetTests FeatureCodecTest_test_AutoMRRegressionTest0 --sourceDirs ./one-java-agent-plugin/src --verbose true --dependencyDistance 2
                CMD_RUN_PIT = f"{CMD_CD_POJ_DIR} {PATH_JAVA} -XX:ActiveProcessorCount=50 -cp {Dir_ClassPath} org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir {DIR_PIT_OUTUT} --targetClasses {FullyQuilfiedName_targetCUT}  --targetTests {FullyQuilfiedName_TestForCUT} --sourceDirs {DIR_POJ_SRC} --verbose true --dependencyDistance 2 --testPlugin junit5 > {Path_output_of_run_PIT_for_TestForCUT}"
                os.system( f"touch {Path_output_of_run_PIT_for_TestForCUT}" )
                CMD_RUN_PIT_res = os.system( CMD_RUN_PIT )
                print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{poj}  cve_exe_cmd: {CMD_RUN_PIT_res}  CMD_RUN_PIT: {CMD_RUN_PIT}')
                pit_result = analyze_pit_exe_result(Path_output_of_run_PIT_for_TestForCUT)
            else:
                pit_result = "COIN: no such test file to run pit"
            # PIT_RESULT[FullyQuilfiedName_TestForCUT] = pit_result
            if FullyQuilfiedName_prefix not in FullyQuilfiedName_TestForCUT: FullyQuilfiedName_TestForCUT = f"{FullyQuilfiedName_prefix}.{FullyQuilfiedName_TestForCUT}"
            PIT_RESULT[FullyQuilfiedName_TestForCUT] = pit_result

            # TODO 
            if CMD_RUN_PIT_res==0:
                flag_PIT_runner_exe_successful = True
    json_processing.write( json_content=PIT_RESULT, path=PATH_PIT_RANDOOP_RESULT_JSON % poj)
    return flag_PIT_runner_exe_successful


def analyze_pit_exe_result(Path_output_of_pit_log):
    Path_output_of_csv_file = Path_output_of_pit_log.replace(".pit_log", ".csv")
    output_content = file_processing.read_TXTfile(path=Path_output_of_pit_log)
    """
    正则表达式： *: 可能为0次，+：至少一次
    r'Line Coverage: \d+/\d+'
    r'Generated \d+ mutations Killed \d+ '
    r'Mutations with no coverage \d+. Test strength [0-9.]*%'
    r'Ran \d+ tests \([0-9.]* tests per mutation\)'
    """
    if len( output_content ) < 40 or len( output_content.split("\n") ) < 2:
        return "COIN: len( pit log ) < 40. " + Path_output_of_pit_log

    # result = {"Line_Coverage":"", "Generated_mutations":0, "Killed_mutations":0, "Covered_mutations":0, "Mutation_score":0.0, "Mutants_coverage(covered/all)":0.0, "Mutations_with_no_coverage":0, "Test_strength":0,
    # "Num_of_test_cases":None, "MutantsAndStatus":{}}
    result = pit_result_item.copy()
    
    output_content_statistics = output_content.split("- Statistics")[-1]
    Line_Coverage_pattern = re.search(r'Line Coverage: \d+/\d+', output_content_statistics)
    # print("analyzing: Path_output_of_pit_log: ", Path_output_of_pit_log, )
    # print("analyzing: output_content: ", output_content)
    # print("analyzing: output_content_statistics: ", output_content_statistics)
    if not Line_Coverage_pattern:
        return "COIN: no Line Coverage in pit log. " + Path_output_of_pit_log
    Line_Coverage = re.findall( r'\d+/\d+', Line_Coverage_pattern.group() )[0]

    Generated_mutations_pattern = re.search(r'Generated \d+ mutations Killed \d+ ', output_content_statistics)
    Generated_mutations_num_str_list = re.findall( r'\d+', Generated_mutations_pattern.group() )
    Generated_mutations = int( Generated_mutations_num_str_list[0] )
    Killed_mutations = int( Generated_mutations_num_str_list[1] )

    Mutations_with_no_coverage_pattern = re.search(r'Mutations with no coverage \d+. Test strength [0-9.]*%', output_content_statistics)
    Mutations_with_no_coverage_str_list = re.findall( r'\d+', Mutations_with_no_coverage_pattern.group() )
    Mutations_with_no_coverage = int( Mutations_with_no_coverage_str_list[0] )

    Test_strength_pattern = re.search(r'Mutations with no coverage \d+. Test strength [0-9.]*%', output_content_statistics)
    Test_strength = re.findall( r'[0-9.]*%', Test_strength_pattern.group() )[0]

    result["Line_Coverage"] = Line_Coverage
    result["Line_Coverage_float"] = float(Line_Coverage.split("/")[0]) / float(Line_Coverage.split("/")[1]) 
    result["Generated_mutations"] = Generated_mutations
    result["Killed_mutations"] = Killed_mutations
    if Generated_mutations > 0:
        result["Mutation_score"] = Killed_mutations / Generated_mutations
    result["Mutations_with_no_coverage"] = Mutations_with_no_coverage
    result["Test_strength"] = Test_strength
    result["Test_strength_float"] = float(Test_strength.split("%")[0]) / 100 
    # killed_MutationIdentifiers, MutationIdentifiers = collect_killed_mutants(pit_log_path = Path_output_of_pit_log)
    # result["MutantsAndStatus"] = MutationIdentifiers
    killed_mutants = [].copy()
    covered_mutants = [].copy()
    survived_mutants = [].copy()
    if file_processing.pathExist(Path_output_of_csv_file):
        killed_mutants_count = 0
        survived_mutants_count = 0
        print("Path_output_of_csv_file: ", Path_output_of_csv_file)
        with open(Path_output_of_csv_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            row_index = 0
            for row in reader:
                mutant_id = config.SPLITE_STR.join(row[0:5]) + config.SPLITE_STR + str(row_index)
                if len(row)<6: continue
                if row[5] == 'KILLED':
                    killed_mutants_count += 1
                    killed_mutants.append(mutant_id) 
                elif row[5] == 'SURVIVED':
                    survived_mutants_count += 1
                    survived_mutants.append(mutant_id) 
                row_index += 1
        covered_mutants_count = killed_mutants_count + survived_mutants_count
        covered_mutants = killed_mutants + survived_mutants
        result["Covered_mutations"] = covered_mutants_count
        if Generated_mutations > 0:
            result["Mutants_coverage(covered/all)"] = covered_mutants_count / Generated_mutations        
            # result["Mutants_coverage(covered/all)"] # "MutantsAndStatus":{"killedMutants":[], "CoveredMutants":[]}}
            result["killedMutants"] = killed_mutants
            result["CoveredMutants"] = covered_mutants

    # 读取test EXE 结果，获取test cases的个数
    # PATH_OF_EXE_RESULT = PATH_AUTOMR_TESTS_EXE_JSON % poj
    # PATH_OF_EXE_RESULT = Path_output_of_pit_log.split("/pit/")[0] + "/AutoMRTestExecutionResult.json"
    pojname = Path_output_of_pit_log.split("/pit/")[0].split("/")[-1]
    PATH_OF_EXE_RESULT = PATH_AUTOMR_RANDOOP_TESTS_EXE_JSON % pojname
    if file_processing.pathExist(PATH_OF_EXE_RESULT):
        EXE_RESULT = json_processing.read(PATH_OF_EXE_RESULT)

        test_class_name = Path_output_of_pit_log.split("/")[-1].split(".")[0]
        for test_file in EXE_RESULT:
            if test_class_name.replace("_Green","") in test_file:
                num_of_passed_test_cases = EXE_RESULT[test_file]["num_of_passed_test_cases"]
                result["Num_of_test_cases"] = num_of_passed_test_cases
                break
            # # 暂时originalTestSuites不在EXE result中， 先特殊处理下，冲test file中识别
            # elif "original" in test_class_name.lower():# 该输入path_of_TestForCUT，应该就是：originalTestSuites
            #     Path_of_original_test_file = path_of_TestForCUT
            #     content = file_processing.read_TXTfile(Path_of_original_test_file)
            #     test_method_num = len(content.split( "@Test" )) -1 # 数“@Test”的个数
            #     result["Num_of_test_cases"] = test_method_num
            # else:
            #     Path_of_original_test_file = path_of_TestForCUT
            #     content = file_processing.read_TXTfile(Path_of_original_test_file)
            #     test_method_num = len(content.split( "@Test" )) -1 # 数“@Test”的个数
            #     result["Num_of_test_cases"] = test_method_num
            else:
                result["Num_of_test_cases"] = -1
                
    print("analyze_pit_exe_result",Path_output_of_pit_log , result)
    return result

def get_statistics_of_mutation_socre(poj_list, collect_PIT_results_options="MR VS. O", path=""): 
    """ collect_PIT_results_options = "MR VS. O", "MR VS. O&ES"  """
    """ 涉及多少项目的多少test class，mutation socre 分别为多少 """

    ALL_PIT_RESULT = {}
    ALL_PIT_statistics = { "num_of_pojs" : 0,   "list_of_pojs" : [],
    "num_of_original_test_classes" : 0, "list_of_original_test_classes" : []
    }
    if "ES4CUT" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_avg"] = 0
        ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_avg"] = 0
    if "ES4MUT" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_4MUT_avg"] = 0
        ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_4MUT_avg"] = 0
    if "MR" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_AutoMR_ESTest_WOassertion_avg"] = 0
        ALL_PIT_statistics["Mutation_score_AutoMR_ESTest_WOassertion_avg"] = 0
    if "O" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_OriginalMRcases_Line_Coverage_avg"] = 0
        ALL_PIT_statistics["Mutation_score_OriginalMRcases_avg"] = 0

    for poj in poj_list:
        if not file_processing.pathExist(PATH_PIT_RESULT_JSON % poj): continue
        
        AutoMRProfile = json_processing.read( path= PATH_AUTOMR_PROFILE_JSON % poj )
        DIR_POJ = EXPERIMENTAL_POJS_DIR + poj +'/'
        PIT_RESULT = json_processing.read(PATH_PIT_RESULT_JSON % poj)
        ALL_PIT_RESULT[poj] = {}

        DIR_POJ = EXPERIMENTAL_POJS_DIR + poj +'/'
        DIR_PIT_OUTUT = DIR_POJ + "pit/"
        
        
        """ 1 get original test class list """ 
        original_test_class_list = []
        for key in PIT_RESULT.keys():
            if "_OriginalMRcases" in key:
                original_test_class_list.append( key.split("_OriginalMRcases")[0] )
        """ 1.1 get CUTs of original test class list """
        for originalTestclass_FQN in original_test_class_list:
            for generatedAutoMRfile in AutoMRProfile.keys():
                if AutoMRProfile[generatedAutoMRfile]['generatedMRClassFQN']==originalTestclass_FQN + '_AutoMR':
                    CUT_of_originalTestclass_FQN_str = AutoMRProfile[generatedAutoMRfile]['ClassessUnderTest']
                    CUT_of_originalTestclass_FQN_list = list(set(CUT_of_originalTestclass_FQN_str.split(', ')))
                    CUT_of_originalTestclass_FQN = CUT_of_originalTestclass_FQN_list[0] # TODO, 针对多个数据时，暂时只取一个。。
            
            """ 1.3 CHECK availability of some options"""
            if not check_availability_of_optionalResults(collect_PIT_results_options, originalTestclass_FQN, CUT_of_originalTestclass_FQN, PIT_RESULT, poj): continue
            if len(PIT_RESULT.keys())>1: 
                # ALL_PIT_statistics["num_of_pojs"] += 1
                if poj not in ALL_PIT_statistics["list_of_pojs"]: ALL_PIT_statistics["list_of_pojs"].append(poj)



            ALL_PIT_RESULT[poj][originalTestclass_FQN] = {}
            ALL_PIT_statistics["num_of_original_test_classes"] += 1
            if originalTestclass_FQN not in  ALL_PIT_statistics["list_of_original_test_classes"]: ALL_PIT_statistics["list_of_original_test_classes"].append( originalTestclass_FQN )
            ESTest_killed_mutants = [];ESTest_4MUT_killed_mutants = [];AutoMR_killed_mutants=[];originalTest_killed_mutants=[];
            ESTest_all_mutants = [];ESTest_4MUT_all_mutants = [];AutoMR_all_mutants=[];originalTest_all_mutants=[];
            """ 2 get result items of collect_options="MR VS. orignial"... """
            if "ES4CUT" in collect_PIT_results_options:
                ESTest_Withassertion_key = CUT_of_originalTestclass_FQN + '_ESTestAll_Green'
                ESTest_Withassertion_item = PIT_RESULT[ ESTest_Withassertion_key]
                ESTest_Withassertion_Line_Coverage = calcuate_Line_Coverage( ESTest_Withassertion_item["Line_Coverage"] )
                ESTest_Withassertion_Mutation_score = ESTest_Withassertion_item["Mutation_score"]
                ESTest_Withassertion_Test_cases_Num = ESTest_Withassertion_item["Num_of_test_cases"]
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_Test_cases_Num"] = ESTest_Withassertion_Test_cases_Num
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_Line_Coverage"] = ESTest_Withassertion_Line_Coverage
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_Mutation_score"] = ESTest_Withassertion_Mutation_score
                Path_output_of_run_PIT_for_ESTest = DIR_PIT_OUTUT + ESTest_Withassertion_key.split(".")[-1] + ".pit_log"
                ESTest_killed_mutants, ESTest_all_mutants = collect_killed_mutants( Path_output_of_run_PIT_for_ESTest )
                ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_avg"] += ESTest_Withassertion_Line_Coverage
                ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_avg"] +=  ESTest_Withassertion_Mutation_score
            
            if "ES4MUT" in collect_PIT_results_options:
                ESTest_Withassertion_4MUT_key = CUT_of_originalTestclass_FQN + '_ESTestAll_only4MUTs_Green'
                ESTest_Withassertion_4MUT_item = PIT_RESULT[ ESTest_Withassertion_4MUT_key]
                ESTest_Withassertion_4MUT_Line_Coverage = calcuate_Line_Coverage( ESTest_Withassertion_4MUT_item["Line_Coverage"] )
                ESTest_Withassertion_4MUT_Mutation_score = ESTest_Withassertion_4MUT_item["Mutation_score"]
                ESTest_Withassertion_4MUT_Test_cases_Num = ESTest_Withassertion_4MUT_item["Num_of_test_cases"]
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_4MUT_Test_cases_Num"] = ESTest_Withassertion_4MUT_Test_cases_Num
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_4MUT_Line_Coverage"] = ESTest_Withassertion_4MUT_Line_Coverage
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["ESTest_Withassertion_4MUT_Mutation_score"] = ESTest_Withassertion_4MUT_Mutation_score
                Path_output_of_run_PIT_for_ESTest_4MUT = DIR_PIT_OUTUT + ESTest_Withassertion_4MUT_key.split(".")[-1] + ".pit_log"
                ESTest_4MUT_killed_mutants, ESTest_4MUT_all_mutants = collect_killed_mutants( Path_output_of_run_PIT_for_ESTest_4MUT )
                ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_4MUT_avg"] += ESTest_Withassertion_4MUT_Line_Coverage
                ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_4MUT_avg"] +=  ESTest_Withassertion_4MUT_Mutation_score
            
            
            if "MR" in collect_PIT_results_options:
                AutoMR_WOassertion_key = originalTestclass_FQN + '_AutoMR_ESTestWOAssertionAll_Green'
                AutoMR_ESTest_WOassertion_item = PIT_RESULT[AutoMR_WOassertion_key]
                AutoMR_ESTest_WOassertion_Line_Coverage = calcuate_Line_Coverage( AutoMR_ESTest_WOassertion_item["Line_Coverage"] )
                AutoMR_ESTest_WOassertion_Mutation_score = AutoMR_ESTest_WOassertion_item["Mutation_score"]
                AutoMR_ESTest_WOassertion_Test_cases_Num = AutoMR_ESTest_WOassertion_item["Num_of_test_cases"]
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["AutoMR_ESTest_WOassertion_Test_cases_Num"] = AutoMR_ESTest_WOassertion_Test_cases_Num
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["AutoMR_ESTest_WOassertion_Line_Coverage"] = AutoMR_ESTest_WOassertion_Line_Coverage
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["AutoMR_ESTest_WOassertion_Mutation_score"] = AutoMR_ESTest_WOassertion_Mutation_score
                Path_output_of_run_PIT_for_MRTest = DIR_PIT_OUTUT + AutoMR_WOassertion_key.split(".")[-1] + ".pit_log"
                AutoMR_killed_mutants, AutoMR_all_mutants = collect_killed_mutants( Path_output_of_run_PIT_for_MRTest )
                # if len(AutoMR_killed_mutants)==0: AutoMR_killed_mutants=None
                # ALL_PIT_RESULT[poj][originalTestclass_FQN]["AutoMR_killed_mutants"] = AutoMR_killed_mutants
                ALL_PIT_statistics["Line_Coverage_of_AutoMR_ESTest_WOassertion_avg"] += AutoMR_ESTest_WOassertion_Line_Coverage
                ALL_PIT_statistics["Mutation_score_AutoMR_ESTest_WOassertion_avg"] += AutoMR_ESTest_WOassertion_Mutation_score 
            
            
            if "O" in collect_PIT_results_options:
                OriginalMRcases_item = PIT_RESULT[originalTestclass_FQN + '_OriginalMRcases']
                OriginalMRcases_Line_Coverage = calcuate_Line_Coverage( OriginalMRcases_item["Line_Coverage"] )
                OriginalMRcases_Mutation_score = OriginalMRcases_item["Mutation_score"] 
                OriginalMRcases_Test_cases_Num = OriginalMRcases_item["Num_of_test_cases"]
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["OriginalMRcases_Test_cases_Num"] = OriginalMRcases_Test_cases_Num
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["OriginalMRcases_Line_Coverage"] = OriginalMRcases_Line_Coverage
                ALL_PIT_RESULT[poj][originalTestclass_FQN]["OriginalMRcases_Mutation_score"] = OriginalMRcases_Mutation_score
                Path_output_of_run_PIT_for_originalTest = DIR_PIT_OUTUT + (originalTestclass_FQN + '_OriginalMRcases').split(".")[-1] + ".pit_log"
                originalTest_killed_mutants, originalTest_all_mutants = collect_killed_mutants( Path_output_of_run_PIT_for_originalTest )
                ALL_PIT_statistics["Line_Coverage_of_OriginalMRcases_Line_Coverage_avg"] += OriginalMRcases_Line_Coverage 
                ALL_PIT_statistics["Mutation_score_OriginalMRcases_avg"] += OriginalMRcases_Mutation_score

            # if (OriginalMRcases_Line_Coverage) > 0:
            #     print(poj, originalTestclass_FQN, "(OriginalMRcases_Line_Coverage) > 0")
            MRkilled_addtional_mutants = set(AutoMR_killed_mutants).difference( set(originalTest_killed_mutants) ).difference( set(ESTest_killed_mutants) ).difference( set(ESTest_4MUT_killed_mutants) )
            all_killed_mutants = set(AutoMR_killed_mutants).union( set(originalTest_killed_mutants) ).union( set(ESTest_killed_mutants) ).union( set(ESTest_4MUT_killed_mutants) )
            ALL_PIT_RESULT[poj][originalTestclass_FQN]["AutoMR_killed_addtional_mutants"] = f'{len(MRkilled_addtional_mutants)} out of all killed {len(all_killed_mutants)} mutants'
            
            # check MRkilled_addtional_mutants 在其他test中是什么状态。。。
            # 测了几个, VS. ES都是survived
            # 测了几个, VS. original都是NON_VIABLE
            for addtional_mutant in MRkilled_addtional_mutants:
                # print(addtional_mutant)
                if addtional_mutant in ESTest_all_mutants:
                    print(addtional_mutant, 'status in ESTest', ESTest_all_mutants[addtional_mutant])
                if addtional_mutant in ESTest_4MUT_all_mutants:
                    print(addtional_mutant, 'status in ESTest_4MUT', ESTest_4MUT_all_mutants[addtional_mutant])
                if addtional_mutant in originalTest_all_mutants:
                    print(addtional_mutant, 'status in originalTest', originalTest_all_mutants[addtional_mutant])
                

    if "ES4CUT" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
        ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
    if "ES4MUT" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_ESTest_Withassertion_4MUT_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
        ALL_PIT_statistics["Mutation_score_ESTest_Withassertion_4MUT_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
    if "MR" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_AutoMR_ESTest_WOassertion_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
        ALL_PIT_statistics["Mutation_score_AutoMR_ESTest_WOassertion_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
    if "O" in collect_PIT_results_options:
        ALL_PIT_statistics["Line_Coverage_of_OriginalMRcases_Line_Coverage_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
        ALL_PIT_statistics["Mutation_score_OriginalMRcases_avg"] /= ALL_PIT_statistics["num_of_original_test_classes"]
    ALL_PIT_statistics["num_of_pojs"]  = len( ALL_PIT_statistics["list_of_pojs"] )
    
    keys = list(ALL_PIT_RESULT.keys()) # 删掉为空的poj
    for poj in keys:
        if len(ALL_PIT_RESULT[poj]) == 0:
            ALL_PIT_RESULT.pop(poj)

    print(ALL_PIT_statistics)
    print(list( ALL_PIT_RESULT.keys()))

    if path:
        json_processing.write( json_content=ALL_PIT_RESULT, path="ALL_PIT_RESULT.json" )
    print( json.dumps(ALL_PIT_RESULT, indent=4) )


def check_availability_of_optionalResults(collect_PIT_results_options, originalTestclass_FQN, CUT_of_originalTestclass_FQN, PIT_RESULT, poj):
    if "ES4CUT" in collect_PIT_results_options:
        ESTest_Withassertion_key = CUT_of_originalTestclass_FQN + '_ESTestAll_Green'
        if ESTest_Withassertion_key not in PIT_RESULT:
            print( "not in PIT_RESULT.." ,  poj, ESTest_Withassertion_key)
            return False
        ESTest_Withassertion_item = PIT_RESULT[ ESTest_Withassertion_key]
        if not isinstance(ESTest_Withassertion_item, dict):
            print( ESTest_Withassertion_item, poj, ESTest_Withassertion_key )
            return False
        ESTest_Withassertion_Line_Coverage = calcuate_Line_Coverage( ESTest_Withassertion_item["Line_Coverage"] )
        ESTest_Withassertion_Mutation_score = ESTest_Withassertion_item["Mutation_score"]
        if ESTest_Withassertion_Line_Coverage==0:
            print( "ESTest_Withassertion_Line_Coverage==0",  poj, ESTest_Withassertion_key )
            return False

    if "ES4MUT" in collect_PIT_results_options:
        ESTest_Withassertion_4MUT_key = CUT_of_originalTestclass_FQN + '_ESTestAll_only4MUTs_Green'
        if ESTest_Withassertion_4MUT_key not in PIT_RESULT:
            print( "not in PIT_RESULT.." ,  poj, ESTest_Withassertion_4MUT_key)
            return False
        ESTest_Withassertion_4MUT_item = PIT_RESULT[ ESTest_Withassertion_4MUT_key]
        if not isinstance(ESTest_Withassertion_4MUT_item, dict):
            print( ESTest_Withassertion_4MUT_item,  poj, ESTest_Withassertion_4MUT_key )
            return False
        ESTest_Withassertion_4MUT_Line_Coverage = calcuate_Line_Coverage( ESTest_Withassertion_4MUT_item["Line_Coverage"] )
        ESTest_Withassertion_4MUT_Mutation_score = ESTest_Withassertion_4MUT_item["Mutation_score"]
        if ESTest_Withassertion_4MUT_Line_Coverage==0:
            print( "ESTest_Withassertion_4MUT_Line_Coverage==0",  poj, ESTest_Withassertion_4MUT_key )
            return False
    
    
    if "MR" in collect_PIT_results_options:
        AutoMR_WOassertion_key = originalTestclass_FQN + '_AutoMR_ESTestWOAssertionAll_Green'
        AutoMR_ESTest_WOassertion_item = PIT_RESULT[AutoMR_WOassertion_key]
        if not isinstance(AutoMR_ESTest_WOassertion_item, dict):
            print( AutoMR_ESTest_WOassertion_item,  poj, AutoMR_WOassertion_key )
            return False
        AutoMR_ESTest_WOassertion_Line_Coverage = calcuate_Line_Coverage( AutoMR_ESTest_WOassertion_item["Line_Coverage"] )
        AutoMR_ESTest_WOassertion_Mutation_score = AutoMR_ESTest_WOassertion_item["Mutation_score"]
        if AutoMR_ESTest_WOassertion_Line_Coverage*AutoMR_ESTest_WOassertion_Mutation_score==0:
            print( "AutoMR_ESTest_WOassertion_Line_Coverage*AutoMR_ESTest_WOassertion_Mutation_score==0",  poj, AutoMR_WOassertion_key )
            return False
        

    if "O" in collect_PIT_results_options:
        OriginalMRcases_item = PIT_RESULT[originalTestclass_FQN + '_OriginalMRcases']
        if not isinstance(OriginalMRcases_item, dict):
            print( OriginalMRcases_item, poj,  originalTestclass_FQN + '_OriginalMRcases' )
            return False
        OriginalMRcases_Line_Coverage = calcuate_Line_Coverage( OriginalMRcases_item["Line_Coverage"] )
        OriginalMRcases_Mutation_score = OriginalMRcases_item["Mutation_score"] 
        if OriginalMRcases_Line_Coverage==0:
            print( "OriginalMRcases_Line_Coverage==0",  poj, originalTestclass_FQN + '_OriginalMRcases' )
            return False
        
    return True

def calcuate_Line_Coverage(Line_Coverage_str):
    return float( Line_Coverage_str.split('/')[0] ) / float( Line_Coverage_str.split('/')[1] )

def collect_killed_mutants(pit_log_path, consider_NON_VIABLE=False):
    pit_log_content = file_processing.read_TXTfile( pit_log_path )
    MutationIdentifiers = {}
    killed_MutationIdentifiers = []
    # stderr  : 5:57:45 PM PIT >> FINE : Mutation MutationIdentifier [location=Location [clazz=com.fizzed.rocker.runtime.PlainTextUnloadedClassLoader, method=size, methodDesc=()I], indexes=[6], mutator=org.pitest.mutationtest.engine.gregor.mutators.returns.PrimitiveReturnsMutator] detected = KILLED by [com.fizzed.rocker.runtime.PlainTextUnloadedClassLoader_ESTestAll_Green, com.fizzed.rocker.runtime.PlainTextUnloadedClassLoader_ESTestAll_Green, com.fizzed.rocker.runtime.PlainTextUnloadedClassLoader_ESTestAll_Green, com.fizzed.rocker.runtime.
    for line in pit_log_content.split("\n"):
        if "FINE : Mutation MutationIdentifier" in line: # 说明是记录信息的关键行
            MutationIdentifier = line.split(" detected = ")[0].split("MutationIdentifier ")[1] # “MutationIdentifier  xxxx  detected = ”中间部分
            status = line.split(" detected = ")[1].split(" [")[0]
            MutationIdentifiers[MutationIdentifier] = status
            if 'KILLED' in status or (consider_NON_VIABLE and 'NON_VIABLE' in status) : 
                killed_MutationIdentifiers.append(MutationIdentifier)
            if ('NON_VIABLE' in status):
                print( "'NON_VIABLE' in status: ", pit_log_path)
    return killed_MutationIdentifiers, MutationIdentifiers


# print( analyze_pit_exe_result("  TODO/data/AutoMR/projects/googleapis____google-http-java-client/pit/JsonWebSignature_ESTestFixedAmount_Green.pit_log") )

# PIT_runner()