#!/usr/bin/env python
# encoding: utf-8
"""

Created on 2019/10/16 12:27
@Author :  


# https://github.com/c2nes/javalang
"""

# import pathlib


# # Replace 'YourJavaFile.java' with your actual file path.
# find_asserts_in_java_file('YourJavaFile.java')


import json, os, sys
_PROJECT_NAME = "tool"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])
# from utility import file_processing, json_processing, CSV_processing, data_propcessing, java_parser
import config
import random
import javalang

import subprocess

# def get_method_code(java_file="", method_name="", class_code=""):
#     source_code = class_code
#     # Read the Java file
#     if len(java_file)>0:
#         with open(java_file, 'r') as file:
#             source_code = file.read()

#     # Parse the Java code
#     tree = javalang.parse.parse(source_code)

#     # Find the method with the given name
#     for path, node in tree:
#         if isinstance(node, javalang.tree.MethodDeclaration):
#             # Check if the method name matches either the simple name or the fully-qualified name
#             # print(node.name)
#             if node.name == method_name:
#                 # Get the code of the method
#                 start_line = node.position.line
#                 method_length = len(node.body)

#                 end_line = start_line + method_length 
#                 end_line_index = -1
#                 for index in range( end_line+1, len(source_code.split('\n')) ):
#                     line =  source_code.split('\n')[index]
#                     if line == ("}") or  (" public ") in line or (" void ") in line :
#                         break
#                     if line == ("    }") or line == ("  }"):
#                         end_line_index = index
#                         end_line = index
#                         break
#                 # end_line = start_line + method_length if start_line + method_length > end_line_index else end_line_index
#                 method_code = source_code.split('\n')[start_line-1:end_line +1]
#                 # method_code = source_code[node.position.start.offset:node.position.end.offset]
#                 return '\n'.join(method_code)
#                 # method_code = node.body.__str__
#                 # return method_code

#     # If method is not found, return None
#     return None


def get_method_content(java_file_path, method_name, class_code):
    java_code = class_code
    if len(java_file_path) > 0:
        with open(java_file_path, 'r') as java_file:
            java_code = java_file.read()

    tree = javalang.parse.parse(java_code)
    for path, node in tree.filter(javalang.tree.MethodDeclaration):
        if node.name == method_name:
            # print(node)
            # return node
            start_line = node.position.line
            end_line = start_line + str(node).count('\n')
            lines = java_code.split('\n')
            return '\n'.join(lines[start_line - 1 : end_line])  # -1 because line numbers start from 1


def replace_method(file_path, method_name, new_method_declaration, function):
    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name, new_method_declaration], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def get_skeleton_of_class(file_path, function):
    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def getDeclaredVariablesInMethod(file_path, method_name, function):
    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def getInvolvedClassInMethod(file_path, method_name, function):
    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def getVaribleRelevantCode(file_path, method_name, variable_info, function):
    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name, variable_info], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def get_method_body_or_related_class_field(file_path, method_name, function):
    # function: 
    # result = subprocess.run([config.PATH_JAVA_8, '-cp', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name], stdout=subprocess.PIPE)
    # return result.stdout.decode('utf-8')

    result = subprocess.run([config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", function, file_path, method_name], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

    # result = subprocess.run([config.PATH_JAVA_8, '-jar', "  TODO/workProjects/AutoMR/Java/demo/target/demo-1.0-SNAPSHOT-jar-with-dependencies.jar" , "getMethod", file_path, method_name], stdout=subprocess.PIPE)
    # return result.stdout.decode('utf-8')

    # # The command you want to execute
    # #   TODO/workProjects/AutoMR/Java/demo/target/demo-1.0-SNAPSHOT.jar
    # command = ["/usr/bin/env", config.PATH_JAVA_8, '-jar', config.AUTOMR_JAVA_DEMO_JAR_PATH , "com.d1.d2.util.paserJavaFileUtil", "getMethod" ,file_path, method_name]

    # # Use subprocess.run to execute the command
    # result = subprocess.run(command, capture_output=True, text=True)
    # return result.stdout


# # Example usage
# java_file_path = '  TODO/data/AutoMR/projects/apache__split__systemds/src/test/java/org/apache/sysds/test/functions/privacy/FineGrainedPrivacyTest_getDataRangesOfPrivacyLevelTest_AutoMR.java'
# method_name = 'getDataRangesOfPrivacyLevelTest_AutoMR'  # Can be a simple name or a fully-qualified name

# java_file_path = '  TODO/data/ITrans/projects/ngs-doo__split__dsl-json/library/src/test/java/com/dslplatform/json/DateTest.java_ITrans'
# method_name = 'localTimeBoundary_h'

# # print( get_method_body_or_related_class_field(java_file_path, method_name,function="getMethod") )
# print( get_method_body_or_related_class_field(java_file_path, method_name,function="getMethodAndRelatedFields") )

