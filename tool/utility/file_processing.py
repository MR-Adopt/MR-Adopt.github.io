#!/usr/bin/env python
# encoding: utf-8
"""

Created on 2019/10/16 12:27
@Author :  

用于进行文件相关操作
"""
import os,sys
import os.path
import shutil
import tarfile
import time

# rootdir -> list: all file full name
def walk_FileDir(rootdir):
    #rootdir = "d:/code/su/data"  # 指明被遍历的文件夹
    file_list = []
    #dfs
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for dirname in dirnames:  # 输出文件夹信息
        #     print ("parent is:" + parent)
        #     print("dirname is" + dirname)

        for filename in filenames:  # 输出文件信息
            full_name = os.path.join(parent, filename)
            file_list.append(full_name)
        #     print("parent is:" + parent)
        #     print("filename is:" + filename)
        #     print("the full name of the file is:" + os.path.join(parent, filename) ) # 输出文件路径信息
    return file_list

# rootdir -> list: all dir full name
def walk_allDirs(rootdir):
    #rootdir = "d:/code/su/data"  # 指明被遍历的文件夹
    dir_list = []
    #dfs
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for dirname in dirnames:  # 输出文件夹信息
        #     print ("parent is:" + parent)
        #     print("dirname is" + dirname)

        for dirname in dirnames:  # 输出文件信息
            full_name = os.path.join(parent, dirname)
            dir_list.append(full_name)
        #     print("parent is:" + parent)
        #     print("filename is:" + filename)
        #     print("the full name of the file is:" + os.path.join(parent, filename) ) # 输出文件路径信息
    return dir_list


# rootdir -> list: all Folders in Level 1
def walk_L1_Folders(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        return dirnames

# rootdir -> list: all filenames in Level 1
def walk_L1_FileNames(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        return filenames

def walk_L1_FoldersAndFilenames(rootdir):
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字

        return dirnames + filenames


def creatFileFolder(path):
    # if os.path.exists(path):
    #     shutil.rmtree(path)
    return os.mkdir(path)

def creatFolder_IfExistPass(path):
    if os.path.exists(path):
        return -1
    else:
        try:
            os.mkdir(path)
            print(f"Directory {path} was created successfully.")
        except OSError as error:
            print(f"Creating directory {path} failed. Error: {error}")

def creatFolder_recursively_IfExistPass(path):
    if os.path.exists(path):
        return -1
    else:
        try:
            os.makedirs(path)
            print(f"Directory {path} was created successfully.")
        except OSError as error:
            print(f"Creating directory {path} failed. Error: {error}")


def creatFolder_IfExistRM(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    return os.mkdir(path)


def moveFile(srcfile, dstfile):
    if not os.path.isfile(srcfile):
            print( "%s not exist!" % (srcfile))
            return ( "%s not exist!" % (srcfile) +'\n')
    else:
            fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)  # 创建路径
            shutil.move(srcfile, dstfile)  # 移动文件
            # print("move %s -> %s " % (srcfile, dstfile))
            return ("move %s -> %s " % (srcfile, dstfile)+'\n')
def moveFile_DSTexistsPass(srcfile, dstfile):
    if not os.path.isfile(srcfile):
            print( "%s not exist!" % (srcfile))
            return ( "%s not exist!" % (srcfile) +'\n')
    elif os.path.exists(dstfile): #文件已存在
        print(dstfile+" exists, from " + srcfile)
        return (dstfile+" exists, from " + srcfile +'\n')
    else:
            fpath, fname = os.path.split(dstfile)  # 分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)  # 创建路径
            shutil.move(srcfile, dstfile)  # 移动文件
            # print("move %s -> %s " % (srcfile, dstfile))
            return ("move %s -> %s " % (srcfile, dstfile)+'\n')

def copyFile(source,target):
    # source = 'current/test/evaluation.py'
    # target = '/prod/new'

    # # assert not os.path.isabs(source)
    # target = os.path.join(target, os.path.dirname(source))

    # # create the folders if not already exists
    # os.makedirs(target)

    # adding exception handling
    try:
        shutil.copy(source, target)
    except IOError as e:
        print("Unable to copy file. %s" % e)
    except:
        print("Unexpected error:", sys.exc_info())
    print("LOG: copy %s -> %s " % (source, target))
        
def copyFolder(source_path,target_path):
    try:
        shutil.copytree(source_path, target_path)
        return 0
    except IOError as e:
        # print("Unable to copy file. %s" % e)
        pass
    except:
        print("Unexpected error:", sys.exc_info())
    return -1

def copyFolder_deleteOld(source_path,target_path):
    if os.path.exists(target_path):
        deleteFolder(target_path)

    copyFolder(source_path,target_path)


def deleteFolder(dir):
    shutil.rmtree(dir, True)  # 最后删除img总文件夹

def remove_file(path):
    if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        os.remove(path)
        # os.unlink(path)
        return 1
    else:
        print('remove_file: no such file:%s' % path)  # 则返回文件不存在
        return 0

def remove_folder(path):
    if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        shutil.rmtree(path)
        # os.unlink(path)
        return 1
    else:
        print('remove_folder: no such folder:%s' % path)  # 则返回文件不存在
        return 0

import tarfile
def untarFile(fname, dirs):
    tar = tarfile.open(fname)
    names = tar.getnames()
    for name in names:
        try:
            tar.extract(name, path=dirs)
        except Exception as e:
            print(e)
            # pass

    tar.close()


def read_TXTfile(path):
    with open(path,'r') as f :
        content = f.read()
        return content

def read_TXTfile_encoding_iso(path):
    # 因为有什么回报错：UnicodeDecodeError: 'utf-8' codec can't decode byte 0xcd in position 15
    with open(path,'r',encoding="ISO-8859-1") as f :
        content = f.read()
        return content

def write_TXTfile(path,content):
    try:
        with open(path,'w') as f :
            f.write(str(content, encoding = "utf-8"))
            # f.write(content.encode("utf-8"))
    except TypeError:
        write_TXTfile_no_encode(path, content)

def write_TXTfile_no_encode(path,content):
    with open(path,'w') as f :
        f.write(content)

def write_TXTfile_encode_utf8(path,content):
    with open(path,'w') as f :
        # f.write(str(content, encoding = "utf-8"))
        f.write(content.encode("utf-8"))

# https://blog.csdn.net/Areigninhell/article/details/86519077
def getFileSize(filepath):
    size = os.path.getsize(filepath)
    return size

# https://blog.csdn.net/thomaswu1992/article/details/90477482
def TimeStampToTime(timestamp):
    timeStruct = time.localtime( timestamp)
    return time.strftime( '%Y-%m-%d %H:%M:%S', timeStruct )

def getFileCreatedTime(filepath):
    t = os.path.getmtime(filepath)
    return TimeStampToTime(t)

def getFolderSize(folderpath):
    size=0
    for root, dirs, files in os.walk(folderpath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
    return size

def pathExist(path):
    return os.path.exists(path) # True/False

def makedirs_moreLevels(path): # 创建多级目录
    return os.makedirs(path)

def renameFile(srcFile, dstFile):
    # srcFile = './actwork/linkFile/allExtLinks - 副本.txt'
    # dstFile = './actwork/linkFile/allExtLinks - copy.txt'
    try:
        os.rename(srcFile, dstFile)
    except Exception as e:
        print(e)
        print('rename file fail\r\n')
        return -1
    print('rename file success\r\n')
    return 1

def retrieve_fileName_with_keyword(Keyword, dir):
    all_file_list = walk_FileDir(dir)
    result_file_full_name = []
    for ele in all_file_list:
        filename = ele.split("/")[-1]
        if Keyword in filename:
            result_file_full_name.append(ele)
    return result_file_full_name

# import yaml
# def read_yml(file_path):
#     with open(file_path) as f:
#         return yaml.load(f)

# if __name__ == '__main__':
#     walk_FileDir('e:/libs')
#     # creatFileFolder('e:/Jars-MD5/AAA/')

if __name__ == '__main__':
    # list_file = retrieve_fileName_with_keyword("OriginalMRcases.java", "/home1/  /data/AutoMR/projects/OpenHFT__split__Chronicle-Core/")
    # for ele in list_file:
    #     print(ele)
    
    # path = "  TODO/data/ITrans/cache/generateInputs/WizardCoder-15B-V1.0_Ti4-2_Temprature0.2_1/generated_inputs/VersionTest_isLowerThanTest_h1Test.java"
    # poj_ITRANS_GENERATED_LLMI_TEST_DIR = "  TODO/data/ITrans/projects/datageartech__split__datagear/ITrans/generated_inputs/LLMI_test_Trans/"
    # copyFile(path, poj_ITRANS_GENERATED_LLMI_TEST_DIR)

    # source = "  TODO/data/ITrans/projects/dromara__split__hutool/ITrans/generated_inputs/w/cn/hutool/json/IssueI7GPGXTest_toBeanTest_h1Test$1.class"
    # target = "  TODO/data/ITrans/cache/generateInputs/WizardCoder-15B-V1.0_Ti4-2_Temprature0.2_1/generated_inputs/IssueI7GPGXTest_toBeanTest_h1Test$1.class"
    # copyFile(source,target)
    pass
