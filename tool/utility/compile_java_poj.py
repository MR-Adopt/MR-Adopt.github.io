#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import os,sys
import os.path
import shutil
import tarfile
import time

_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing, json_processing

import config

import multiprocessing as mp

PATH_MVN = config.PATH_MVN
PATH_JAVA = config.PATH_JAVA

PATH_EVOSUITE_JAR = config.PATH_EVOSUITE_JAR
PATH_ES_RUNTIME_JAR = config.PATH_ES_RUNTIME_JAR
PATH_JUNIT4_JAR = config.PATH_JUNIT4_JAR
PATH_JUNIT5_JAR = config.PATH_JUNIT5_JAR
PATH_HAMCREST_CORE_JAR = config.PATH_HAMCREST_CORE_JAR
PATH_PITEST_JAR = config.PATH_PITEST_JAR
PATH_PITEST_CMD_JAR = config.PATH_PITEST_CMD_JAR
PATH_PITEST_ENTRY_JAR = config.PATH_PITEST_ENTRY_JAR

PATH_JAVAC_11 = config.PATH_JAVAC_11
PATH_JAVA_11 = config.PATH_JAVA_11
DIR_JAVA_11 = config.DIR_JAVA_11


PATH_JAVAC_8 = config.PATH_JAVAC_8
PATH_JAVA_8 = config.PATH_JAVA_8
DIR_JAVA_8 = config.DIR_JAVA_8
PATH_JAVAC_11 = config.PATH_JAVAC_11
PATH_JAVA_11 = config.PATH_JAVA_11
DIR_JAVA_11 = config.DIR_JAVA_11
PATH_JAVAC_13 = config.PATH_JAVAC_13
PATH_JAVA_13 = config.PATH_JAVA_13
DIR_JAVA_13 = config.DIR_JAVA_13
PATH_JAVAC_15 = config.PATH_JAVAC_15
PATH_JAVA_15 = config.PATH_JAVA_15
DIR_JAVA_15 = config.DIR_JAVA_15
PATH_JAVAC_17 = config.PATH_JAVAC_17
PATH_JAVA_17 = config.PATH_JAVA_17
DIR_JAVA_17 = config.DIR_JAVA_17
PATH_JAVAC_18 = config.PATH_JAVAC_18
PATH_JAVA_18 = config.PATH_JAVA_18
DIR_JAVA_18 = config.DIR_JAVA_18
PATH_JAVAC_19 = config.PATH_JAVAC_19
PATH_JAVA_19 = config.PATH_JAVA_19
DIR_JAVA_19 = config.DIR_JAVA_19
PATH_JAVAC_21 = config.PATH_JAVAC_21
PATH_JAVA_21 = config.PATH_JAVA_21
DIR_JAVA_21 = config.DIR_JAVA_21



PATH_GRADLE_7_4 = config.PATH_GRADLE_7_4
DIR_GRADLE_USER_HOME = config.DIR_GRADLE_USER_HOME
CMD_GRADLE_7_4_WITH_PARAMETERS = f"{PATH_GRADLE_7_4} -Dgradle.user.home={DIR_GRADLE_USER_HOME} -Dorg.gradle.java.home={DIR_JAVA_11}"


def get_jdk_path(int_jdk_version):
    DIR_JAVA = ""
    jdk_version = int_jdk_version
    if jdk_version==19: DIR_JAVA = DIR_JAVA_19
    elif jdk_version==18: DIR_JAVA = DIR_JAVA_18
    elif jdk_version==17: DIR_JAVA = DIR_JAVA_17
    elif jdk_version==11: DIR_JAVA = DIR_JAVA_11
    elif jdk_version==8: DIR_JAVA = DIR_JAVA_8 
    elif jdk_version==21: DIR_JAVA = DIR_JAVA_21
    elif jdk_version==13: DIR_JAVA = DIR_JAVA_13
    elif jdk_version==15: DIR_JAVA = DIR_JAVA_15
    PATH_JAVA = f"{DIR_JAVA}bin/java"       
    return PATH_JAVA

def get_jdkc_path(int_jdk_version):
    PATH_JAVA = get_jdk_path(int_jdk_version)
    PATH_JAVAC = f"{PATH_JAVA}c"
    return PATH_JAVAC

def compile(poj_dir, jdk_version, poj_build_tool, log_path):
    CMD_CD = f"cd {poj_dir} ;"
    if jdk_version==19: DIR_JAVA = DIR_JAVA_19
    elif jdk_version==18: DIR_JAVA = DIR_JAVA_18
    elif jdk_version==17: DIR_JAVA = DIR_JAVA_17
    elif jdk_version==11: DIR_JAVA = DIR_JAVA_11
    elif jdk_version==8: DIR_JAVA = DIR_JAVA_8 
    elif jdk_version==21: DIR_JAVA = DIR_JAVA_21  
    elif jdk_version==13: DIR_JAVA = DIR_JAVA_13
    elif jdk_version==15: DIR_JAVA = DIR_JAVA_15
    PATH_JAVA = f"{DIR_JAVA}bin/java"       
    PATH_JAVAC = f"{PATH_JAVA}c"


    """ 1. 编译项目，生成class文件  """
    if poj_build_tool.lower() == "maven":
        
        CMD_COMPILE = f"{CMD_CD} {PATH_MVN} clean install -DskipTests -Dcheckstyle.skip -Dlicense.skip=true -Dmaven.antrun.skip=true -Dmaven.compiler.fork=true -Dmaven.javadoc.skip=true -Dmaven.plugin.skip=true -Dmaven.compiler.executable={PATH_JAVAC} dependency:copy-dependencies"
    elif poj_build_tool.lower() == "gradle":
        
        CMD_COMPILE = f"{CMD_CD} {PATH_GRADLE_7_4} -Dgradle.user.home={DIR_GRADLE_USER_HOME} -Dorg.gradle.java.home={DIR_JAVA} build"
    CMD = f"{CMD_COMPILE} > {log_path} 2>&1 "
    CMD_COMPILE_res = os.system( CMD )
    print(CMD)
    # CMD_COMPILE_res = -1

    # print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), f'{poj}  cve_exe_cmd: {CMD_COMPILE_res}  CMD_COMPILE: {CMD_COMPILE}')
    if(CMD_COMPILE_res==0):
        print("### SUCCESS ###: CMD_COMPILE_res==0", CMD)
    else:
        print("### ERROR ###: CMD_COMPILE_res!=0", )
        # return flag_MRInputs_generator_with_Evosuite_exe_successful
    # time.sleep(5) # 停一下，等文件生成。
    
    if(CMD_COMPILE_res!=0):
        return False
    else:
        return True



def try_to_compile(poj, poj_dir, log_dir, compile_info_path, pass_compile_success = True, pass_already_failed_jdk = True, pass_already_successed_jdk=True): 
    """_summary_
        pass_compile_success: if True, then pass the compile if compile success before
        pass_already_failed_jdk: if True, then pass the compile if compile failed before
    """
    print("compiling: ", poj)
    # poj_dir = config.AUTOMR_EXPERIMENTAL_POJS4COMPILE_DIR + poj + "/"
    # log_dir = config.DIR__AUTOMR_COMPILE_LOG % poj; 
    # compile_info_path = config.PATH_AUTOMR_COMPILE_INFO % poj

    file_processing.creatFolder_IfExistPass(log_dir)
    
    # poj_build_tool = "gradle"
    compile_info = {
            "compile_success": False, #/True
            "build_tool" : [], #/ "gradle" or "maven&gradle"
            "maven_java_version_success" : [],
            "maven_java_version_failed":[],
            "gradle_java_version_success" : [],
            "gradle_java_version_failed":[]
        }
    
    if file_processing.pathExist(compile_info_path): compile_info = json_processing.read(compile_info_path)
    for poj_build_tool in ["maven","gradle"]:
        for jdk_version in [11,17,19,8,13,15,18,21]:
            log_path = f"{log_dir}compile_{poj_build_tool}_jdk_{jdk_version}.log"

            # condition
            if compile_info["compile_success"] and pass_compile_success:
                print("compile_success: ", poj);break;
            # elif (not compile_info["compile_success"]) and pass_already_failed_jdk and (jdk_version in compile_info[f"{poj_build_tool}_java_version_failed"]):
            elif pass_already_failed_jdk and (jdk_version in compile_info[f"{poj_build_tool}_java_version_failed"]):
                print("already_failed: ", poj, jdk_version);continue; 
            elif pass_already_successed_jdk and (jdk_version in compile_info[f"{poj_build_tool}_java_version_success"]):
                print("already_successed: ", poj, jdk_version);continue;
            else:
                # compile
                compile_result = compile(poj_dir, jdk_version, poj_build_tool, log_path)
                # writte compile result
                if compile_info["compile_success"]==False and compile_result:
                    compile_info["compile_success"] = compile_result
                if compile_result:
                    if poj_build_tool not in compile_info["build_tool"]:
                        compile_info["build_tool"].append(poj_build_tool)
                    if jdk_version not in compile_info[f"{poj_build_tool}_java_version_success"]: 
                        compile_info[f"{poj_build_tool}_java_version_success"].append(jdk_version)
                    if jdk_version in compile_info[f"{poj_build_tool}_java_version_failed"]:
                        compile_info[f"{poj_build_tool}_java_version_failed"].remove(jdk_version)
                else:
                    if jdk_version not in compile_info[f"{poj_build_tool}_java_version_failed"]:
                        compile_info[f"{poj_build_tool}_java_version_failed"].append(jdk_version)
                    if jdk_version in compile_info[f"{poj_build_tool}_java_version_success"]:
                        compile_info[f"{poj_build_tool}_java_version_success"].remove(jdk_version)
    json_processing.write(json_content=compile_info, path=compile_info_path)


def try_to_compile_s(task):
    print(f"try_to_compile_s task: {task}")
    try_to_compile(poj=task[0], poj_dir=task[1], log_dir=task[2], compile_info_path=task[3], pass_compile_success = task[4], pass_already_failed_jdk = task[5])

def parellel_try_to_compile(poj_list, poj_dir_dict, log_dir_dict, compile_info_path_dict, pass_compile_success = True, pass_already_failed_jdk = True):
    task_list = []
    for poj in poj_list:
        task_list.append( (poj, poj_dir_dict[poj], log_dir_dict[poj], compile_info_path_dict[poj], pass_compile_success, pass_already_failed_jdk) )
    
    task_list = list(set( task_list ))
    print("len(pojs_list): ", len(task_list))
    with mp.Pool(6) as p: # max: 10
        p.map( try_to_compile_s, task_list) 
