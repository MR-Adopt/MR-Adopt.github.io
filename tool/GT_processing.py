"""
"""

import os, sys
_PROJECT_NAME = "InputTrans"
_CURRENT_ABSPATH = os.path.abspath(__file__)
sys.path.insert(0, _CURRENT_ABSPATH[:_CURRENT_ABSPATH.find(_PROJECT_NAME) + len(_PROJECT_NAME) + 1])

from utility import file_processing,json_processing, Evosuite_runner_general, java_file_processing, java_test, compile_java_poj
import test_IT
import config

import javalang
from javalang.tree import Annotation, MethodDeclaration, ClassDeclaration
import xml.etree.ElementTree as ET

inputTrans_poj_dir = config.ROOT_DIR
maven_benchmark_poj_dir = config.BENCHMARK_DIR
Generated_ES_TEST_DIR = config.ES_GENERATED_TEST_DIR

dir_GT_data = f"{inputTrans_poj_dir}/data/"
Profile_GT_MTCs_wo_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_wo_IT/profile.json"
Profile_GT_MTCs_w_IT_path = f"{inputTrans_poj_dir}/../experimental_data/dataset/GT_MTCs_w_IT/profile.json"


raw_GT_MTCs_wo_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_wo_IT/raw/"
raw_GT_MTCs_w_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_w_IT/raw/"
processed_GT_MTCs_wo_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_wo_IT/processed_GT_only/"
processed_GT_MTCs_w_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_w_IT/processed_GT_only/"
processed_MTCITrans_wo_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_wo_IT/processed_MTCITrans_only/"
processed_MTCITrans_w_IT_dir = f"{inputTrans_poj_dir}/data/GT_MTCs_w_IT/processed_MTCITrans_only/"

suffix_single_test="_ESTest" # for ES generated test
suffix_merged_tests=""

src_dir_to_place_crafted_GT_ITrans = f"{maven_benchmark_poj_dir}/src/main/java/com/dataset/"
src_GT_dir = f"{maven_benchmark_poj_dir}/src/main/java/com/dataset/GT/"
test_dir_to_place_crafted_MTC_ITrans = f"{maven_benchmark_poj_dir}/src/test/java/com/dataset/" # crafted_MTC_ITrans


package_line = config.PACKAGE_STATEMENT
PACKAGE_GT_STATEMENT = config.PACKAGE_GT_STATEMENT
GT_CLASS_SUFFIX = config.GT_CLASS_SUFFIX
HARDCODED_CLASS_SUFFIX = config.HARDCODED_CLASS_SUFFIX
PATH_JAVA = config.PATH_JAVA_8
DIR_m2 = config.DIR_MAVEN_USER_HOME
DIR_m2_repo = config.DIR_MAVEN_M2_REPO_USER_HOME

PATH_ITRANS_COMPILE_INFO = config.PATH_ITRANS_COMPILE_INFO


ITRANS_FOLDER_NAME = config.ITRANS_FOLDER_NAME
ITRANS_FOLDER_DIR = config.ITRANS_EXPERIMENTAL_POJ_FOLDER_DIR
ITRANS_RAW_DIR = config.ITRANS_RAW_DIR
ITRANS_GT_DIR = config.ITRANS_GT_DIR
ITRANS_MTCIT_DIR = config.ITRANS_MTCIT_DIR
ITRANS_GENERATED_IT_DIR = config.ITRANS_GENERATED_IT_DIR
FEW_SHOT_BASE_DIR = config.FEW_SHOT_BASE_DIR

Profile_GT_MTCs_wo_IT = json_processing.read(Profile_GT_MTCs_wo_IT_path)
Profile_GT_MTCs_w_IT = json_processing.read(Profile_GT_MTCs_w_IT_path)
file_processing.creatFolder_IfExistPass(raw_GT_MTCs_wo_IT_dir)
file_processing.creatFolder_IfExistPass(raw_GT_MTCs_w_IT_dir)
file_processing.creatFolder_IfExistPass(processed_GT_MTCs_wo_IT_dir)
file_processing.creatFolder_IfExistPass(processed_GT_MTCs_w_IT_dir)


Junit_helper_methods_annotations = [
    "@setUp",
    "@BeforeClass",
    "@Before",
    "@BeforeAll",
    "@After",
    "@AfterClass",
    "@AfterAll",
] 

class craftedSubject:
    def __init__(self, MTC_item):
        self.MTC_item = MTC_item
        self.crafted_class_name = ""
        self.IT_GT_only_test_class_file_path = ""
        self.IT_GT_only_test_class_FQN = ""
        self.MTCITrans_only_test_class_file_path = ""
        self.MTCITrans_only_test_class_FQN = ""
        self.MTC_h_only_test_class_file_path = ""
        self.MTC_h_only_test_class_FQN = ""
        
        self.mocked_generated_IT_only_test_class_file_path = ""
        self.mocked_generated_IT_GT_only_test_class_FQN = ""
        self.backup_mocked_generated_IT_file_path = ""
        self.MTCITrans_only_GTtest_class_file_path = ""
        self.MTCITrans_only_GTtest_class_FQN = ""

        self.poj_ITRANS_RAW_DIR = ""
        self.poj_ITRANS_GT_DIR = ""
        self.poj_ITRANS_MTC_ITrans_DIR = ""
        self.poj_ITRANS_GENERATED_IT_DIR = ""




def suggest_dependencies(MTC_item):
    test_file_path = MTC_item["test_file_path"]
    invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
    invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
    invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]

    suggest_dependencies = f"{invoked_class_FQN};{invoked_class_FQN}.*"
    print("suggested_dependencies: ", f"\"dependency\": \"{suggest_dependencies}\"")
    suggest_pom = ""
    # given path of a class, find the nearest pom.xml, and parse it to get the ariticalID, groupID, version

    """ get suggested pom """
    path_of_class =  test_file_path
    nearest_pom_path = test_file_path.split("/src/")[0] + "/pom.xml"
    def parse_pom(pom_path):
        """Parse the pom.xml to get artifactId, groupId, and version."""
        tree = ET.parse(pom_path)
        root = tree.getroot()

        # handle XML namespaces, which can often make XPath tricky
        namespaces = {'mvn': 'http://maven.apache.org/POM/4.0.0'}
        parent_element = root.find('mvn:parent', namespaces)
        if parent_element:
            artifact_id_element = parent_element.find('mvn:artifactId', namespaces)
            group_id_element = parent_element.find('mvn:groupId', namespaces)
            version_element = parent_element.find('mvn:version', namespaces)
            artifact_id = artifact_id_element.text if artifact_id_element is not None else None
            group_id = group_id_element.text if group_id_element is not None else None
            version = version_element.text if version_element is not None else None

        artifact_id_element = root.find('mvn:artifactId', namespaces)
        group_id_element = root.find('mvn:groupId', namespaces)
        version_element = root.find('mvn:version', namespaces)

        artifact_id = artifact_id_element.text if artifact_id_element is not None else artifact_id
        group_id = group_id_element.text if group_id_element is not None else group_id
        version = version_element.text if version_element is not None else version
        
        return group_id, artifact_id, version

    group_id, artifact_id, version = parse_pom(nearest_pom_path)
    print("suggested_pom: ", f"\"pom\": \"{group_id}:{artifact_id}:{version};{group_id}:{artifact_id}:{version}:test-jar\"")
    print("suggested_pom_statmens: ", f"\n\
    <dependency>\n\
    \t<groupId>{group_id}</groupId>\n\
    \t<artifactId>{artifact_id}</artifactId>\n\
    \t<version>{version}</version>\n\
    </dependency>\n\
    <dependency>\n\
    \t<groupId>{group_id}</groupId>\n\
    \t<artifactId>{artifact_id}</artifactId>\n\
    \t<version>{version}</version>\n\
    \t<type>test-jar</type>\n\
    </dependency>\n\
    ")


def prepare_crafted_GT_MTC_class_originalPoj(MTC_item,withSuggestedDependencies=False):
        """
        二、保存至：original项目 ITrans/下 
        * 2 pre-processing: GT ITrans function单独摘出来， [ITrans/processed_GT_only/]
            * 命名：class.java_ITrans-> class_method.java (同时改变内部class的命名方式)
            * dependency：
                * import MTCTestClass_MTC;  // for invoke MTCTestClass_MTC.inputTransformation__MTC()
            * 删除：取消`final`的设置
            * 删除：其他test case
        * 3 pre-processing: MTC_ITrans 单独摘出来，用于test case [ITrans/processed_MTCITrans_only/]
            * class_method -> class_methodTest 
            * 注释：input transformaion function
            * 注释：其他的test case
            * method invocation: inputTransformaion() -> class_method.inputTransformaion()

        同时backup至：inputtrans项目
        """
        # setting
        if "type" in MTC_item: type = MTC_item["type"]
        else:
            if MTC_item["withInputTransformation"]:
                type = "w_ITrans"
            else:
                type = "wo_ITrans"
        test_simple_name = MTC_item["test_simple_name"]
        original_MTC_test_file_path = MTC_item["test_file_path"]
        invoked_methods_FQS = MTC_item["invoked_methods_FQS"]
        invoked_method_FQN = invoked_methods_FQS[0].split("(")[0]
        invoked_class_FQN = invoked_method_FQN[: invoked_method_FQN.rfind(".") ]
        invoked_package_FQN = invoked_class_FQN[: invoked_class_FQN.rfind(".") ]

        test_file_path = MTC_item["test_file_path"]
        test_file = file_processing.read_TXTfile(test_file_path)
        package_line = test_file.split("\n")[:0]
        for line in test_file.split("\n"):
            if line.startswith("package "): package_line = line; break
            if line.strip().startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦
        
        # print( "MAKR, FQS_testMethos: ", MTC_item["FQS_testMethos"])
        # print( "MAKR, invoked_methods_FQS: ", invoked_methods_FQS)
        # print( "MAKR, invoked_package_FQN: ", invoked_package_FQN)
        special_list = ["com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest.test()","com.alibaba.fastjson2.internal.processor.collections.JSONArrayTest.test1()"]
        FQS_testMethos = MTC_item["FQS_testMethos"]
        if f"{invoked_package_FQN}." not in FQS_testMethos or MTC_item["FQS_testMethos"] in special_list: # 说明：invoked_package_FQN 识别有误
            test_file_path = MTC_item["test_file_path"]
            test_file = file_processing.read_TXTfile(test_file_path)
            package_line = test_file.split("\n")[:0]
            for line in test_file.split("\n"):
                if line.startswith("package "): package_line = line; break
                if line.strip().startswith("package "): package_line = line; break
            invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦
        
        test_file_path = MTC_item["test_file_path"]
        test_file = file_processing.read_TXTfile(test_file_path)
        package_line = test_file.split("\n")[:0]
        for line in test_file.split("\n"):
            if line.startswith("package "): package_line = line; break
        invoked_package_FQN = package_line.replace('package ','').replace(';','').strip() # 最准确啦
        
        # print( "MAKR, FQS_testMethos: ", MTC_item["FQS_testMethos"])
        # print( "MAKR, invoked_methods_FQS: ", invoked_methods_FQS)
        # print( "MAKR, invoked_package_FQN: ", invoked_package_FQN)

        """ 1. read manually crafted file """
        original_crafted_GT_MTC_test_file_path = original_MTC_test_file_path.replace(".java", ".java_ITrans")
        if not file_processing.pathExist(original_crafted_GT_MTC_test_file_path):
            original_crafted_GT_MTC_test_file_path = original_MTC_test_file_path.replace(".java", ".java_IT")
        crafted_GT_MTC_test_class_text = file_processing.read_TXTfile(original_crafted_GT_MTC_test_file_path)
        # inputTransformation -> inputTransformation_MTCname # 
        if f" inputTransformation(" in crafted_GT_MTC_test_class_text and f" inputTransformation_{test_simple_name}(" not in crafted_GT_MTC_test_class_text:
            crafted_GT_MTC_test_class_text.replace(f" inputTransformation(", f" inputTransformation_{test_simple_name}(")
        # 1. store file (for backup)
        poj_name = MTC_item["poj_name"]
        poj_dir = original_MTC_test_file_path.split( poj_name )[0] + poj_name + "/"
        poj_ITRANS_FOLDER_DIR = ITRANS_FOLDER_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_FOLDER_DIR)

        poj_ITRANS_RAW_DIR = ITRANS_RAW_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_RAW_DIR)
        poj_ITRANS_GT_DIR = ITRANS_GT_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_GT_DIR)
        poj_ITRANS_MTC_ITrans_DIR = ITRANS_MTCIT_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_MTC_ITrans_DIR)
        poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name; file_processing.creatFolder_IfExistPass(poj_ITRANS_GENERATED_IT_DIR)

        crafted_GT_MTC_test_file_path_for_backup = poj_ITRANS_RAW_DIR + original_crafted_GT_MTC_test_file_path.split("/")[-1] # wo
        file_processing.write_TXTfile(path=crafted_GT_MTC_test_file_path_for_backup, content=crafted_GT_MTC_test_class_text )
        ## store to local central 'inputTrans' poj (for backup)
        if type == "wo_ITrans":
            crafted_GT_MTC_test_file_path_central_poj = raw_GT_MTCs_wo_IT_dir + original_crafted_GT_MTC_test_file_path.split("/")[-1] # wo
        else:
            crafted_GT_MTC_test_file_path_central_poj = raw_GT_MTCs_w_IT_dir + original_crafted_GT_MTC_test_file_path.split("/")[-1] # w
        file_processing.write_TXTfile(path=crafted_GT_MTC_test_file_path_central_poj, content=crafted_GT_MTC_test_class_text )

        

        """ 2. processing: class of processed_GT_only/ """
        """
        	pre-processing: GT ITrans function单独摘出来， [processed_GT_only/]
            * 命名：class.java_ITrans-> class_method.java (同时改变内部class的命名方式)
            * dependency：
                * import MTCTestClass_MTC;  // for invoke MTCTestClass_MTC.inputTransformation__MTC()
            * 删除：取消`final`的设置
            * 删除：其他test case
            * 把MTC MTC_h MTC_ITrans methods 都注释掉 [todo]
        """
        # * 命名：class.java_ITrans-> class_method.java (同时改变内部class的命名方式)
        MTC_test_class_name = original_MTC_test_file_path.split("/")[-1].replace(".java", "")
        processed_crafted_GT_MTC_test_class_name = f"{MTC_test_class_name}_{test_simple_name}"
        class_name = processed_crafted_GT_MTC_test_class_name
        crafted_GT_MTC_test_class_text = crafted_GT_MTC_test_class_text.replace(MTC_test_class_name, class_name)
        processed_crafted_GT_MTC_test_class_file_path = f"{poj_ITRANS_GT_DIR}{class_name}.java"

        # * 删除：取消代码中对于`final`变量的限制
        crafted_GT_MTC_test_class_text = crafted_GT_MTC_test_class_text.replace("\tfinal ", "")
        
        # * 删除：代码中不想干的test case
        # crafted_GT_MTC_test_class_text = crafted_GT_MTC_test_class_text.replace("`","")
        # print( "inputTransformation_isLowerThan", "String inputTransformation_isLowerThan" in  crafted_GT_MTC_test_class_text)
        # crafted_GT_MTC_test_class_text = delete_irrelevant_test_cases(crafted_GT_MTC_test_class_text, test_simple_name, restrict_to_given_test_case=True)
        crafted_GT_MTC_test_class_text = delete_irrelevant_test_cases(crafted_GT_MTC_test_class_text, test_simple_name)
        # print( "inputTransformation_isLowerThan", "String inputTransformation_isLowerThan" in  crafted_GT_MTC_test_class_text)
        
        
        # * dependency：
		# * import CUT; CUT.*; 
        if withSuggestedDependencies:        suggest_dependencies(MTC_item)
        package_line = crafted_GT_MTC_test_class_text.split("\n")[:0]
        for line in crafted_GT_MTC_test_class_text.split("\n"):
            if line.startswith("package "):
                package_line = line; break
        import_dependencies = MTC_item["dependency"].split(";")
        import_statement = ("\n").join( [f"import {ele};" for ele in import_dependencies if f"import {ele};" not in crafted_GT_MTC_test_class_text ] )
        crafted_GT_MTC_test_class_text = crafted_GT_MTC_test_class_text.replace(f"{package_line}", f"{package_line}\n\n{import_statement}")

        # * 把MTC MTC_h MTC_ITrans methods 都注释掉 [todo]
        # print( crafted_GT_MTC_test_class_text )
        ITrans_only_test_class_text = crafted_GT_MTC_test_class_text # 202040411： 暂时不comment其他的methods，因为会误伤其他helper methods/sub classes
        # ITrans_only_test_class_text = comment_target_method(crafted_GT_MTC_test_class_text, f"inputTransformation_{test_simple_name}", only_keep_target_method=True, keep_helper_methods=True)
        # print("ITrans_only_test_class_text: ", ITrans_only_test_class_text)

        # 更改一下class name -> *_GT
        class_name_GT = f"{class_name}{GT_CLASS_SUFFIX}"
        ITrans_only_test_class_text = ITrans_only_test_class_text.replace(f"class {class_name}", f"class {class_name_GT}")
        
        # store: * processed_GT_only/
        IT_GT_only_test_class_file_path = f"{poj_ITRANS_GT_DIR}{invoked_package_FQN.replace('.','/')}/{class_name_GT}.java"
        file_processing.creatFolder_recursively_IfExistPass(f"{poj_ITRANS_GT_DIR}{invoked_package_FQN.replace('.','/')}/")
        file_processing.write_TXTfile(path=IT_GT_only_test_class_file_path, content=ITrans_only_test_class_text)
        ## store to local central 'inputTrans' poj (for backup)
        if type == "wo_ITrans":
            processed_GT_only_test_class_file_path_central_poj = f"{processed_GT_MTCs_wo_IT_dir}{invoked_package_FQN.replace('.','/')}/{class_name_GT}.java" # wo
            file_processing.creatFolder_recursively_IfExistPass(f"{processed_GT_MTCs_wo_IT_dir}{invoked_package_FQN.replace('.','/')}/")
        else:
            processed_GT_only_test_class_file_path_central_poj = f"{processed_GT_MTCs_w_IT_dir}{invoked_package_FQN.replace('.','/')}/{class_name_GT}.java" # w
            file_processing.creatFolder_recursively_IfExistPass(f"{processed_GT_MTCs_w_IT_dir}{invoked_package_FQN.replace('.','/')}/")
        file_processing.write_TXTfile(path=processed_GT_only_test_class_file_path_central_poj, content=ITrans_only_test_class_text )

        """  2.5. pre-processing: class of generated_ITrans/ """
        # use GT_only_class mock generated ITrans
        poj_ITRANS_GENERATED_IT_DIR = ITRANS_GENERATED_IT_DIR % poj_name
        mock_generated_class_file_path = f"{poj_ITRANS_GENERATED_IT_DIR}{invoked_package_FQN.replace('.','/')}/{class_name}.java"
        file_processing.creatFolder_recursively_IfExistPass(f"{poj_ITRANS_GENERATED_IT_DIR}{invoked_package_FQN.replace('.','/')}/")
        mock_generated_class = ITrans_only_test_class_text.replace(f"{class_name_GT}", f"{class_name}")
        file_processing.write_TXTfile(path=mock_generated_class_file_path, content=mock_generated_class)
        # for backup: original poj, GT only dir/ 
        mock_generated_class_file_path_backup_IT_only = f"{poj_ITRANS_GT_DIR}{invoked_package_FQN.replace('.','/')}/{class_name}.java"
        file_processing.write_TXTfile(path=mock_generated_class_file_path_backup_IT_only, content=mock_generated_class)
        # for backup: contral inputTrans poj, GT only dir/ 
        file_processing.write_TXTfile(path=processed_GT_only_test_class_file_path_central_poj.replace(f"{class_name_GT}.java",f"{class_name}.java"), content=mock_generated_class)

        """  3. pre-processing: class of processed_MTCITrans_only/ ，用于test case """
        dir_MTCItrans_only_test_class_file_in_central_poj, MTCITrans_only_test_class_file_path, MTCITrans_only_test_class_name, MTCITrans_only_GTtest_class_file_path, MTCITrans_only_GTtest_class_name = prepare_MTCTrans_only_class(crafted_GT_MTC_test_class_text,test_simple_name,class_name, class_name_GT, invoked_package_FQN, poj_ITRANS_MTC_ITrans_DIR,type)

        """ 4. pre-processing: class of MTC_h_only/ """
        MTC_h_only_test_class_name, MTC_h_only_test_class_file_path = prepare_MTC_h_only_class(test_simple_name, crafted_GT_MTC_test_class_text, class_name, poj_ITRANS_MTC_ITrans_DIR, dir_MTCItrans_only_test_class_file_in_central_poj, invoked_package_FQN)

        """ 5. return crafted_subject """
        crafted_subject = craftedSubject(MTC_item)
        crafted_subject.crafted_class_name = class_name
        crafted_subject.IT_GT_only_test_class_file_path = IT_GT_only_test_class_file_path
        crafted_subject.IT_GT_only_test_class_FQN = f"{invoked_package_FQN}.{class_name_GT}"
        crafted_subject.MTCITrans_only_test_class_file_path = MTCITrans_only_test_class_file_path
        crafted_subject.MTCITrans_only_test_class_FQN = f"{invoked_package_FQN}.{MTCITrans_only_test_class_name}"

        crafted_subject.mocked_generated_IT_only_test_class_file_path = mock_generated_class_file_path
        crafted_subject.mocked_generated_IT_GT_only_test_class_FQN = f"{invoked_package_FQN}.{class_name}"
        crafted_subject.MTCITrans_only_GTtest_class_file_path = MTCITrans_only_GTtest_class_file_path
        crafted_subject.MTCITrans_only_GTtest_class_FQN = f"{invoked_package_FQN}.{MTCITrans_only_GTtest_class_name}"
        crafted_subject.MTC_h_only_test_class_file_path = MTC_h_only_test_class_file_path
        crafted_subject.MTC_h_only_test_class_FQN = f"{invoked_package_FQN}.{MTC_h_only_test_class_name}"

        crafted_subject.poj_ITRANS_RAW_DIR = poj_ITRANS_RAW_DIR
        crafted_subject.poj_ITRANS_GT_DIR = poj_ITRANS_GT_DIR
        crafted_subject.poj_ITRANS_MTC_ITrans_DIR = poj_ITRANS_MTC_ITrans_DIR
        crafted_subject.poj_ITRANS_GENERATED_IT_DIR = poj_ITRANS_GENERATED_IT_DIR
        return crafted_subject

def prepare_MTCTrans_only_class(crafted_GT_MTC_test_class_text,test_simple_name,class_name, class_name_GT, invoked_package_FQN, poj_ITRANS_MTC_ITrans_DIR,type):
    # * 注释：input transformaion function
    # * 注释：其他的test case
    # comment 掉其他, 仅保留：MTC_ITrans
    MTCITrans_only_test_class_text = crafted_GT_MTC_test_class_text
    MTCITrans_only_test_class_text = comment_target_method(MTCITrans_only_test_class_text, f"inputTransformation_{test_simple_name}")
    # print( MTCITrans_only_test_class_text )
    MTCITrans_only_test_class_text = comment_target_method(MTCITrans_only_test_class_text, f"{test_simple_name}")
    MTCITrans_only_test_class_text = comment_target_method(MTCITrans_only_test_class_text, f"{test_simple_name}_original")
    MTCITrans_only_test_class_text = comment_target_method(MTCITrans_only_test_class_text, f"{test_simple_name}_h")

    # * class_method -> class_methodTest (重命名class及文件；以服务Junit框架)
    ## generated ITrans
    MTCITrans_only_test_class_name = f"{class_name}Test"
    MTCITrans_only_test_class_text = MTCITrans_only_test_class_text.replace(class_name, MTCITrans_only_test_class_name)
    ## GT
    MTCITrans_only_GTtest_class_name = f"{class_name}{GT_CLASS_SUFFIX}Test"
    MTCITrans_only_GTtest_class_text = MTCITrans_only_test_class_text.replace(MTCITrans_only_test_class_name, MTCITrans_only_GTtest_class_name)
    
    # * method invocation: inputTransformaion() -> class_method.inputTransformaion()
    if "= inputTransformation" in MTCITrans_only_test_class_text: 
        MTCITrans_only_test_class_text = MTCITrans_only_test_class_text.replace( f"= inputTransformation", f"= {class_name}.inputTransformation" )
        MTCITrans_only_GTtest_class_text = MTCITrans_only_GTtest_class_text.replace( f"= inputTransformation", f"= {class_name_GT}.inputTransformation" )
    elif ") inputTransformation" in MTCITrans_only_test_class_text:
        MTCITrans_only_test_class_text = MTCITrans_only_test_class_text.replace( f") inputTransformation", f") {class_name}.inputTransformation" )
        MTCITrans_only_GTtest_class_text = MTCITrans_only_GTtest_class_text.replace( f") inputTransformation", f") {class_name_GT}.inputTransformation" ) 
    

    # * dependency：
    import_statement = f"import {invoked_package_FQN}.{class_name};"
    MTCITrans_only_test_class_text = MTCITrans_only_test_class_text.replace(f"{package_line}", f"{package_line}\n\n{import_statement}")
    # import class_name_GT; 
    import_statementGT = f"import {invoked_package_FQN}.{class_name_GT};"
    MTCITrans_only_GTtest_class_text = MTCITrans_only_GTtest_class_text.replace(f"{package_line}", f"{package_line}\n\n{import_statementGT}")

    # store: processed_MTCITrans_only/
    MTCITrans_only_test_class_dir = f"{poj_ITRANS_MTC_ITrans_DIR}{invoked_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(MTCITrans_only_test_class_dir)
    MTCITrans_only_test_class_file_path = f"{MTCITrans_only_test_class_dir}{MTCITrans_only_test_class_name}.java"
    file_processing.write_TXTfile(path=MTCITrans_only_test_class_file_path, content=MTCITrans_only_test_class_text) # generated ITrans test
    MTCITrans_only_GTtest_class_file_path = f"{MTCITrans_only_test_class_dir}{MTCITrans_only_GTtest_class_name}.java"
    file_processing.write_TXTfile(path=MTCITrans_only_GTtest_class_file_path, content=MTCITrans_only_GTtest_class_text) # GT test
    
    ## scopy_to_central_poj (for backup)
    dir_MTCItrans_only_test_class_file_in_central_poj = ""
    if type == "wo_ITrans":
        dir_MTCItrans_only_test_class_file_in_central_poj = f"{processed_MTCITrans_wo_IT_dir}{invoked_package_FQN.replace('.','/')}/"
    else:
        dir_MTCItrans_only_test_class_file_in_central_poj = f"{processed_MTCITrans_w_IT_dir}{invoked_package_FQN.replace('.','/')}/"
    path_MTCItrans_only_test_class_file_in_central_poj = f"{dir_MTCItrans_only_test_class_file_in_central_poj}{MTCITrans_only_test_class_name}.java"
    path_MTCItrans_only_GTtest_class_file_in_central_poj = f"{dir_MTCItrans_only_test_class_file_in_central_poj}{MTCITrans_only_GTtest_class_name}.java"
    file_processing.creatFolder_recursively_IfExistPass(dir_MTCItrans_only_test_class_file_in_central_poj)
    file_processing.write_TXTfile(path=path_MTCItrans_only_test_class_file_in_central_poj, content=MTCITrans_only_test_class_text ) # generated ITrans test
    file_processing.write_TXTfile(path=path_MTCItrans_only_GTtest_class_file_in_central_poj, content=MTCITrans_only_GTtest_class_text ) # GT test
    return dir_MTCItrans_only_test_class_file_in_central_poj, MTCITrans_only_test_class_file_path, MTCITrans_only_test_class_name, MTCITrans_only_GTtest_class_file_path, MTCITrans_only_GTtest_class_name


def prepare_MTC_h_only_class(test_simple_name, crafted_GT_MTC_test_class_text, class_name, poj_ITRANS_MTC_ITrans_DIR, dir_MTCItrans_only_test_class_file_in_central_poj, invoked_package_FQN):
    # MTC_h_only_class_text = crafted_GT_MTC_test_class_text
    # print(crafted_GT_MTC_test_class_text)
    MTC_h_only_class_text = delete_irrelevant_test_cases(crafted_GT_MTC_test_class_text, f"{test_simple_name}{HARDCODED_CLASS_SUFFIX}", restrict_to_given_test_case=True)
    # print(MTC_h_only_class_text)
    # 重命名class及文件名；以服务Junit框架)
    MTC_h_only_test_class_name = f"{class_name}{HARDCODED_CLASS_SUFFIX}Test"
    MTC_h_only_test_class_text = MTC_h_only_class_text.replace(class_name, MTC_h_only_test_class_name)

    # store to original poj
    MTCITrans_only_test_class_dir = f"{poj_ITRANS_MTC_ITrans_DIR}{invoked_package_FQN.replace('.','/')}/"
    file_processing.creatFolder_recursively_IfExistPass(MTCITrans_only_test_class_dir)
    MTC_h_only_test_class_file_path = f"{MTCITrans_only_test_class_dir}{MTC_h_only_test_class_name}.java"
    file_processing.write_TXTfile(path=MTC_h_only_test_class_file_path, content=MTC_h_only_test_class_text) # generated ITrans test

    # store to local central 'inputTrans' poj
    path_MTC_h_only_test_class_file_in_central_poj = f"{dir_MTCItrans_only_test_class_file_in_central_poj}{MTC_h_only_test_class_name}.java"
    file_processing.creatFolder_recursively_IfExistPass(dir_MTCItrans_only_test_class_file_in_central_poj)
    file_processing.write_TXTfile(path=path_MTC_h_only_test_class_file_in_central_poj, content=MTC_h_only_test_class_text )

    return MTC_h_only_test_class_name, MTC_h_only_test_class_file_path


def copy_to_central_poj(crafted_subject):
    # TODO，currently, the funciton is mixed in the "prepare_crafted_GT_MTC_class_originalPoj" function
    return crafted_subject

def make_method_private(crafted_GT_MTC_test_class_text):
    pass


def delete_irrelevant_test_cases(crafted_GT_MTC_test_class_text, relevant_test_case_simple_name, restrict_to_given_test_case=False):
    """
    * 删除：irrelevant test cases
    * 保留：class field, @setup, @Before, @BeforeAll 等helper methods
    """
    # Parse the file using javalang
    java_class = crafted_GT_MTC_test_class_text
    print(java_class)
    tree = javalang.parse.parse(java_class)

    # Create a list to store methods to be removed
    methods_to_remove = []

    # Find all methods that are annotated with @Test and not relevant
    for path, node in tree.filter(MethodDeclaration):
        is_test_method = any(isinstance(anno, Annotation) and anno.name == 'Test' for anno in node.annotations)
        if restrict_to_given_test_case: # 紧
            if is_test_method and relevant_test_case_simple_name!=node.name:
                methods_to_remove.append(node)
            elif "inputTransformation_" in node.name: # inputTransformation 也不保留
                methods_to_remove.append(node) 
        else:                           # 松
            if is_test_method and f"{relevant_test_case_simple_name}_" not in node.name and {relevant_test_case_simple_name}!=node.name:
                # print( "methods_to_remove: ", node.name )
                methods_to_remove.append(node)
            # 删除，其他MTC的input transformation function
            if "inputTransformation_" in  node.name and relevant_test_case_simple_name not in  node.name:
                # print( "methods_to_remove: ", node.name )
                methods_to_remove.append(node)

     
        # for path, node in tree.filter(MethodDeclaration):
        #     is_test_method = any(isinstance(anno, Annotation) and anno.name == 'Test' for anno in node.annotations)
        #     if is_test_method and f"{relevant_test_case_simple_name}_" not in node.name and {relevant_test_case_simple_name}!=node.name:
        #         # print( "methods_to_remove: ", node.name )
        #         methods_to_remove.append(node)
        #     # 删除，其他MTC的input transformation function
        #     if "inputTransformation_" in  node.name and relevant_test_case_simple_name not in  node.name:
        #         # print( "methods_to_remove: ", node.name )
        #         methods_to_remove.append(node)


    
    # find all methods
    all_methods = []
    all_methods_start_line = []
    for path, node in tree.filter(MethodDeclaration):
        all_methods.append(node)
        start_line, _ = node.position
        all_methods_start_line.append(start_line)
    all_methods_start_line = sorted(all_methods_start_line)
    
    lines = java_class.splitlines()
    index_to_delete = []
    updated_lines = []
    # Remove the irrelevant test methods line by line
    for method in methods_to_remove:
        # print( "methods_to_remove: ", method.name )
        start_line, _ = method.position
        index = start_line-2 # 从@test开始删除 (index是从0开始的， line number 是从1开始的)
        method_len = 0
        while index + method_len<len(lines):
            # 说明是下一个 method的开始了
            if index + method_len > start_line and (index + method_len +1) in all_methods_start_line: # (index是从0开始的， line number 是从1开始的), 所以 index要+1
                break
            # 说明是下一个test method的开始了
            if index + method_len > start_line and (lines[index + method_len].strip().startswith("@") or lines[index + method_len]=="}"): # or "class " in lines[index + method_len].strip():
                break
            # 说明是一个class 的声明
            if index + method_len > start_line and (" class " in lines[index + method_len]): # or "class " in lines[index + method_len].strip():
                break
            index_to_delete.append(index + method_len)
            method_len +=1
        # option2: 直接用 this start_line - next start_line in all_methods_start_line, 就可以得出; 不准确，万一不是连续 methods呢。。
    # print( "index_to_delete: ", index_to_delete)
    
    for index in range(len(lines)):
        if index not in index_to_delete:
            updated_lines.append(lines[index])
    updated_java_class = "\n".join(updated_lines)

    # # Write the updated class back to the file
    # crafted_GT_MTC_test_class_path = "./data/AutoMR/projects/cantaloupe-project__split__cantaloupe/src/test/java/edu/illinois/library/cantaloupe/image/iptc/DataSetTest.java_ITrans0000"
    # with open(crafted_GT_MTC_test_class_path, 'w') as f:
    #     f.write(updated_java_class)
    # print(f"updated_java_class: {updated_java_class}")
    return updated_java_class


def comment_non_target_method(test_class_text, target_method_name): # to keep input transformation only
    pass


def comment_target_method(test_class_text, target_method_name, only_keep_target_method=False, keep_helper_methods=True): # to delete input transformation and other test cases
    """_summary_
        only_keep_target_method: True, only uncomment the target method

    """
    # print( test_class_text )
    # Parse the file using javalang
    java_class = test_class_text
    # Parse the file using javalang
    print( "java_class: ", java_class )
    tree = javalang.parse.parse(java_class)

    methods = []
    all_methods_start_line = []
    for path, node in tree.filter(MethodDeclaration):
        methods.append(node)
        start_line, _ = node.position
        all_methods_start_line.append(start_line)

    # Remove the irrelevant test methods line by line
    lines = java_class.splitlines()
    commented_ATTest_lines_index = []
    for method in methods:
        if only_keep_target_method:
            if method.name == target_method_name:
                continue
        else:
            if method.name != target_method_name:
                continue

        start_line, _ = method.position
        index = start_line-1 # 从当前行开始删除
        if lines[start_line-2].strip().startswith("@"):
            # keep_helper_methods
            if keep_helper_methods:
                flag_is_helper_method = False
                for ele in Junit_helper_methods_annotations:
                    if ele in lines[start_line-2]: 
                        flag_is_helper_method=True;break;
                if flag_is_helper_method: continue

            lines[start_line-2] = "// " + lines[start_line-2]  # 从@Test开始注释   
            commented_ATTest_lines_index.append(start_line-2)    # commented line index of "@Test" 
        while index<len(lines):
            lines[index] = "// " + lines[index]
            index += 1
            # 说明遇到下一个method的开始了
            if index >= start_line and ( index+1 in all_methods_start_line or # 因为index是从0开始的， line number 是从1开始的
                                        lines[index].strip().startswith("@") or 
                                        lines[index].strip().startswith("public") or 
                                        lines[index].strip().startswith("void") or 
                                        lines[index]==("}") or
                                        " class " in lines[index]): # # or "class " in lines[index].strip()
                break
    
    # # delete the commented @Test line, 防止给后续处理带来误报。。。
    # for line_index in commented_ATTest_lines_index:
    #     lines[line_index] = ""

    updated_java_class = "\n".join(lines)
    return updated_java_class


def get_classpath(MTC_item, POJ_DIR=config.BENCHMARK_DIR , poj_build_tool="maven"):
    poj_name = MTC_item["poj_name"]
    dependency_jars_paths = []
    if "pom" in MTC_item:
        dependency_jars_list = MTC_item["pom"].split(";")
        for dependency_jar_item in dependency_jars_list:
            groupID = dependency_jar_item.split(":")[0]
            artifactID = dependency_jar_item.split(":")[1]
            version = dependency_jar_item.split(":")[2]
            jar_name = f"{artifactID}-{version}.jar"
            if len(dependency_jar_item.split(":")) ==4 and "test" in dependency_jar_item.split(":")[3]:
                jar_name = f"{artifactID}-{version}-tests.jar"
            if len(dependency_jar_item.split(":")) ==4 and "dependencies" in dependency_jar_item.split(":")[3]:
                jar_name = f"{artifactID}-{version}-{dependency_jar_item.split(':')[3]}.jar"
            jar_path = f"{DIR_m2_repo}/{groupID.replace('.','/')}/{artifactID.replace('.','/')}/{version}/{jar_name}"
            dependency_jars_paths.append(jar_path)
    dependency_all_jars_path = (":").join(dependency_jars_paths)


    class_dir_list = java_file_processing.get_all_class_relative_path(dir=POJ_DIR, include_test_classes=True, poj_build_tool=poj_build_tool)
    all_class_dir_str = (":").join( class_dir_list )
    CLASS_PATHS = f"{Generated_ES_TEST_DIR}:{all_class_dir_str}:{dependency_all_jars_path}"
    ClassPath = f"{CLASS_PATHS}:{config.PATH_EVOSUITE_JAR}:{config.PATH_ES_RUNTIME_JAR}:{config.PATH_JUNIT4_JAR}:{config.PATH_JUNIT5_JAR}:{config.PATH_HAMCREST_CORE_JAR}"

    return ClassPath


def compile_and_execute_crafted_class(crafted_subject, passIfcompile=True, passIfexecuted=True):
    # compile order:  GT, MTC_ITrans test case
    # compile condition: classpath for original MTC execution 
    result = {
        "compilation_IT_GT_only": True,
        "compilation_mocked_IT_only": True,
        "compilation_MTCITrans_only": True,
        "compilation_MTCITrans_only_GTtest": True,
        "compilation_MTC_h_only_test": True,

        "execution_MTC_ITrans_result": True,
        "execution_MTC_ITrans_GTtest_result": True,
        "execution_MTC_htest_result": True,
    }

    MTC_item = crafted_subject.MTC_item
    IT_GT_only_test_class_file_path = crafted_subject.IT_GT_only_test_class_file_path
    mocked_generated_IT_only_test_class_file_path = crafted_subject.mocked_generated_IT_only_test_class_file_path
    MTCITrans_only_test_class_file_path = crafted_subject.MTCITrans_only_test_class_file_path
    MTCITrans_only_GTtest_class_file_path = crafted_subject.MTCITrans_only_GTtest_class_file_path
    MTC_h_only_test_class_file_path = crafted_subject.MTC_h_only_test_class_file_path
    poj_ITRANS_RAW_DIR = crafted_subject.poj_ITRANS_RAW_DIR

    test_file_path = MTC_item["test_file_path"]
    poj_name = MTC_item["poj_name"]
    poj_dir = test_file_path.split(poj_name)[0] + f"{poj_name}/"
    # poj_compilation_info = json_processing.read( f"{poj_dir}AutoMR/compile_info.json" )
    poj_compilation_info = json_processing.read( PATH_ITRANS_COMPILE_INFO %  poj_name )
    poj_build_tool = poj_compilation_info["build_tool"][0]
    jdk_version = poj_compilation_info[f"{poj_build_tool}_java_version_success"][0]
    
    CMD_CD = f"cd {poj_dir};"
    PATH_JAVAC = compile_java_poj.get_jdkc_path(jdk_version)
    # IT_GT_only_test_class_file_path
    generated_dot_class_path = IT_GT_only_test_class_file_path.replace(".java", ".class")
    if not (passIfcompile and file_processing.pathExist(generated_dot_class_path)):
        res = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp="", Path_TestFile_to_compile = IT_GT_only_test_class_file_path, PATH_JAVAC=PATH_JAVAC)
        if res!=0:  result["compilation_IT_GT_only"] = False # cmd exe result
    else:
        print(f"Skip: {IT_GT_only_test_class_file_path} has been compiled")
    
    # mocked_generated_IT_only_test_class_file_path
    generated_dot_class_path = mocked_generated_IT_only_test_class_file_path.replace(".java", ".class")
    if not (passIfcompile and file_processing.pathExist(generated_dot_class_path)):
        res = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp="", Path_TestFile_to_compile = mocked_generated_IT_only_test_class_file_path, PATH_JAVAC=PATH_JAVAC)
        if res!=0: result["compilation_mocked_IT_only"] = False # cmd exe result
    else:
        print(f"Skip: {mocked_generated_IT_only_test_class_file_path} has been compiled")
    if file_processing.pathExist(generated_dot_class_path): # cp to raw/ for backup
        file_name = mocked_generated_IT_only_test_class_file_path.split("/")[-1]
        backup_mocked_generated_IT_file_path = f"{poj_ITRANS_RAW_DIR}{file_name}"
        file_processing.copyFile(mocked_generated_IT_only_test_class_file_path, backup_mocked_generated_IT_file_path)
        file_processing.copyFile(generated_dot_class_path, backup_mocked_generated_IT_file_path.replace(".java", ".class"))
        crafted_subject.backup_mocked_generated_IT_file_path = backup_mocked_generated_IT_file_path


    extra_cp = f"{crafted_subject.poj_ITRANS_GT_DIR}:{crafted_subject.poj_ITRANS_MTC_ITrans_DIR}:{crafted_subject.poj_ITRANS_GENERATED_IT_DIR}"
    # MTCITrans_only_test_class_file_path
    generated_dot_class_path = MTCITrans_only_test_class_file_path.replace(".java", ".class")
    if not (passIfcompile and file_processing.pathExist(generated_dot_class_path)):
        res = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp=extra_cp, Path_TestFile_to_compile = MTCITrans_only_test_class_file_path, PATH_JAVAC=PATH_JAVAC)
        if res!=0: result["compilation_MTCITrans_only"] = False # cmd exe result
    else:
        print(f"Skip: {MTCITrans_only_test_class_file_path} has been compiled")

    # MTCITrans_only_GTtest_class_file_path
    generated_dot_class_path = MTCITrans_only_GTtest_class_file_path.replace(".java", ".class")
    if not (passIfcompile and file_processing.pathExist(generated_dot_class_path)):
        res = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp=extra_cp, Path_TestFile_to_compile = MTCITrans_only_GTtest_class_file_path, PATH_JAVAC=PATH_JAVAC)
        if res!=0: result["compilation_MTCITrans_only_GTtest"] = False # cmd exe result
    else:
        print(f"Skip: {MTCITrans_only_GTtest_class_file_path} has been compiled")

    # MTC_h_only_test_class_file_path
    generated_dot_class_path = MTC_h_only_test_class_file_path.replace(".java", ".class")
    if not (passIfcompile and file_processing.pathExist(generated_dot_class_path)):
        res = java_test.compile_test_class_general(poj_build_tool, poj_name, CMD_CD, poj_dir, CP_jar_path="", extra_cp=extra_cp, Path_TestFile_to_compile = MTC_h_only_test_class_file_path, PATH_JAVAC=PATH_JAVAC)
        if res!=0: result["compilation_MTC_h_only_test"] = False # cmd exe result
    else:
        print(f"Skip: {MTC_h_only_test_class_file_path} has been compiled")

    # setting for exectute test case
    FQS_testMethos = MTC_item["FQS_testMethos"]
    test_simple_name = MTC_item["test_simple_name"]
    test_exe_dir = f"{test_file_path.split('/projects/')[0]}/projects/{poj_name}/AutoMR/test_exe/"
    file_processing.creatFolder_recursively_IfExistPass(test_exe_dir)
    MTC_IT_test_case_name = f"{test_simple_name}_IT"
    MTC_h_test_case_name = f"{test_simple_name}_h"

    # execute the MTCITrans_test
    Path_test_file = MTCITrans_only_test_class_file_path
    target_class_FQN = crafted_subject.MTCITrans_only_test_class_FQN
    Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log"
    Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
    if not result["compilation_MTCITrans_only"]:
        result["execution_MTC_ITrans_result"] = False
    elif (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = json_processing.read(Path_execution_result)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_IT_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_ITrans_result"] = False
    elif not (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_IT_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_ITrans_result"] = False
    else:
        print(f"Skip: {target_class_FQN} has been executed")

    # execute the MTCITrans_only_GTtest
    Path_test_file = MTCITrans_only_GTtest_class_file_path
    target_class_FQN = crafted_subject.MTCITrans_only_GTtest_class_FQN
    Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log"
    Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
    if not result["compilation_MTCITrans_only_GTtest"]:
        result["execution_MTC_ITrans_GTtest_result"] = False
    elif (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = json_processing.read(Path_execution_result)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_IT_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_ITrans_GTtest_result"] = False
    elif not (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_IT_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_ITrans_GTtest_result"] = False
    else:
        print(f"Skip: {target_class_FQN} has been executed")
    
    # execute the MTC_h_only_test
    Path_test_file = MTC_h_only_test_class_file_path
    target_class_FQN = crafted_subject.MTC_h_only_test_class_FQN
    Path_execution_log = f"{test_exe_dir}{target_class_FQN}.log"
    Path_execution_result = f"{test_exe_dir}{target_class_FQN}.json"
    if not result["compilation_MTC_h_only_test"]:
        result["execution_MTC_htest_result"] = False
    elif (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = json_processing.read(Path_execution_result)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_h_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_htest_result"] = False
    elif not (passIfexecuted and file_processing.pathExist(Path_execution_result)):
        EXE_RESULT = java_test.test_runner(poj_dir, jdk_version, target_class_FQN, Path_execution_log, Path_execution_result, Path_test_file, poj_build_tool=poj_build_tool,ifExeResult_skip=False, extra_cp=extra_cp)
        num_of_passed_test_cases =  EXE_RESULT[target_class_FQN]["num_of_passed_test_cases"]
        if num_of_passed_test_cases==0 or MTC_h_test_case_name not in EXE_RESULT[target_class_FQN]["passed_test_cases_list"]:
            print(f"Error, failed to execute: {target_class_FQN} ")
            result["execution_MTC_htest_result"] = False
    else:
        print(f"Skip: {target_class_FQN} has been executed")

    # print( f"result: {result}" )
    return result


def build_few_shot_base():
    import generate_Inputs_with_LLMs
    FEW_SHOT_BASE_DIR

    all_GT_MTCs = Profile_GT_MTCs_w_IT + Profile_GT_MTCs_wo_IT
    for MTC_item in all_GT_MTCs: 
        if "skip" in MTC_item and MTC_item["skip"] == True: continue
        FQS_testMethos = MTC_item["FQS_testMethos"]
        trans_class_def = generate_Inputs_with_LLMs.get_GT_Trans(MTC_item, type="class_definition")
        A = f"```java\n{trans_class_def}\n```"
        A_path = f"{FEW_SHOT_BASE_DIR}{FQS_testMethos}".split("(")[0]
        file_processing.write_TXTfile(A_path, A)
    # THEN, 手动矫正


# nohup python GT_processing.py > GT_processing.log 2>&1 &
if __name__ == "__main__":
    # build_few_shot_base()

    GT_result = {}
    all_GT_MTCs = Profile_GT_MTCs_w_IT + Profile_GT_MTCs_wo_IT
    # all_GT_MTCs = [Profile_GT_MTCs_wo_IT[-1]] # debug, for new subject
    # all_GT_MTCs = [Profile_GT_MTCs_w_IT[-1]] # debug, for new subject
    # all_GT_MTCs = Profile_GT_MTCs_w_IT[-2:] # debug, for new subject
    for MTC_item in all_GT_MTCs: 
        if "skip" in MTC_item and MTC_item["skip"] == True: continue
        if "org.threeten.extra.TestYearHalf.test_parse_CharSequenceDateTimeFormatter()" not in MTC_item["FQS_testMethos"] : continue # for debug
        print('Processing: ', MTC_item["FQS_testMethos"])

        """ 1. 将 GT ITrans function, MTC_ITrans 原 test case 拆分并保存  """
        # prepare_crafted_GT_MTC_class(MTC_item, withSuggestedDependencies=True)
        crafted_subject = prepare_crafted_GT_MTC_class_originalPoj(MTC_item, withSuggestedDependencies=False)
        # crafted_subject = copy_to_central_poj(crafted_subject) # TODO
        """ 1.1 编译/运行 拆分的 GT ITrans function 和 MTC_ITrans 原 test case  """
        compilation_exe_res = compile_and_execute_crafted_class(crafted_subject, passIfcompile=False, passIfexecuted=False)

        compilation_exe_res["withInputTransformation"] = MTC_item["withInputTransformation"]
        GT_result[ MTC_item["FQS_testMethos"] ] = compilation_exe_res
        
        """ 2. Evosuite: generate more test inputs (不靠谱，1-不如直接mutate 已有的 / 2-let GPT 进行mutate，哈哈哈哈哈哈)  """
        # test_IT.generate_test_cases_evosuite(MTC_item, skip_ESTest_generation=1) # generate tests for GT ITrans function
        # test_IT.generate_test_cases_in_original_poj(crafted_subject, skip_ESTest_generation=1) # generate tests for GT ITrans function
        # break
    json_processing.write(GT_result, f"{dir_GT_data}GT_result.json")
# nohup python -u GT_processing.py > GT_processing.log 2>&1 &