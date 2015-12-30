#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib.request


class Compare_Virus(object):

    def __init__(self):
        self.virus_number = []

    def get_md5_list(self):
        f = open('virus_list.txt')
        self.md5_list = f.readlines()
        f.close()
        return self.md5_list

    def match_virus(self):
        for md5 in self.get_md5_list():
            url = 'http://localhost:9200/trojan_2015.12.14.220/trojan/_search?q=_id:' + md5[13:45]
            info = urllib.request.urlopen(url).read().decode('utf-8')
            if "virus_name" in info:
                self.virus_number.append(md5[13:45])
        Hits = len(self.virus_number) / len(self.md5_list)
        print('私有云匹配病毒个数:' + str(len(self.virus_number)) + '个')
        print('Data Package 命中率:' + "%.3f%%" % (Hits*100))

if __name__ == '__main__':
    compare = Compare_Virus()
    compare.match_virus()









