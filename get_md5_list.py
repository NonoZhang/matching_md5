#!/usr/bin/python
# -*- coding:utf-8 -*-

from functools import reduce
import os
import operator


class Generate_md5_list(object):

    def __init__(self, path):
        self.path = path
        self.file_list = []

    def file_name(self, files):
        return [os.path.basename(f) for f in files]

    def get_md5_list(self):
        paths = [self.file_name(files)
                 for root, dirs, files in os.walk(self.path)
                 ]
        self.file_list = reduce(operator.add, paths)
        print(self.file_list)
        f = open('virus_list', "w")
        for file in self.file_list:
            f.writelines(file+'\n')
        f.close()
generate = Generate_md5_list("/home/developer/Downloads/share/bingdu")
generate.get_md5_list()





