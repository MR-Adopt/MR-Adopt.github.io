#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
PROJECT_NAME = "InputTrans"

import socket
# HOST_NAME = socket.gethostname()
HOST_NAME = "localhost"
DIR_HOME = "./"
COFIG_DICT = {
    "localhost":{
        "DIR_DATA": f"{DIR_HOME}data/",
        "DIR_SOFTWARE":f"{DIR_HOME}/software/",
        "DIR_WORKPROJECTS": f"{DIR_HOME}/workProjects/",
        "PATH_JAVADEMO": f"{DIR_HOME}/software/demo_anony-1.0-SNAPSHOT-jar-with-dependencies.jar",
        "DIR_HOME": DIR_HOME
    }
}

DIR_HOME = COFIG_DICT[HOST_NAME]["DIR_HOME"]
DIR_DATA = COFIG_DICT[HOST_NAME]["DIR_DATA"]
DIR_SOFTWARE = COFIG_DICT[HOST_NAME]["DIR_SOFTWARE"]
DIR_WORKPROJECTS = COFIG_DICT[HOST_NAME]["DIR_WORKPROJECTS"]



AUTOMR_JAVA_DEMO_JAR_PATH = COFIG_DICT[HOST_NAME]["PATH_JAVADEMO"]
AUTOMR_JAVA_DEMO_JAR_PATH = f"{DIR_HOME}/software/demo_anony-1.0-SNAPSHOT-jar-with-dependencies.jar"
################################# Jar_HOME #################################
DIR_GRADLE_USER_HOME = DIR_HOME + ".gradle/"
DIR_MAVEN_USER_HOME = DIR_HOME + ".m2/"
DIR_MAVEN_M2_REPO_USER_HOME = DIR_HOME + ".m2/repository/"

################################# META DIR #################################
OUTPUT_DIR = f"{ROOT_DIR}/output/"
BENCHMARK_DIR = f"{ROOT_DIR}/inputtransdata/"
MVN_PATH = f"{DIR_SOFTWARE}/apache-maven-3.8.5/bin/mvn"

################################# NAME #################################
PACKAGE_NAME = "com.dataset"
PACKAGE_STATEMENT = "package com.dataset;"
PACKAGE_GT_STATEMENT = "package com.dataset.GT;"
GT_CLASS_SUFFIX = "_GT"
HARDCODED_CLASS_SUFFIX = "_h"
VALID_INPUT_CLASS_SUFFIX = "_valid"
JUNIT_STATEMENT = "import org.junit.Test;\nimport static org.junit.Assert.*;"


################################# TO DIR_DATA #################################
# ITrans data

ITRANS_CACHE_DIR = f"{DIR_DATA}ITrans/cache/"
ITRANS_CACHE_GENERATED_TRANS_DIR = f"{DIR_DATA}ITrans/cache/generateTrans/"
ITRANS_CACHE_GENERATED_INPUTS_DIR = f"{DIR_DATA}ITrans/cache/generateInputs/"


# ITrans in benchmark dir
FEW_SHOT_BASE_DIR = f"{ROOT_DIR}/data/few_shot_base/"
GT_ITRANS_WO_DIR = f"{ROOT_DIR}/data/GT_MTCs_wo_IT/processed_GT_only/"
GT_ITRANS_W_DIR = f"{ROOT_DIR}/data/GT_MTCs_w_IT/processed_GT_only/"

PROMPT_GENERATED_ITRANS_DIR = f"{ROOT_DIR}/cache/generated_ITrans/"

BENCHMARK_SRC_DIR = f"{BENCHMARK_DIR}/src/"
ES_GENERATED_TEST_DIR = f"{BENCHMARK_DIR}src/test/evosuite/"
ES_TEST_EXE_RESULT_DIR = f"{BENCHMARK_DIR}src/test/evosuite/exe_result/"

CRAFTED_MTC_IT_TEST_EXE_RESULT_DIR = f"{BENCHMARK_DIR}src/test/java/exe_result/"


DIR_ITRANS_COMPILE_LOG = DIR_DATA + "ITrans/projects/%s/AutoMR/compile/"
PATH_ITRANS_COMPILE_INFO = DIR_DATA + "ITrans/projects/%s/AutoMR/compile_info.json"
ITRANS_EXPERIMENTAL_POJS_DIR = DIR_DATA + "ITrans/projects/" 
ITRANS_EXPERIMENTAL_POJS4COMPILE_DIR = DIR_DATA + "ITrans/projects4compiling/"

# ITrans in origianl poj dir
ITRANS_PATH_PIT_RESULT_JSON = DIR_DATA + "ITrans/projects/%s/ITrans/PITResult.json"
ITRANS_FOLDER_NAME = "ITrans"
ITRANS_EXPERIMENTAL_POJS_DIR = DIR_DATA + "ITrans/projects/" 
ITRANS_EXPERIMENTAL_POJ_FOLDER_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/" 

ITRANS_RAW_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/raw/"
ITRANS_GT_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/processed_GT_only/"
ITRANS_MTCIT_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/processed_MTCITrans_only/"
ITRANS_GENERATED_IT_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/generated_ITrans/"
ITRANS_GENERATED_INPUTS_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/generated_inputs/"
ITRANS_GENERATED_LLMI_TEST_DIR = DIR_DATA + "ITrans/projects/%s/ITrans/generated_inputs/LLMI_test_Trans/"

ITRANS_EVOSUITE_TESTS_DIR = DIR_DATA + "ITrans/projects/%s/evosuite/"


## path
DEPDENCY_MANUAL = DIR_DATA + "AutoMR/manualDependcy/"
AUTOMR_EXPERIMENTAL_POJS_DIR = DIR_DATA + "AutoMR/projects/" 
AUTOMR_EXPERIMENTAL_POJS4COMPILE_DIR = DIR_DATA + "AutoMR/projects4compiling/"

AUTOMR_EXPERIMENTAL_POJS_MTIDENTIFIER_OUTPUT_DIR = DIR_DATA + "AutoMR/projects_MTidentifier_outputs/"
AUTOMR_EXPERIMENTAL_POJS_MTIDENTIFIER_RELATIONASSRTION_OUTPUT_DIR = DIR_DATA + "AutoMR/projects_MTidentifier_relationAssertion_outputs/"
AUTOMR_EXPERIMENTAL_POJS_MTIDENTIFIER_RELATIONASSRTION_OUTPUT_LOGS_DIR = DIR_DATA + "AutoMR/projects_MTidentifier_relationAssertion_outputs/LOGS/"
PATH_AUTOMR_ORIGINAL_TESTS_INFO = DIR_DATA + "AutoMR/projects/%s/AutoMR_original_tests_info.json"

PATH_AUTOMR_PROFILE_JSON = DIR_DATA + "AutoMR/projects/%s/AutoMR/AutoMRProfile.json"
PATH_UNSUCCESSFUL_GENRATED_AUTOMR = DIR_DATA + "AutoMR/projects/%s/AutoMR/UnsuccessfulGeneratedAutoMR.json"
PATH_AUTOMR_TESTS_EXE_JSON = DIR_DATA + "AutoMR/projects/%s/AutoMR/AutoMRTestExecutionResult.json"
PATH_AUTOMR_RANDOOP_TESTS_EXE_JSON = DIR_DATA + "AutoMR/projects/%s/AutoMR/AutoMRTestExecutionResultRandoop.json"
PATH_PIT_RESULT_JSON = DIR_DATA + "AutoMR/projects/%s/AutoMR/AutoMRPITResult.json"
PATH_PIT_RANDOOP_RESULT_JSON = DIR_DATA + "AutoMR/projects/%s/AutoMR/AutoMRPITResultRANDOOP.json"

DIR__AUTOMR_COMPILE_LOG = DIR_DATA + "AutoMR/projects/%s/AutoMR/compile/"
PATH_AUTOMR_COMPILE_LOG = DIR_DATA + "AutoMR/projects/%s/AutoMR/compile/compile_%s_jdk_%s.log"
PATH_AUTOMR_COMPILE_INFO = DIR_DATA + "AutoMR/projects/%s/AutoMR/compile_info.json"

## output
DIR_POJ_AUTOMR_OUTPUT_FOLDER = DIR_DATA + "AutoMR/projects/%s/AutoMR/"
DIR_MTIDENTIFIER_MRINSTSNCES = DIR_DATA + "AutoMR/projects/%s/AutoMR/MTidentifier/"


## split
## str
SPLITE_STR = "__split__"
TOOL_NAME = "AutoMR";
ORIGINAL_MRCASES = "OriginalMRcases";
UNSUCCESSFUL_CODIFED_MR_CONSTRUCTION = "UnsuccessfulCodifiedMRConstruction"






################################# TO DIR_WORKPROJECTS #################################

## clone_github_projects
PATH_EXPERIMENTAL_POJ_WITH_TESTS = DIR_WORKPROJECTS + "AutoMR/script/clone_github_projects/pojs_with_tests.json"
DIR_AUTOMR_DEMO_POJ = DIR_WORKPROJECTS + "AutoMR/Java/demo"
MTIDENTIFIER_OUTPUT_JSON_PATH = DIR_WORKPROJECTS + "AutoMR/script/run_MTidentifier/MTidentifier_result_on_8kPojs220529.json"
MTIDENTIFIER_SELECTED_OUTPUT_JSON_PATH = DIR_WORKPROJECTS + "AutoMR/script/run_MTidentifier/selected_MTidentifier_result_on_8kPojs220526.json"

################################# TO DIR_SOFTWARE #################################
# path or evosuite/randoop
RANDOOP431_JAR_PATH = DIR_SOFTWARE + "randoop/randoop-4.3.1/randoop-all-4.3.1.jar"
# PATH_EVOSUITE_JAR = DIR_SOFTWARE + "evosuite/evosuite-1.2.0.jar"
PATH_EVOSUITE_JAR = DIR_SOFTWARE + "evosuite/evosuite-master-1.2.1-SNAPSHOT.jar" # updated by hc
PATH_ES_RUNTIME_JAR = DIR_SOFTWARE + "evosuite/evosuite-standalone-runtime-1.2.0.jar"
PATH_JUNIT4_JAR =DIR_SOFTWARE + "junit/junit-4.13.2.jar"
PATH_JUNIT5_JAR =DIR_SOFTWARE + "junit/junit-jupiter-api-5.8.2.jar"
PATH_OPENTT4J_JAR = DIR_SOFTWARE + "junit/opentest4j-1.2.0.jar"
PATH_JUNIT5_STANDALONE_JAR =DIR_SOFTWARE + "junit/junit-platform-console-standalone-1.10.0.jar"
PATH_HAMCREST_CORE_JAR =DIR_SOFTWARE + "junit/hamcrest-core-1.3.jar"
PATH_PITEST_JAR =DIR_SOFTWARE + "pitest/pitest-1.8.0.jar"
PATH_PITEST_CMD_JAR =DIR_SOFTWARE + "pitest/pitest-command-line-1.8.0.jar"
PATH_PITEST_ENTRY_JAR =DIR_SOFTWARE + "pitest/pitest-entry-1.8.0.jar"
PATH_PITEST_JUNIT5_PLUGIN_JAR =DIR_SOFTWARE + "pitest/pitest-junit5-plugin-0.16.jar"

# path of java
PATH_MVN = DIR_SOFTWARE + "apache-maven-3.8.5/bin/mvn"
PATH_GRADLE_7_4 = DIR_SOFTWARE + "gradle/gradle-7.4/bin/gradle"
PATH_JAVA = DIR_SOFTWARE + "jdk1.8.0_131/bin/java"



# PATH_JAVAC_11 = DIR_SOFTWARE + "jdk11.0.2/jdk-11.0.2/bin/javac" 
# PATH_JAVA_11 = DIR_SOFTWARE + "jdk11.0.2/jdk-11.0.2/bin/java"
# DIR_JAVA_11 = DIR_SOFTWARE + "jdk11.0.2/jdk-11.0.2/"

# PATH_JAVAC_8 = DIR_SOFTWARE + "x86_jdks/jdk1.8.0_131/bin/javac" 
# PATH_JAVA_8 = DIR_SOFTWARE + "x86_jdks/jdk1.8.0_131/bin/java"
# DIR_JAVA_8 = DIR_SOFTWARE + "x86_jdks/jdk1.8.0_131/"
# PATH_JAVAC_11 = DIR_SOFTWARE + "x86_jdks/jdk-11.0.2/bin/javac" 
# PATH_JAVA_11 = DIR_SOFTWARE + "x86_jdks/jdk-11.0.2/bin/java"
# DIR_JAVA_11 = DIR_SOFTWARE + "x86_jdks/jdk-11.0.2/"
# PATH_JAVAC_17 = DIR_SOFTWARE + "x86_jdks/jdk-17.0.5/bin/javac" 
# PATH_JAVA_17 = DIR_SOFTWARE + "x86_jdks/jdk-17.0.5/bin/java"
# DIR_JAVA_17 = DIR_SOFTWARE + "x86_jdks/jdk-17.0.5/"
# PATH_JAVAC_18 = DIR_SOFTWARE + "x86_jdks/jdk-18.0.2.1/bin/javac" 
# PATH_JAVA_18 = DIR_SOFTWARE + "x86_jdks/jdk-18.0.2.1/bin/java"
# DIR_JAVA_18 = DIR_SOFTWARE + "x86_jdks/jdk-18.0.2.1/"
# PATH_JAVAC_19 = DIR_SOFTWARE + "x86_jdks/jdk-19.0.1/bin/javac" 
# PATH_JAVA_19 = DIR_SOFTWARE + "x86_jdks/jdk-19.0.1/bin/java"
# DIR_JAVA_19 = DIR_SOFTWARE + "x86_jdks/jdk-19.0.1/"


PATH_JAVAC_8 = DIR_SOFTWARE + "zulu_jdks/zulu8.68.0.19-ca-jdk8.0.362-linux_x64/bin/javac" 
PATH_JAVA_8 = DIR_SOFTWARE + "zulu_jdks/zulu8.68.0.19-ca-jdk8.0.362-linux_x64/bin/java"
DIR_JAVA_8 = DIR_SOFTWARE + "zulu_jdks/zulu8.68.0.19-ca-jdk8.0.362-linux_x64/"
PATH_JAVAC_11 = DIR_SOFTWARE + "zulu_jdks/zulu11.62.17-ca-jdk11.0.18-linux_x64/bin/javac" 
PATH_JAVA_11 = DIR_SOFTWARE + "zulu_jdks/zulu11.62.17-ca-jdk11.0.18-linux_x64/bin/java"
DIR_JAVA_11 = DIR_SOFTWARE + "zulu_jdks/zulu11.62.17-ca-jdk11.0.18-linux_x64/"
PATH_JAVAC_13 = DIR_SOFTWARE + "zulu_jdks/zulu13.54.17-ca-jdk13.0.14-linux_x64/bin/javac" 
PATH_JAVA_13 = DIR_SOFTWARE + "zulu_jdks/zulu13.54.17-ca-jdk13.0.14-linux_x64/bin/java"
DIR_JAVA_13 = DIR_SOFTWARE + "zulu_jdks/zulu13.54.17-ca-jdk13.0.14-linux_x64/"
PATH_JAVAC_15 = DIR_SOFTWARE + "zulu_jdks/zulu15.46.17-ca-jdk15.0.10-linux_x64/bin/javac" 
PATH_JAVA_15 = DIR_SOFTWARE + "zulu_jdks/zulu15.46.17-ca-jdk15.0.10-linux_x64/bin/java"
DIR_JAVA_15 = DIR_SOFTWARE + "zulu_jdks/zulu15.46.17-ca-jdk15.0.10-linux_x64/"

PATH_JAVAC_17 = DIR_SOFTWARE + "zulu_jdks/zulu17.40.19-ca-jdk17.0.6-linux_x64/bin/javac" 
PATH_JAVA_17 = DIR_SOFTWARE + "zulu_jdks/zulu17.40.19-ca-jdk17.0.6-linux_x64/bin/java"
DIR_JAVA_17 = DIR_SOFTWARE + "zulu_jdks/zulu17.40.19-ca-jdk17.0.6-linux_x64/"
PATH_JAVAC_18 = DIR_SOFTWARE + "zulu_jdks/zulu18.32.13-ca-jdk18.0.2.1-linux_x64/bin/javac" 
PATH_JAVA_18 = DIR_SOFTWARE + "zulu_jdks/zulu18.32.13-ca-jdk18.0.2.1-linux_x64/bin/java"
DIR_JAVA_18 = DIR_SOFTWARE + "zulu_jdks/zulu18.32.13-ca-jdk18.0.2.1-linux_x64/"
PATH_JAVAC_19 = DIR_SOFTWARE + "zulu_jdks/zulu19.32.13-ca-jdk19.0.2-linux_x64/bin/javac" 
PATH_JAVA_19 = DIR_SOFTWARE + "zulu_jdks/zulu19.32.13-ca-jdk19.0.2-linux_x64/bin/java"
DIR_JAVA_19 = DIR_SOFTWARE + "zulu_jdks/zulu19.32.13-ca-jdk19.0.2-linux_x64/"
PATH_JAVAC_21 = DIR_SOFTWARE + "zulu_jdks/zulu21.32.17-ca-jdk21.0.2-linux_x64/bin/javac" 
PATH_JAVA_21 = DIR_SOFTWARE + "zulu_jdks/zulu21.32.17-ca-jdk21.0.2-linux_x64/bin/java"
DIR_JAVA_21 = DIR_SOFTWARE + "zulu_jdks/zulu21.32.17-ca-jdk21.0.2-linux_x64/"



################################# OTHERS #################################
DIR_ENV = "/usr/bin/env"
# PATH_USR_JVM_JAVA8 = "/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.322.b06-11.el8.x86_64/bin/java"
PATH_USR_JVM_JAVA8 = PATH_JAVA_8


ASSERTION_FAILURE_LIST = ["java.lang.AssertionError", "org.junit.ComparisonFailure", "org.junit.internal.AssertionError", "org.testng.AssertionError", "junit.framework.AssertionFailedError" , "org.opentest4j.AssertionFailedError"] # org.opentest4j.AssertionFailedError, 疑惑这个之前为啥不放进去？
# "arrays first differed at element" but not totoally same. use "contains"

# org.opentest4j.AssertionFailedError, array lengths differed ??感觉也没几个