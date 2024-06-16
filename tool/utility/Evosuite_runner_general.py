#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os,sys
import re
import os.path
import shutil
import tarfile
import time

_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing, json_processing, java_file_processing, compile_java_poj
import datetime

import config



PATH_EVOSUITE_JAR = config.PATH_EVOSUITE_JAR
PATH_ES_RUNTIME_JAR = config.PATH_ES_RUNTIME_JAR
PATH_JUNIT4_JAR = config.PATH_JUNIT4_JAR

PATH_JUNIT5_JAR = config.PATH_JUNIT5_JAR
PATH_HAMCREST_CORE_JAR = config.PATH_HAMCREST_CORE_JAR
PATH_JUNIT5_STANDALONE_JAR = config.PATH_JUNIT5_STANDALONE_JAR
JUNIT_JARS_CP_str = f"{PATH_JUNIT4_JAR}:{PATH_JUNIT5_JAR}:{PATH_HAMCREST_CORE_JAR}"

PATH_JAVA_11 = config.PATH_JAVA_11
PATH_JAVA = PATH_JAVA_11
PATH_JAVAC = f"{PATH_JAVA}c" # be careful: all the tests are generated, and compiled by Java 11. May some problems occurs。。。

addManualDependency = f"{config.DEPDENCY_MANUAL}*"

# max_iteration_Evo = 100

class evoConfig: # 2023.02.13 暂时废弃
    null_probability = 0.1
    catch_undeclared_exceptions = False

    POJ_NAMR = ""
    CMD_CD = ""
    TARGET_CLASS = ""
    CLASS_PATHS = ""
    GENERATED_TEST_FILE_PATH = ""


# todo: 下一轮：根据 Inputtrans需要，定制化输入就行；
# 然后，把中间的todo都理顺就好。 就可以跑一跑玩起来了。
# 先跑通，再重构！
def generally_generate_fixed_amountORiteration_test_cases(poj_build_tool, test_amount, max_iteration_Evo, TASK_POJ_NAMR, CMD_CD, PATH_JAVA, TARGET_CLASS, CP_jar_path, DIR_POJ, Generated_ES_TEST_DIR, suffix_single_test, suffix_merged_tests, withoutAssertion=False, overWriteExistingTestFile=False, PATH_JAVAC=PATH_JAVAC):
    """
    PATH_JAVA: for run EvoSuite
    PATH_JAVAC: for compile EvoSuite generated test cases
    """
    # poj_build_tool,test_amount, max_iteration_Evo, withoutException, POJ_NAMR,CMD_CD, PATH_JAVA, PATH_EVOSUITE_JAR, TARGET_CLASS, CLASS_PATHS, withoutAssertion=False, overWriteExistingTestFile=False
     # init: path setting
    POJ_NAMR = TASK_POJ_NAMR
    class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
    all_class_dir_str = (":").join( class_dir_list )
    CLASS_PATHS = f"{Generated_ES_TEST_DIR}:{all_class_dir_str}:{CP_jar_path}"
    Path_generatedESTestFile = Generated_ES_TEST_DIR + TARGET_CLASS.replace(".","/") + f"{suffix_single_test}.java"
    GENERATED_TEST_FILE_PATH = Path_generatedESTestFile

    # init
    i_execution = -1
    amount_of_tests = 0
    merged_test_file_path = ""
    merged_failedtest_file_path = ""
    withGeneratedTests = False
    withFixedAmountTests = False
    """stopping condition:
        1. amount_of_tests < test_amount
        2. i_execution>=max_iteration_Evo
    """
    while amount_of_tests < test_amount and i_execution<max_iteration_Evo:
        # # stop condition
        # if(i_execution>=max_iteration_Evo): break

        i_execution += 1 
        print("LOG: i_execution:", i_execution, "amount_of_tests: ", amount_of_tests, "TARGET_CLASS: ", TARGET_CLASS)
        renamedPath_generatedESTestFile = get_renamed_EStest_file_path(i_execution, TARGET_CLASS, Path_generatedESTestFile, suffix=suffix_single_test, withoutAssertion=withoutAssertion) # Path_renamed_generatedESTestFile_i_execution
        # print("renamedPath_generatedESTestFile: " , renamedPath_generatedESTestFile)
        # renamedPath_generatedFailedESTestFile =  renamedPath_generatedESTestFile.replace("_ESTest", "_Failed_ESTest") # 
        # print("renamedPath_generatedFailedESTestFile: " , renamedPath_generatedFailedESTestFile) 

        if not file_processing.pathExist(renamedPath_generatedESTestFile): # 该i_execution文件不存在时，再重新生成。
            """ 1. run evo """
            i_seed = hash(str(i_execution))
            res_CMD_RUN_EVOSUITE_WITHOUT_ASSERTIONS = CMD_RUN_EVOSUITE_to_generate_test_cases_general(POJ_NAMR,CMD_CD, PATH_JAVA, PATH_EVOSUITE_JAR, TARGET_CLASS, CLASS_PATHS, i_seed, GENERATED_TEST_FILE_PATH, withoutAssertion=withoutAssertion, suffix_single_test=suffix_single_test)
            if not res_CMD_RUN_EVOSUITE_WITHOUT_ASSERTIONS:
                print("ERROR: generated_fixed_amount_test_cases")
                return False

            """ 2. compilable """
            # EStest file
            Dir_ClassPath = f"{CLASS_PATHS}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}"

            CMD_COMPILE_EVOSUITE_GENERATED_TESTS_scaffolding = f"{CMD_CD} {PATH_JAVAC} {Path_generatedESTestFile.replace('.java','_scaffolding.java')} -cp .:{Dir_ClassPath}"
            CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res = os.system( CMD_COMPILE_EVOSUITE_GENERATED_TESTS_scaffolding )

            CMD_COMPILE_EVOSUITE_GENERATED_TESTS = f"{CMD_CD} {PATH_JAVAC} {Path_generatedESTestFile} -cp .:{Dir_ClassPath}"
            CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res = os.system( CMD_COMPILE_EVOSUITE_GENERATED_TESTS )
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{TASK_POJ_NAMR}  cve_exe_cmd: {CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res}  CMD_COMPILE_EVOSUITE_GENERATED_TESTS: {CMD_COMPILE_EVOSUITE_GENERATED_TESTS}')
            if CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res !=0: # ==0: 编译成功
                print("ERROR: CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res")
                # continue
            if CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res!=0:
                continue # todo : continue 干嘛？

            """ 3. [optional] withoutException test suite """
            # if withoutException:
            #     pass


            """ 5. seperate, check duplicate tests, merge to ALL file """
            if CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res==0:
                newPath_generatedESTestFile = rename_test_file(i_execution=i_execution, FullyQuilfiedNameOfClass=TARGET_CLASS, file_path=Path_generatedESTestFile,withoutAssertion=withoutAssertion,suffix_single_test=suffix_single_test)
                print("LOG: newPath_generatedESTestFile:", newPath_generatedESTestFile)
            # seperate/ todo: mv to the folder~ (或许：最后统一merge也是可以的～： 先创建folder/再mv)
            if CMD_COMPILE_EVOSUITE_GENERATED_TESTS_res==0:
                seperated_test_file_path = newPath_generatedESTestFile.replace(f"{i_execution}.java", f"_Sep{i_execution}.java")
                seperate_tests(original_test_file_path=newPath_generatedESTestFile, seperated_test_file_path=seperated_test_file_path)
                print("LOG: seperated_tests:", seperated_test_file_path)
        
        # merge file 
        seperated_tests = True
        check_duplicate_test_input = True
        merged_test_file_path =  merge_test_cases(i_execution, TARGET_CLASS, Path_generatedESTestFile, withoutAssertion=withoutAssertion, failed_test=False, check_duplicate_test_input=check_duplicate_test_input, seperated_tests=seperated_tests,suffix_single_test=suffix_single_test, suffix_merged_tests=suffix_merged_tests)
        print("LOG: merged_test_file_path:", merged_test_file_path)
        # 注意下: 名字别改！

        # check test case num
        EStest_methods = []; FailedEStest_methods = []
        if merged_test_file_path:
            EStest_content = file_processing.read_TXTfile(merged_test_file_path)
            EStest_methods = re.findall(r'public void test[0-9_a-zA-Z]', EStest_content)
        amount_of_tests = len( EStest_methods ) + len(FailedEStest_methods)
        print("LOG: amount_of_tests:", amount_of_tests, f"EStest_methods: {len( EStest_methods )} + FailedEStest_methods: {len( FailedEStest_methods )}")
        if amount_of_tests>0:
            withGeneratedTests = True
        if amount_of_tests >= test_amount:
            withFixedAmountTests = True
    
    if not withGeneratedTests:
        return False
    # merge EStest + Failed_EStest -> fixed amount test file
    """ compile fixedAmount test file """
    ESfixedAmount_file_path = merged_test_file_path
    print("### step2-ES(sub): compile fixedAmount test file ###")
    Dir_ClassPath = f"{CLASS_PATHS}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}"
    CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS = f"{CMD_CD} {PATH_JAVAC} {ESfixedAmount_file_path} -cp .:{Dir_ClassPath}:{addManualDependency}"
    CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS_res = os.system( CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{TASK_POJ_NAMR}  cve_exe_cmd: {CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS_res}  CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS: {CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS}')

    # clean: move _sep cases into folder
    print("ESfixedAmount_file_path: ", ESfixedAmount_file_path)
    DIR_generated_seperate_tests_folder = ESfixedAmount_file_path.replace(".java","/")
    print("DIR_generated_seperate_tests_folder: ", DIR_generated_seperate_tests_folder)
    file_processing.creatFolder_IfExistPass(DIR_generated_seperate_tests_folder)
    while i_execution>=0:
        newPath_generatedESTestFile = Path_generatedESTestFile.replace(".java" ,f"{i_execution}.java" )
        seperated_test_file_path = newPath_generatedESTestFile.replace(f"{i_execution}.java", f"_Sep{i_execution}.java")
        i_execution -= 1
        file_processing.moveFile(newPath_generatedESTestFile,DIR_generated_seperate_tests_folder+newPath_generatedESTestFile.split("/")[-1])
        file_processing.moveFile(seperated_test_file_path,DIR_generated_seperate_tests_folder+seperated_test_file_path.split("/")[-1])


    if CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS_res==0:
        return True
    return False


def compile_test_class(poj_build_tool, TASK_POJ_NAMR, CMD_CD, CP_jar_path, DIR_POJ, Generated_ES_TEST_DIR, Path_TestFile_to_compile):
    class_dir_list = java_file_processing.get_all_class_relative_path(dir=DIR_POJ, include_test_classes=True, poj_build_tool=poj_build_tool)
    all_class_dir_str = (":").join( class_dir_list )
    CLASS_PATHS = f"{Generated_ES_TEST_DIR}:{all_class_dir_str}:{CP_jar_path}"
    Dir_ClassPath = f"{CLASS_PATHS}:{PATH_ES_RUNTIME_JAR}:{PATH_JUNIT4_JAR}"
    CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS = f"{CMD_CD} {PATH_JAVAC} {Path_TestFile_to_compile} -cp .:{Dir_ClassPath}"
    CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS_res = os.system( CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS )
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{TASK_POJ_NAMR}  cve_exe_cmd: {CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS_res}  CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS: {CMD_COMPILE_EVOSUITE_GENERATED_FIXEDAMOUNT_TESTS}')




def CMD_RUN_EVOSUITE_to_generate_test_cases_general(POJ_NAMR,CMD_CD, PATH_JAVA, PATH_EVOSUITE_JAR, TARGET_CLASS, CLASS_PATHS, i_seed, GENERATED_TEST_FILE_PATH, withoutAssertion=False,checkConstract=False, alg="DYNAMOSA",suffix_single_test="_ESTest"):
    """ checkConstract = True: 生成Failed tests 
        alg=RANDOM_SEARCH
    """
    # init
    GENERATED_TEST_FILE_DIR = GENERATED_TEST_FILE_PATH[:GENERATED_TEST_FILE_PATH.rfind(TARGET_CLASS.replace(".","/"))]
    Assertion = not withoutAssertion

    # -Xms2048m -Xmx4096m -XX:ActiveProcessorCount=10
    CMD_RUN_EVOSUITE = f"{CMD_CD} {PATH_JAVA} -XX:ActiveProcessorCount=10 -jar {PATH_EVOSUITE_JAR} -class {TARGET_CLASS} -projectCP ./:{CLASS_PATHS}  -generateSuite -seed {i_seed} -Dnull_probability=0.1 -Dcatch_undeclared_exceptions=false -Dminimize=false -Dcriterion=LINE:BRANCH:WEAKMUTATION -Dstop_zero=false -Ddse_stopping_condition=MAXTESTS -Dstopping_condition=MAXTESTS -Dnum_tests=10 -Drandom_tests=10 -Dlog.level=OFF -Dshow_progress=false  -Dassertions={Assertion}\
    -Dtest_dir={GENERATED_TEST_FILE_DIR}\
    -Djunit_suffix={suffix_single_test}" # -Dalgorithm={alg} -Dcheck_contracts=true
    CMD_RUN_EVOSUITE_res = os.system( CMD_RUN_EVOSUITE )

    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{POJ_NAMR}  cve_exe_cmd: {CMD_RUN_EVOSUITE_res}  CMD_RUN_EVOSUITE: {CMD_RUN_EVOSUITE}')

    if checkConstract:
        GENERATED_FAILEDTEST_FILE_PATH = GENERATED_TEST_FILE_PATH.replace("_ESTest.java", "_Failed_ESTest.java")
        if not file_processing.pathExist(GENERATED_FAILEDTEST_FILE_PATH): 
            print( "ERROR: not file_processing.pathExist(GENERATED_FAILEDTEST_FILE_PATH)", GENERATED_FAILEDTEST_FILE_PATH )
            return False
    if not file_processing.pathExist(GENERATED_TEST_FILE_PATH): 
        print( "ERROR: not file_processing.pathExist(GENERATED_TEST_FILE_PATH)", GENERATED_TEST_FILE_PATH )
        return False
    return True



def seperate_tests(original_test_file_path, seperated_test_file_path):
    """ for a test case including multiple test inputs and invocations, seperate it!!!"""
    # 存入一个新文件   xxx10_Sep.java

    # 读取文件内容，修改内容中的class name, 判断test method是否保留，并重新输出到新文件中
    target_content = ''

    content = file_processing.read_TXTfile(path=original_test_file_path)
    content_lines = content.split( '\n')
    # 提取原文件头 content
    target_head_content = ""
    target_package_content = ""
    target_import_content = ""
    target_classDeclaration_content = ""
    for line in content_lines:
        if  line.startswith(" *") or line.startswith("/*"):
            target_head_content += line + '\n' 
        if "package " in line: # 说明是package声明部分
            target_package_content = line + '\n'
        if "import " in line: # 说明是import部分
            target_import_content += line + '\n'
        if "public class " in line: # 说明是class声明部分
            target_classDeclaration_content = line + '\n'
            break

    # 提取符合要求的test method部分
    target_body_content = ""
    sub_content_lines = content_lines
    toadd=False
    
    test_method_content_lines = []
    for line_index in range(len(sub_content_lines)):
        line = sub_content_lines[line_index]
        
        if "public void test" in line: # 说明是method声明的开始，判断是不是to add的内容(即是否重复了)
                toadd = True
                test_method_content_lines.append( sub_content_lines[line_index-1] )# 增加前一行@Test内容
        if toadd==True and (line.startswith("  @Test") or  line.startswith("}") ): # 说明是下一个 test method开始的标志,  or test file 结束的标志
            toadd=False

            # seperate and add methods
            seprated_new_test_cases_bodys = sperate_this_test_case(test_method_content_lines)
            if seprated_new_test_cases_bodys and len(seprated_new_test_cases_bodys)>0:
                for seprated_new_test_case_body in seprated_new_test_cases_bodys:
                    target_body_content += seprated_new_test_case_body+"\n"

            test_method_content_lines = []
        if toadd:
            test_method_content_lines.append( line )

    target_tail_content = "}"
    # merge
    target_content += target_head_content +'\n'
    target_content += target_package_content +'\n'
    target_content += target_import_content +'\n'
    target_content += target_classDeclaration_content +'\n'
    target_content += target_body_content +'\n'
    target_content += target_tail_content

    file_processing.write_TXTfile(path=seperated_test_file_path ,content=target_content )


def sperate_this_test_case(test_method_content_lines):
    seprated_new_test_cases_bodys = []

    """
    1. 明确：AutoMR method name
    2. find invocations
    3. 
    """

    """1. 明确：AutoMR method name"""
    test_method_content_body = ("\n").join( test_method_content_lines )
    matched_autoMR_invocations = re.findall(r'[.][0-9_a-zA-Z]*_AutoMR\(', test_method_content_body)
    if len(matched_autoMR_invocations)==0: # 无 AutoMR invocation
        return seprated_new_test_cases_bodys 
    if len(matched_autoMR_invocations)==1: # 不需拆分
        seprated_new_test_cases_bodys.append( test_method_content_body )
        return seprated_new_test_cases_bodys

    print("matched_autoMR_invocations",matched_autoMR_invocations)
    invokedAutoMRMethodName = matched_autoMR_invocations[0][1:-1] # .toExternalObject_whenLong_AutoMR( -> toExternalObject_whenLong_AutoMR

    kept_invocation_lines = []
    for invocation_to_keep_index in range(len(matched_autoMR_invocations)):
        # init
        cloned_method_content_lines = []
        invocation_index = -1
        kept_invocation_line = None
        # 
        for line in test_method_content_lines:
            new_line = line
            
            if "public void test" in line: # change test method name: test1() ->test10000X()
                test_method_name = re.findall(r'test[0-9_a-zA-Z]*\(', line)[0][:-1]
                if "_" in test_method_name:
                    new_test_method_name = test_method_name.split("_")[0] + "0000" + str(invocation_to_keep_index) +"_"+ test_method_name.split("_")[1] # test0_5()  -> test00000x_5()
                else: new_test_method_name = test_method_name + "0000" + str(invocation_to_keep_index)
                new_line = new_line.replace(test_method_name, new_test_method_name )

            if f".{invokedAutoMRMethodName}(" in line:
                invocation_index += 1
            if f".{invokedAutoMRMethodName}(" in line and invocation_index==invocation_to_keep_index:
                kept_invocation_line = new_line
            if f".{invokedAutoMRMethodName}(" in line and invocation_index!=invocation_to_keep_index:
                # new_line = "//" + new_line
                new_line = ""

            if new_line != "":
                cloned_method_content_lines.append(new_line)


        if kept_invocation_line and kept_invocation_line not in kept_invocation_lines:
            kept_invocation_lines.append(kept_invocation_line)
            seprated_new_test_cases_bodys.append( ("\n").join(cloned_method_content_lines) )
    
    return seprated_new_test_cases_bodys


def rename_test_file(i_execution, FullyQuilfiedNameOfClass, file_path, withoutAssertion=False, delete_original_file=False, failed_test=False,suffix_single_test="_ESTest"):
    # 有些时候，failed tests会没有的
    if failed_test and not file_processing.pathExist(file_path): return
    # minor bug: 有些时候，failed tests会没有，但上一次生成的failed tests还在，就会被误以为是当前的failing test。。
    # 有些时候，ES for CUT （not withoutAssertion）有时会没有
    if not withoutAssertion and not file_processing.pathExist(file_path): 
        print("LOG: no ES for CUT", file_path)
        return


    # 读取文件内容，修改内容中的class name + "{i_execution}"，修改test method name + "_{i_execution}", 并重新输出到新文件中
    # 删掉原文件(也可以不删。。。先留着，便于最后merge)

    # 读取文件内容，并重新输出到新文件中
    content = file_processing.read_TXTfile(path=file_path)
    class_name = FullyQuilfiedNameOfClass.split(".")[-1]
    if failed_test:
        ES_class_name_original = class_name+f"_Failed{suffix_single_test}"
    else:
        ES_class_name_original = class_name+f"{suffix_single_test}"
    # 修改内容中的class name + "{i_execution}"
    if withoutAssertion:
        ES_class_name_new = ES_class_name_original + "WOAssertion" + str(i_execution)
    else: 
        ES_class_name_new = ES_class_name_original + str(i_execution)
    content = content.replace( ' '+ ES_class_name_original + ' ', ' '+ ES_class_name_new + ' ' )
    # 修改test method name + "_{i_execution}"
    test_cases_num = len(content.split("public void test"))-1
    number_of_test_cases = 0
    while True:
        # 当cases 大于10时，命名是从“test00”开始
        if test_cases_num>10 and test_cases_num<100 and number_of_test_cases<10:
            number_of_test_cases_str = '0' + str(number_of_test_cases)
        # 大于100暂时就没处理了。。
        else:
            number_of_test_cases_str = str(number_of_test_cases)

        ES_testmethod_name_original = f"public void test{number_of_test_cases_str}()"
        ES_testmethod_name_new = f"public void test{number_of_test_cases_str}_{i_execution}()"
        if content.find(ES_testmethod_name_original) >-1:
            content = content.replace( ES_testmethod_name_original, ES_testmethod_name_new)
            number_of_test_cases += 1
        else: break # 说明遍历结束了。

    new_file_path = file_path.replace( ES_class_name_original , ES_class_name_new )
    file_processing.write_TXTfile(path=new_file_path ,content=content )

    # 删掉原文件
    if delete_original_file:
        file_processing.remove_file(path=file_path)
    
    return new_file_path


def get_renamed_EStest_file_path(i_execution, FullyQuilfiedNameOfClass, file_path, suffix="_ESTest" , withoutAssertion=False, delete_original_file=False, failed_test=False):
    class_name = FullyQuilfiedNameOfClass.split(".")[-1]
    if failed_test:
        ES_class_name_original = class_name+f"_Failed{suffix}"
    else:
        ES_class_name_original = class_name+f"{suffix}"
    # 修改内容中的class name + "{i_execution}"
    if withoutAssertion:
        ES_class_name_new = ES_class_name_original + "WOAssertion" + str(i_execution)
    else: 
        ES_class_name_new = ES_class_name_original + str(i_execution)

    new_file_path = file_path.replace( ES_class_name_original , ES_class_name_new )
    return new_file_path


def merge_test_cases(num_of_executions, FullyQuilfiedNameOfClass, target_file_path, withoutAssertion=False, failed_test=False, check_duplicate_test_input=False, seperated_tests=False, suffix_single_test="_ESTest", suffix_merged_tests="_ESTest"):
    # 有些时候，failed tests会没有的; ES for CUT （not withoutAssertion）有时也会没有
    if failed_test and not file_processing.pathExist(target_file_path): return
    # 有些时候，ES for CUT （not withoutAssertion）有时会没有
    if not withoutAssertion and not file_processing.pathExist(target_file_path): 
        print("LOG: no target_file_path for merge", target_file_path)
        return

    
    # 将target file中的所有方法替换为 零星文件中的所有方法即可。
    target_content = ''

    content = file_processing.read_TXTfile(path=target_file_path)
    content_lines = content.split( '\n')
    # 提取原文件头 content
    target_head_content = ""
    target_package_content = ""
    target_import_content = ""
    target_classDeclaration_content = ""
    for line in content_lines:
        if  line.startswith(" *") or line.startswith("/*"):
            target_head_content += line + '\n' 
        if "package " in line: # 说明是package声明部分
            target_package_content = line + '\n'
        if "import " in line: # 说明是import部分
            target_import_content += line + '\n'
        if "public class " in line: # 说明是class声明部分
            target_classDeclaration_content = line + '\n'
            break


    # 提取sub file的body部分
    target_body_content = ""
    class_name = FullyQuilfiedNameOfClass.split(".")[-1]
    if failed_test:
        ES_class_name_original = class_name+f"_Failed{suffix_single_test}"
    else:
        ES_class_name_original = class_name+f"{suffix_single_test}"
    for i_execution in range(num_of_executions):
        if withoutAssertion:
            if seperated_tests:
                ES_class_name_new = ES_class_name_original + "WOAssertion" + "_Sep" +str(i_execution)
            else:
                ES_class_name_new = ES_class_name_original + "WOAssertion" + str(i_execution)
        else: 
            ES_class_name_new = ES_class_name_original + str(i_execution)
        sub_file_path = target_file_path.replace( ES_class_name_original , ES_class_name_new )
        # if (failed_test or not withoutAssertion) and not file_processing.pathExist(sub_file_path): continue # 有些时候，failed tests会没有的
        if not file_processing.pathExist(sub_file_path): 
            print("INFO, no ES generated file: ", sub_file_path)
            continue # 有些时候 tests会没有的

        sub_content = file_processing.read_TXTfile(path=sub_file_path)
        sub_content_lines = sub_content.split( '\n')

        """
        class_declaration_line = ''
        class_declaration_end_index = sub_content.rindex("}")
        for line in sub_content_lines:
            if "public class " in line: # 说明是class声明部分
                class_declaration_line = line
                break
        if class_declaration_line == '' or class_declaration_end_index<0: print("Sth wrong: class_declaration_line == '' or class_declaration_end_line==''")
        sub_body_content = sub_content[:class_declaration_end_index].split(class_declaration_line)[-1][:class_declaration_end_index]
        """

        sub_body_content_lines = []
        sub_body_content = ""
        # 遇到 sub_content method declaration后，判断下target_body_content中是否有重复method，有的话就跳过（重复的method应该是 notGeneratedAnyTest ）
        toadd=False

        test_declaration_content_lines = []
        test_body_content_lines = []

        for line_index in range(len(sub_content_lines)):
            line = sub_content_lines[line_index]
            if "import " in line and line not in target_import_content: # 说明是import部分
                target_import_content += line + '\n'
            
            if "public void test" in line: # 说明是method声明的开始，判断是不是to add的内容(即,是否重复了)
                method_name = line.split('(')[0].split('public void ')[-1] # public void ....() 中间这部分
                if line not in target_body_content:# 未重复, 开始添加
                    toadd = True
                    # sub_body_content_lines.append( sub_content_lines[line_index-1] )# 增加前一行@Test内容
                    test_declaration_content_lines.append( sub_content_lines[line_index-1] )# 增加前一行@Test内容
                else:
                    print("WARNING: already in file", line)
            if toadd==True and (line.startswith("  @Test") or  line.startswith("}") ): # 说明是下一个 test method开始的标志,  or test file 结束的标志
                toadd=False
                if check_duplicate_test_input:
                    test_body_content_lines = test_declaration_content_lines[2:]
                    test_body_content = ('\n').join(test_body_content_lines)
                    if test_body_content in sub_body_content or test_body_content in target_body_content: # 重复了
                        test_declaration_content_lines = []
                sub_body_content += ('\n').join(test_declaration_content_lines) + "\n\n"
                test_declaration_content_lines = []

            if toadd:
                # sub_body_content_lines.append( line )
                test_declaration_content_lines.append( line )# 增加前一行@Test内容

        # sub_body_content = ('\n').join(sub_body_content_lines)

        # if withoutAssertion: # 说明是codified MR，判断下是否有codified MR method invocation
        #     # codified MR method name: original test method name + _AutoMR
        #     # FullyQuilfiedName_targetAutoMRClass
        #     class_name = FullyQuilfiedNameOfClass.split(".")[-1]
        #     codified_method_name = "_".join( class_name.split("_")[1:])
        #     method_invocation_str = f".{codified_method_name}"
        #     if not method_invocation_str in sub_body_content:
        #         sub_body_content = ""
        
        
        target_body_content += sub_body_content +'\n'
    
    target_tail_content = "}"
    # merge
    target_content += target_head_content +'\n'
    target_content += target_package_content +'\n'
    target_content += target_import_content +'\n'
    target_content += target_classDeclaration_content +'\n'
    target_content += target_body_content +'\n'
    target_content += target_tail_content

    if withoutAssertion:
        ES_class_name_new = ES_class_name_original + f"WOAssertion{suffix_merged_tests}"
    else: 
        ES_class_name_new = ES_class_name_original + f"{suffix_merged_tests}"
    target_content = target_content.replace( ' '+ ES_class_name_original + ' ', ' '+ ES_class_name_new + ' ' )
    target_file_path = target_file_path.replace( ES_class_name_original , ES_class_name_new )
    file_processing.write_TXTfile(path=target_file_path ,content=target_content )
    return target_file_path


def merge_fix_amount_inputs(ESTestAll_file_path, FailedESTestAll_file_path, FullyQuilfiedName_targetESTestAllClass, target_file_path, only_useful_tests=True, ESTest_exe_result=None, FailedESTestAll_exe_result=None, fixedAmount=-1):
    ESTestWOAssertionAll_exe_result=ESTest_exe_result
    ESTestWOAssertionAll_file_path=ESTestAll_file_path
    FailedESTestWOAssertionAll_exe_result=FailedESTestAll_exe_result
    FailedESTestWOAssertionAll_file_path=FailedESTestAll_file_path

    """
    1. get the useful test method names of ES and failedES & select first fixed amount of test cases

    for each method in ES:
    2. if useful: rename the ES test cases to $_ES, and add it
    for each method in failedES:
    3. if useful: rename the FailedES test cases to $_FailedES
    """

    
    # 1. get the useful test method names of ES and failedES 
    selected_ES_useful_method_names = []
    selected_failedES_useful_method_names = []
    if only_useful_tests:
        ES_useful_method_names = sorted(ESTestWOAssertionAll_exe_result["passed_test_cases_list"] + ESTestWOAssertionAll_exe_result["assertion_failed_test_cases_list"])
        failedES_useful_method_names = sorted(FailedESTestWOAssertionAll_exe_result["passed_test_cases_list"] + FailedESTestWOAssertionAll_exe_result["assertion_failed_test_cases_list"])

        if len(ES_useful_method_names) + len(failedES_useful_method_names)<fixed_amount_of_inputs4MR:
            print("ERROR: len(ES_useful_method_names) + len(failedES_useful_method_names)<fixed_amount_of_inputs4MR", ESTestWOAssertionAll_file_path)
            return
        
        iteration_num = 0
        while len(selected_ES_useful_method_names) + len(selected_failedES_useful_method_names) < fixed_amount_of_inputs4MR:
            for method_name in ES_useful_method_names:
                iteration_num_of_this_method = int(method_name.split("_")[-1])
                if iteration_num_of_this_method == iteration_num:
                    selected_ES_useful_method_names.append( method_name )
                    if len(selected_ES_useful_method_names) + len(selected_failedES_useful_method_names) == fixed_amount_of_inputs4MR: break
            for method_name in failedES_useful_method_names:
                iteration_num_of_this_method = int(method_name.split("_")[-1])
                if iteration_num_of_this_method == iteration_num:
                    selected_failedES_useful_method_names.append( method_name )
                    if len(selected_ES_useful_method_names) + len(selected_failedES_useful_method_names) == fixed_amount_of_inputs4MR: break
            iteration_num +=1
    


    # for each method in ES:
    # 2. if useful: rename the ES test cases to $_ES, and add it
    # for each method in failedES:
    # 3. if useful: rename the FailedES test cases to $_FailedES
    target_head_content = ""
    target_package_content = ""
    target_import_content = ""
    target_classDeclaration_content = ""
    Added_tests_amount = 0

    ESTestWOAssertionAll_content = file_processing.read_TXTfile(ESTestWOAssertionAll_file_path)
    content_lines = ESTestWOAssertionAll_content.split("\n")
    for line in content_lines:
        if  line.startswith(" *") or line.startswith("/*"):
            target_head_content += line + '\n' 
        if "package " in line: # 说明是package声明部分
            target_package_content = line + '\n'
        if "import " in line: # 说明是import部分
            target_import_content += line + '\n'
        if "public class " in line: # 说明是class声明部分
            target_classDeclaration_content = line + '\n'
            break

    target_body_content = ""

    for file_path in [ESTestWOAssertionAll_file_path, FailedESTestWOAssertionAll_file_path]:
        method_suffix_toadd = ""
        if file_path==ESTestWOAssertionAll_file_path: 
            method_suffix_toadd = "_ES"
            selected_useful_method_names = selected_ES_useful_method_names
        elif file_path==FailedESTestWOAssertionAll_file_path: 
            method_suffix_toadd = "_FailedES"
            selected_useful_method_names = selected_failedES_useful_method_names

        if file_path==None or not file_processing.pathExist(file_path): continue # because FailedESTestWOAssertionAll_file_path can be None, if not failed tests generated

        sub_content = file_processing.read_TXTfile(path=file_path)
        sub_content_lines = sub_content.split( '\n')

        sub_body_content_lines = []
        # 遇到 sub_content method declaration后，判断下target_body_content中是否有重复method，有的话就跳过（重复的method应该是 notGeneratedAnyTest ）
        toadd=False
        for line_index in range(len(sub_content_lines)):
            method_name = ''
            line = sub_content_lines[line_index]
            if "import " in line and line not in target_import_content: # 说明是import部分
                target_import_content += line + '\n'
            
            if "public void test" in line: # 说明是method声明的开始，判断是不是to add的内容(即是否重复了)
                method_name = line.split('(')[0].split('public void ')[-1] # public void ....() 中间这部分
                """ 添加 criteria """
                if (fixedAmount>-1 and Added_tests_amount>=fixedAmount) or (only_useful_tests and method_name not in selected_useful_method_names) :
                    pass # 不添加
                else: # 准备添加该tests
                    toadd = True
                    Added_tests_amount +=1
                    sub_body_content_lines.append( sub_content_lines[line_index-1] )# 增加前一行@Test内容
            if toadd==True and (line.startswith("  @Test") or  line.startswith("}") ): # 说明是下一个 test method开始的标志,  or test file 结束的标志
                toadd=False
            if toadd:
                sub_body_content_lines.append( line.replace( f"public void {method_name}", f"public void {method_name}{method_suffix_toadd}") ) # rename method name
        sub_body_content = ('\n').join(sub_body_content_lines)

        
        target_body_content += sub_body_content +'\n'
    
    target_tail_content = "}"

    class_name_original = FullyQuilfiedName_targetESTestAllClass.split(".")[-1]
    class_name_new = class_name_original[:-3] + "FixedAmount" # 把末尾的All去掉
    # merge
    target_content = ""
    target_content += target_head_content +'\n'
    target_content += target_package_content +'\n'
    target_content += target_import_content +'\n'
    target_content += target_classDeclaration_content.replace( class_name_original,class_name_new ) +'\n'
    target_content += target_body_content +'\n'
    target_content += target_tail_content



    # check
    while re.search(r'(_AutoMR){2,}', target_content):
        target_content = re.sub(r'(_AutoMR){2,}', "_AutoMR", target_content)
    # if "_AutoMR_AutoMR" in target_content:
    #     target_content.replace("_AutoMR_AutoMR","_AutoMR")

    file_processing.write_TXTfile(path=target_file_path ,content=target_content )



def get_size_of_the_fixedAmount_green_tests(AutoMRProfile, FQN_targetCUT, EXE_RESULT, DIR_POJ):
    """
    min_size = 1000000000000
    for all AutoMRs/CUT in the same CUT:
        if passed_test_cases_num>0 and passed_test_cases_num<min_size:
                    min_size = passed_test_cases_num
    """
    min_size = 1000000000000
    for generatedMRfilePath in AutoMRProfile.keys():
        FullyQuilfiedName_targetAutoMRClass = AutoMRProfile[generatedMRfilePath]["generatedMRClassFQN"]
        FullyQuilfiedName_targetCUT = AutoMRProfile[generatedMRfilePath]["ClassessUnderTest"]
        if FQN_targetCUT!= FullyQuilfiedName_targetCUT: # 说明不是这个CUT的
            continue

        GeneratedESTestFile_suffix_list = ["_ESTestFixedAmount", "_ESTestWOAssertionFixedAmount"]
        for GeneratedESTestFile_suffix in GeneratedESTestFile_suffix_list:
            if GeneratedESTestFile_suffix in ["_ESTestWOAssertionAll" ,"_Failed_ESTestWOAssertionAll", "_ESTestWOAssertionFixedAmount"]:
                Path_GeneratedESTestFile = DIR_POJ + "evosuite-tests/" + FullyQuilfiedName_targetAutoMRClass.replace(".","/") + f"{GeneratedESTestFile_suffix}.java"
                FullyQuilfiedName_targetESTestClass = FullyQuilfiedName_targetAutoMRClass+f"{GeneratedESTestFile_suffix}"
            elif GeneratedESTestFile_suffix in ["_ESTestAll", "_Failed_ESTestAll", "_ESTestAll_only4MUTs", "_ESTestFixedAmount"] :
                Path_GeneratedESTestFile = DIR_POJ + "evosuite-tests/" + FullyQuilfiedName_targetCUT.replace(".","/") + f"{GeneratedESTestFile_suffix}.java"
                FullyQuilfiedName_targetESTestClass = FullyQuilfiedName_targetCUT+f"{GeneratedESTestFile_suffix}"
            
            if FullyQuilfiedName_targetESTestClass in EXE_RESULT.keys():
                exe_result = EXE_RESULT[FullyQuilfiedName_targetESTestClass]            
                passed_test_cases_num = exe_result["num_of_passed_test_cases"]
            else:
                print(f"WARN: {FullyQuilfiedName_targetESTestClass} not in EXE_RESULT")
                passed_test_cases_num = -1

            if passed_test_cases_num>0 and passed_test_cases_num<min_size:
                min_size = passed_test_cases_num
    print("LOG: FQN_targetCUT",FQN_targetCUT, "min_size", min_size)
    return min_size


def get_passed_tests_names(FullyQuilfiedName, poj):
    passed_tests_names = []
    PATH_OF_EXE_RESULT = PATH_AUTOMR_TESTS_EXE_JSON % poj
    if not file_processing.pathExist(path=PATH_OF_EXE_RESULT):
        return passed_tests_names
    
    EXE_RESULT = json_processing.read(PATH_OF_EXE_RESULT)
    if FullyQuilfiedName in EXE_RESULT.keys():
        passed_tests_names = EXE_RESULT[FullyQuilfiedName]["passed_test_cases_list"]

    return passed_tests_names
            