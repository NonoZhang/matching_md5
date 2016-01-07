#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import pycurl
import json
import time
import tarfile
import requests
import sys

class ImportData(object):

    def getInfo(self, command):
        imageId = os.popen(command + "| grep elasticsearch | awk '{print $1}'").readlines()
        return imageId

    def create_image(self):
        # stating docker
        print('starting docker.....')
        if self.getInfo('docker images') == []:
            os.popen('docker build -t "elasticsearch" /home/developer/elasticData').readlines()
            print(" building images successful")
            os.system("docker run -d -p 9200:9200 elasticsearch")

        else:
            if self.getInfo('docker ps') == []:
                os.system("docker run -d -p 9200:9200 elasticsearch")
                print(" starting a docker successful")

    def mount(self):
        url = 'http://localhost:9200/_snapshot/my_backup'
        data = json.dumps({
        "type": "fs",
        "settings": {
            "location": "/backups/my_backup",
            "compress": True
            }
        })
        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.CUSTOMREQUEST, 'PUT')
        c.setopt(pycurl.POSTFIELDS, data)
        c.perform()
        c.close()

    def mountDockerToLocal(self):
        a = self.getInfo('docker ps')[0]
        os.popen('docker stop'+' '+ a.replace('\n','')).readlines()
        os.popen('docker run -v /home/developer/elasticData/:/backups/my_backup -p 9200:9200 -d elasticsearch').readlines()
        time.sleep(10)
        self.mount()
        print("~~~~~~~~", 'i am ok')

    def unZip(self, raw_tar='raw.tar', trojan_tar='trojan.tar.gz'):
        filePath = sys.argv[2]
        tar = tarfile.open(filePath)
        tar.extract(raw_tar, path='/tmp')
        tar1 = tarfile.open('/tmp/' + raw_tar)
        tar1.extract(trojan_tar, path='/tmp')
        tar2 = tarfile.open('/tmp/'+trojan_tar)
        for name in tar2.getnames():
            tar2.extract(name, path='/home/developer/elasticData/')
        tar.close()

    def elastic(self):
        url = 'http://localhost:9200/_snapshot/my_backup/trojan/_restore'
        re = requests.post(url)
        time.sleep(15)
