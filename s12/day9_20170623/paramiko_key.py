#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.31.60',port=52113,username='zhangcai',key_filename=private_key)

stdin, stdout, stderr = ssh.exec_command('df')
result = stdout.read()

ssh.close()