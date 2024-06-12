# -*- coding: utf-8 -*-

"""
Created on 2020-01-06 15:39  

@author:  
"""

import json


def write(json_content, path, has_indent=True):
    with open(path, 'w+') as f:
        f.write(json.dumps(json_content, indent=(4 if has_indent else None)))


def read(path):
    with open(path, 'r') as f:
        content = json.loads(f.read(), strict=False)
        return content
