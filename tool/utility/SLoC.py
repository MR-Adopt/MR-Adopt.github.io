#!/usr/bin/env python
# encoding: utf-8
"""

Created on 2019/10/16 12:27
@Author :  


# https://stackoverflow.com/questions/38543709/count-lines-of-code-in-directory-using-python
"""

import pathlib


class LoC(object):
    # suffixes = ['.py','.java']

    def count(self, path: pathlib.Path, suffixes, init=True):
        self.suffixes = suffixes
        if init:
            self.root = path
            self.files = 0
            self.lines = 0
        if path.is_dir():
            # recursive case
            for item in path.iterdir():
                self.count(path=item, suffixes=self.suffixes, init=False)
        elif path.is_file() and path.suffix in self.suffixes:
            try:
                # base case
                with path.open(mode='r',encoding="ISO-8859-1") as f:
                    line_count = len(f.readlines())
                # print(f'{path.relative_to(self.root)}: {line_count}')
                self.files += 1
                self.lines += line_count
            except Exception:
                    print("openfile, Exception:", file_path)
        if init:
            # print(f'\n{self.lines} lines in {self.files} files')
            return {"lines":self.lines, "files":self.files}

loc = LoC()
# res = loc.count(path=pathlib.Path('/home1/ /data/AutoMR/projects/'), suffixes=[".java"] )
# print(res)

def get_Loc(path_or_dir,suffixes=[".java"]):
    return loc.count(path=pathlib.Path(path_or_dir), suffixes=suffixes )