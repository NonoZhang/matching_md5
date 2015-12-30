#!/usr/bin/python
# -*- coding:utf-8 -*-

from VIrusMd5List import *
import urllib.request


class Compare_Virus(object):

    def __init__(self, md5_list, virus_number):
        self.md5_list = md5_list
        self.virus_number = virus_number

    def match_virus(self):
        for md5 in self.md5_list:
            url = 'http://localhost:9200/trojan_2015.12.14.220/trojan/_search?q=_id:' + md5.lower()
            info = urllib.request.urlopen(url).read().decode('utf-8')
            if "virus_name" in info:
                self.virus_number.append(md5.lower)
        print(self.virus_number, len(self.virus_number))








