#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

# transport = paramiko.Transport(('hostname',22))
# transport.connect()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.31.60',port=52113,username='zhangcai',password='123456')

stdin,stdout,stderr = ssh.exec_command('df')
#result = stdout.read()
result =list(filter(lambda x: x is not None,[stdout.read(),stderr.read()]))#lambda表达式意思是不为空则留在这个列表里
print(result)
ssh.close()