#!/usr/bin/python
# -*- coding:utf-8 -*-

from matching import *
from functools import reduce
import os
import operator


class Generate_md5_list(object):

    def __init__(self, path):
        self.path = path

    def file_name(self, files):
        return [os.path.basename(f) for f in files]

    def get_md5_list(self):
        paths = [self.file_name(files)
                 for root, dirs, files in os.walk(self.path)
                 ]
        file_list = reduce(operator.add, paths)
        return file_list

if __name__ == '__main__':
    generate = Generate_md5_list("/home/developer/Downloads/share/bingdu")
    matching = Compare_Virus(generate.get_md5_list(), [])
    matching.match_virus()




