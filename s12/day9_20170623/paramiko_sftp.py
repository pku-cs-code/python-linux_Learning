#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

transport = paramiko.Transport(('192.168.31.60',52113))
#transport.connect(username='zhangcai',password='123456')
transport.connect(username='root',password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put('D:\\test\\test.txt','/tmp/test.py')#将location.py上传至test.py
#sftp.get('remote_path','local_path')#获取或者传输文件，记住是文件
sftp.get('/tmp/test.py','D:\\test\\linux.txt')

transport.close()
