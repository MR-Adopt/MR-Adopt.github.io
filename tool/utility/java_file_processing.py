#!/usr/bin/env python
# encoding: utf-8
"""

Created on 2022/11/22
@Author :  

用于进行Java文件相关操作
"""
import os,sys
import os.path
import shutil
import tarfile
import time
import re

import json, os, sys
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing
import config


def get_all_class_path(dir, include_test_classes=False, poj_build_tool= "maven"):
    class_dir_list = []
    dir_list = file_processing.walk_allDirs(dir)
    if poj_build_tool.lower() == "maven":
        for dir_ in dir_list:
            if '/target/classes' in dir_:
                class_str = dir_.split("/target/classes")[0] + "/target/classes"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if include_test_classes and '/target/test-classes' in dir_ :
                class_str = dir_.split("/target/test-classes")[0] + "/target/test-classes"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
    elif poj_build_tool.lower() == "gradle":
        for dir_ in dir_list:
            if '/build/classes/java/main/' in dir_:
                class_str = dir_.split("/build/classes/java/main/")[0] + "/build/classes/java/main/"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if include_test_classes and '/build/classes/java/test/' in dir_ :
                class_str = dir_.split("/build/classes/java/test/")[0] + "/build/classes/java/test/"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )

    return class_dir_list


def get_all_class_relative_path(dir, include_test_classes=False, poj_build_tool= "maven", specific_dependency_folder=False):
    if specific_dependency_folder==False:
        specific_dependency_folder = dir
    class_dir_list = []
    dir_list = file_processing.walk_allDirs(dir)
    if poj_build_tool.lower() == "maven":
        for dir_ in dir_list:
            if '/target/dependency' in dir_ and specific_dependency_folder in dir_:
                class_str = dir_.split("/target/dependency")[0] + "/target/dependency/*"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if '/target/classes' in dir_:
                class_str = dir_.split("/target/classes")[0] + "/target/classes"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if include_test_classes and '/target/test-classes' in dir_ :
                class_str = dir_.split("/target/test-classes")[0] + "/target/test-classes"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
    elif poj_build_tool.lower() == "gradle":
        for dir_ in dir_list:
            if '/build/dependency/' in dir_ and specific_dependency_folder in dir_: # to modify
                class_str = dir_.split("/build/dependency/")[0] + "/build/dependency/*"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if '/build/classes/java/main/' in dir_:
                class_str = dir_.split("/build/classes/java/main/")[0] + "/build/classes/java/main/"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )
            if include_test_classes and '/build/classes/java/test/' in dir_ :
                class_str = dir_.split("/build/classes/java/test/")[0] + "/build/classes/java/test/"
                if class_str not in class_dir_list:
                    class_dir_list.append( class_str )

    class_relative_dir_list = []
    for ele in class_dir_list:
        if ele.startswith(dir):
            class_relative_dir_list.append( ele.replace(dir,"") )
        else:
            class_relative_dir_list.append( ele )
    return class_relative_dir_list


def analyze_test_exe_result(Path_output_of_run_Test, Path_Test_file=False, FullyQuilfiedName_targetAutoMRMethod=False, assertionLineNums=False, junit_type=4):
    if junit_type == 5:
        return analyze_junit5_test_results(Path_output_of_run_Test, Path_Test_file, FullyQuilfiedName_targetAutoMRMethod, assertionLineNums)

    all_test_method_name = []
    if Path_Test_file:
        if not file_processing.pathExist(Path_Test_file):
            print("ERROR: analyze_test_exe_result, test file does not exist: ", Path_Test_file)
        else:
            test_file_content = file_processing.read_TXTfile(path=Path_Test_file)
            # 针对：ES generated test cases
            all_test_method_list = re.findall(r'void test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', test_file_content)
            for test_method in all_test_method_list:
                test_method_name = re.findall(r'test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', test_method )[0].split('(')[0]
                all_test_method_name.append(test_method_name)
            # 针对：original developer written test cases
            if len(all_test_method_name) == 0:
                all_test_method_list = re.findall(r'void [0-9_a-zA-Z]*\(\)', test_file_content)
                for test_method in all_test_method_list:
                    test_method_name = re.findall(r'[0-9_a-zA-Z]*\(\)', test_method )[0].split('(')[0]
                    all_test_method_name.append(test_method_name)

            # check if the line with the test method name startswith("//"), discard
            for line in test_file_content.split("\n"):
                if " void " in line and "// " in line: #  说明，有可能是method declaration line
                    if line.strip().startswith("//"):
                        test_method_name = re.findall(r'[0-9_a-zA-Z]*\(\)', line )[0].split('(')[0]
                        all_test_method_name.remove(test_method_name)

    output_content = file_processing.read_TXTfile(path=Path_output_of_run_Test)
    """
    正则表达式： *: 可能为0次，+：至少一次
    r'There was [0-9]* failure:'
    r'[0-9]*\) test[0-9]*\([0-9a-zA-Z._]*\)'
    r'Tests run: [0-9]*,  Failures: [0-9]*'
    r'OK \([0-9]* tests\)'
    """

    result = {"num_of_test_cases":0, "num_of_passed_test_cases":0, "num_of_assertion_failed_test_cases":0, "num_of_exception_thrown_test_cases":0, "num_of_reach_assertion_test_cases":-1, "assertionLineNums":[],
    "reach_assertion_test_cases_list":[],
    "assertion_failed_test_cases_list":[], "exception_thrown_test_cases_list":[], "passed_test_cases_list":[], "failure_info":{}}
    # 针对testclass not found时
    if "Tests run: 1,  Failures: 1" in output_content and "java.lang.IllegalArgumentException: Could not find class" in output_content:
        return result
    # 针对无meaningful test inputs时 / 
    if "Tests run: 1,  Failures: 1" in output_content and "No runnable methods" in output_content:
        return result
    if 'Exception in thread "main" java.lang.' in output_content:
        return result
    if len(output_content.split('\n'))<5:
        return result
    
    # # 针对运行较慢的情况
    # if "OK" not in output_content and "Tests run: " not in output_content and len(output_content.split("\n"))==2:
    #     time.sleep(30);print("sleep 30s in analyze_test_exe_result")
    #     return analyze_test_exe_result(Path_output_of_run_Test, Path_Test_file)

    exception_thrown_test_cases_list = []
    assertion_failed_test_cases_list = []
    passed_test_cases_list = []
    reach_assertion_test_cases_list = []
    # 判断结果
    ok_pattern = re.compile(r'OK \([0-9]+ test[s]*\)')
    ok_pattern_res = ok_pattern.search(output_content)
    ok_pattern2 = re.compile(r'OK\[[a-zA-Z-@/ ]*\]#  \([0-9]+ test[s]*\)') # OK[runtime@skinny-dewey /]#  (1 test)
    ok_pattern2_res = ok_pattern2.search(output_content)
    if ok_pattern_res!=None or ok_pattern2_res!=None: # 就说明全通过啊
        # 解析数量。
        num_pattern_res = re.search(r'\d+', ok_pattern_res.group())
        num_of_test_cases = int( num_pattern_res.group() )
        num_of_failed_test_cases = 0
        failure_info = {}
        passed_test_cases_list = all_test_method_name
    else: #说明有没通过的哇，解析失败和成功的数量及 failed testname
        failure_pattern = re.compile(r'Tests run: [0-9]*,  Failures: [0-9]*')
        failure_pattern_res = failure_pattern.search(output_content) # search 只匹配第一个。。。
        if failure_pattern_res==None:
            print("ERROR: analyze_test_exe_result, no failure pattern found: ", Path_output_of_run_Test)
            return result
        # 解析数量。
        num_pattern_res_list = re.findall(r'\d+', failure_pattern_res.group()) # findall 匹配多个个。。。
        num_of_test_cases = int( num_pattern_res_list[0] )
        num_of_failed_test_cases = int( num_pattern_res_list[1] )
        # print( num_of_test_cases, num_of_failed_test_cases)
        failure_info = {}
        # previous: for ES test?
        failure_test_str_list = re.findall(r'[0-9]*\) test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', output_content)
        for failed_test in failure_test_str_list:
            test_method_name = re.findall(r'test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', failed_test )[0].split('(')[0]
            if test_method_name not in failure_info: failure_info[test_method_name] = test_method_name
        # for common test
        failure_test_str_list = re.findall(r'[0-9]*\) [0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', output_content)
        for failed_test in failure_test_str_list:
            test_method_name = re.findall(r'[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', failed_test )[0].split('(')[0]
            if test_method_name not in failure_info: failure_info[test_method_name] = test_method_name
        

        # calculate the exception types, line number
        lines = output_content.split("\n")
        for line_index in range(len(lines)):
            line = lines[line_index]
            if len(re.findall(r'[0-9]*\) test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', line ))>0: # 说明是 test log start line
                test_method_name = re.findall(r'test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', line )[0].split('(')[0]
                exception_message_line = lines[line_index+1]
                exception_message = exception_message_line.split(":")[0]
                
                # exception line number
                exception_line_number = None
                for potential_exception_info_line_index in range(line_index+1, len(lines)):
                    potential_exception_info_line = lines[potential_exception_info_line_index]
                    if len(re.findall(r'[0-9]*\) test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', potential_exception_info_line ))>0: # 说明是 test log start line; 到了下一个 test的结果
                        break
                    if FullyQuilfiedName_targetAutoMRMethod and (FullyQuilfiedName_targetAutoMRMethod in potential_exception_info_line and ".java" in potential_exception_info_line): # AutoMR method invocation line
                        exception_line_number = int(potential_exception_info_line.split(".java:")[1].split(")")[0])
                        break
                # at org.cornutum.tcases.util.ObjectUtilsTest_toExternalObject_whenDecimal_AutoMR.toExternalObject_whenDecimal_AutoMR(ObjectUtilsTest_toExternalObject_whenDecimal_AutoMR.java:15)

                # # identify reach assertion test case: 1. exception line number > max(assertion lines) OR 2. exception line number = someOne(assertion lines) , & assertionError
                # if exception_line_number:
                #     if exception_line_number > max(assertionLineNums) or (exception_line_number in assertionLineNums and exception_message in config.ASSERTION_FAILURE_LIST):
                #         reach_assertion_test_cases_list.append(test_method_name)
                # identify reach assertion test case: 2. exception line number = someOne(assertion lines) , & assertionError
                if exception_line_number:
                    # assertfailed
                    # if (exception_line_number in assertionLineNums and exception_message in config.ASSERTION_FAILURE_LIST):
                    if (exception_line_number <= max(assertionLineNums) and exception_message in config.ASSERTION_FAILURE_LIST): # 有的时候assertion会横跨几行，不能直接用 assertion line numbers 来匹配。。比如：  TODO/data/AutoMR/projects/jgitver__split__jgitver/src/test/java/fr/brouillard/oss/jgitver/VersionTest_can_parse_semver_AutoMR.java
                        reach_assertion_test_cases_list.append(test_method_name)
                
                # store info
                if exception_message in config.ASSERTION_FAILURE_LIST:
                    assertion_failed_test_cases_list.append( test_method_name )
                failure_info[test_method_name] = f"{exception_message}, line:{exception_line_number}" # to update
        
        passed_test_cases_list = [ ele for ele in all_test_method_name if ele not in failure_info.keys()]
        exception_thrown_test_cases_list = [ ele for ele in failure_info.keys() if ele not in assertion_failed_test_cases_list]
        reach_assertion_test_cases_list.extend(passed_test_cases_list)
        reach_assertion_test_cases_list = sorted(set(reach_assertion_test_cases_list))
    
    assertion_failed_test_cases_list = list( set(assertion_failed_test_cases_list) )
    exception_thrown_test_cases_list = list( set(exception_thrown_test_cases_list) )
    # result['num_of_test_cases']= num_of_test_cases 
    if num_of_test_cases < len(all_test_method_name):
        num_of_test_cases = len(all_test_method_name)
    result['num_of_test_cases']= num_of_test_cases
    result['num_of_assertion_failed_test_cases']= len(assertion_failed_test_cases_list) 
    result['num_of_exception_thrown_test_cases']= num_of_failed_test_cases - len(assertion_failed_test_cases_list)
    result['num_of_passed_test_cases']= num_of_test_cases - num_of_failed_test_cases 
    result['num_of_reach_assertion_test_cases']= len(reach_assertion_test_cases_list) 
    result['assertionLineNums']= assertionLineNums
    result['reach_assertion_test_cases_list']= reach_assertion_test_cases_list 
    result['assertion_failed_test_cases_list']= assertion_failed_test_cases_list 
    result['passed_test_cases_list']= passed_test_cases_list 
    result['exception_thrown_test_cases_list']= exception_thrown_test_cases_list 
    result['failure_info']= failure_info 
    return result

def analyze_junit5_test_results(Path_output_of_run_Test, Path_Test_file=False, FullyQuilfiedName_targetAutoMRMethod=False, assertionLineNums=False):
    output_content = file_processing.read_TXTfile(path=Path_output_of_run_Test)
    all_test_method_name = []
    if Path_Test_file:
        if not file_processing.pathExist(Path_Test_file):
            print("ERROR: analyze_test_exe_result, test file does not exist: ", Path_Test_file)
        else:
            test_file_content = file_processing.read_TXTfile(path=Path_Test_file)
            # 针对：ES generated test cases
            all_test_method_list = re.findall(r'void test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', test_file_content)
            for test_method in all_test_method_list:
                test_method_name = re.findall(r'test[0-9_a-zA-Z]*\([0-9a-zA-Z._]*\)', test_method )[0].split('(')[0]
                all_test_method_name.append(test_method_name)
            # 针对：original developer written test cases
            if len(all_test_method_name) == 0:
                all_test_method_list = re.findall(r'void [0-9_a-zA-Z]*\(\)', test_file_content)
                for test_method in all_test_method_list:
                    test_method_name = re.findall(r'[0-9_a-zA-Z]*\(\)', test_method )[0].split('(')[0]
                    all_test_method_name.append(test_method_name)
            # check if the line with the test method name startswith("//"), discard
            for line in test_file_content.split("\n"):
                if " void " in line and "// " in line: #  说明，有可能是method declaration line
                    if line.strip().startswith("//"):
                        test_method_name = re.findall(r'[0-9_a-zA-Z]*\(\)', line )[0].split('(')[0]
                        all_test_method_name.remove(test_method_name)

    result = {
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

    # Parse general test run info
    test_run_info_pattern = r'\[.*?\]'
    test_run_info_matches = re.findall(test_run_info_pattern, output_content)
    exe_result = {}
    for info in test_run_info_matches:
        # [         1 tests started         ]
        if " tests " not in info: continue
        value, tests, key = [s.strip() for s in info.strip('[]').strip(' ').split(' ')]
        if tests == "tests":
            exe_result[key] = int(value)

    # Update result with total tests and total successful tests
    result['num_of_test_cases'] = exe_result.get('found', 0)
    result['num_of_passed_test_cases'] = exe_result.get('successful', 0)
    # result['num_of_failed_test_cases'] = exe_result.get('failed', 0)

    # Parse failed tests
    failed_test_pattern = r'(JUnit\sJupiter:.+?\n\s+MethodSource.+\n\s+=>\s+.+)'
    failed_tests_matches = re.findall(failed_test_pattern, output_content)
    for failed_test in failed_tests_matches:
        """
        failed_test JUnit Jupiter:ExecutionTest:test_equals()
        MethodSource [className = 'com.github.kagkarlsson.scheduler.ExecutionTest', methodName = 'test_equals', methodParameterTypes = '']
        => org.opentest4j.AssertionFailedError: expected: <1> but was: <2>
        """
        if "methodName = " not in failed_test: 
            print("ERROR: analyze_junit5_test_results", Path_output_of_run_Test,Path_Test_file)
            continue

        test_name = re.search(r"methodName = '([^']+)'" , failed_test).group(1)
        exception_message_line = re.search(r'=>\s(.+)', failed_test).group(1)
        exception_message = exception_message_line.split(":")[0]
        # print("exception_message", exception_message)
        if exception_message in config.ASSERTION_FAILURE_LIST:
            result['assertion_failed_test_cases_list'].append(test_name)
        else:
            result['exception_thrown_test_cases_list'].append(test_name)
        result['failure_info'][test_name] = exception_message_line

    # Determine passed tests
    result['passed_test_cases_list'] = [test for test in all_test_method_name if test not in result['assertion_failed_test_cases_list'] and test not in result['exception_thrown_test_cases_list']]

    result['num_of_assertion_failed_test_cases'] = len( result['assertion_failed_test_cases_list'] )
    result['num_of_exception_thrown_test_cases'] = len( result['exception_thrown_test_cases_list'] )

    return result



def find_asserts_in_java_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    assertionLines = {}
    for line_number, line in enumerate(lines, start=1):
        if 'assert' in line and not line.startswith("import ") :
            assertionLines[line_number] = line.strip()
            # print(f'Line {line_number}: {line.strip()}')
    return assertionLines


def find_class_file_path_by_methodFQS(poj_dir, method_fqs):
    # Step 1: Derive class name and relative path from method FQS
    FQN_method = method_fqs.split('(')[0]
    package_class_part = FQN_method.rsplit('.', 1)[0]
    relative_class_path = package_class_part.replace('.', '/') + '.java'
    # print(f"Relative class path: {relative_class_path}", package_class_part)
    parent_package_class_part = package_class_part.rsplit('.', 1)[0]
    parent_relative_class_path = parent_package_class_part.replace('.', '/') + '.java'
    # print(f"parent Relative class path: {parent_relative_class_path}", parent_package_class_part)

    found_file_path = ""
    # Step 2: Search for the Java file
    for root, dirs, files in os.walk(poj_dir):
        for file in files:
            if file.endswith(".java"):
                file_path = os.path.join(root, file)
                # Check if this file's path ends with the package path derived from FQS
                if file_path.endswith(relative_class_path):
                    found_file_path = file_path
                    return found_file_path  # Found the corresponding class file path
    if found_file_path=="": # may package_class_part is the subclass
        # Step 3: Search for the parenta Java file
        for root, dirs, files in os.walk(poj_dir):
            for file in files:
                if file.endswith(".java"):
                    file_path = os.path.join(root, file)
                    # Check if this file's path ends with the package path derived from FQS
                    if file_path.endswith(parent_relative_class_path):
                        found_file_path = file_path
                        return found_file_path  # Found the corresponding class file path
    
    return None  # If no file is found

# # Example usage: find_class_file_path_by_methodFQS
# poj_dir = "  TODO/data/ITrans/projects/datageartech__split__datagear/"
# method_fqs = "org.datagear.util.version.Version.valueOf(java.lang.String)"
# class_file_path = find_class_file_path_by_methodFQS(poj_dir, method_fqs)

# Example usage: find_class_file_path_by_methodFQS
# poj_dir = "  TODO/data/ITrans/projects/aws__split__event-ruler/"
# method_fqs = "software.amazon.event.ruler.SubRuleContext.Generator.generate(java.lang.Object)"
# class_file_path = find_class_file_path_by_methodFQS(poj_dir, method_fqs)

# if class_file_path:
#     print(f"Found class file at: {class_file_path}")
# else:
#     print("Class file not found.")



# result = analyze_test_exe_result("  TODO/data/AutoMR/projects/Stratio__split__cassandra-lucene-index/evosuite-tests/com/stratio/cassandra/lucene/search/sort/builder/GeoDistanceSortFieldBuilderTest_testJsonDefault_AutoMR_ESTestWOAssertionFixedAmount.exe_log", Path_Test_file=False)
# print(result)

# result = get_all_class_relative_path("  TODO/data/AutoMR/projects/Cornutum__split__tcases/", include_test_classes=False, poj_build_tool= "maven", specific_dependency_folder="  TODO/data/AutoMR/projects/Cornutum__split__tcases//tcases-lib")
# print(result)

# result = find_asserts_in_java_file("  TODO/data/AutoMR/projects/Cornutum__split__tcases/tcases-lib/src/test/java/org/cornutum/tcases/util/ObjectUtilsTest_toExternalObject_whenBoolean_AutoMR.java")
# print(result)

# result = analyze_test_exe_result('  TODO/data/AutoMR/projects/jgitver__split__jgitver/evosuite-tests/fr/brouillard/oss/jgitver/VersionTest_can_parse_semver_AutoMR_ESTestWOAssertionFixedAmount.exe_log','  TODO/data/AutoMR/projects/jgitver__split__jgitver/evosuite-tests/fr/brouillard/oss/jgitver/VersionTest_can_parse_semver_AutoMR_Failed_ESTestWOAssertionAll.java','fr.brouillard.oss.jgitver.VersionTest_can_parse_semver_AutoMR.can_parse_semver_AutoMR', [43, 45, 48, 50, 57, 58])

# result = analyze_test_exe_result('  TODO/data/ITrans/projects/datageartech__split__datagear/AutoMR/test_exe/w.org.datagear.util.version.VersionTest_isLowerThanTest_h0Test.log','  TODO/data/ITrans/projects/datageartech__split__datagear/ITrans/generated_inputs/w/org/datagear/util/version/VersionTest_isLowerThanTest_h0Test.java')
# print(result)