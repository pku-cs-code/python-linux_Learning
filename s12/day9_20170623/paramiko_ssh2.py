#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko

transport = paramiko.Transport(('192.168.31.60',52113))
transport.connect(username='zhangcai',password='123456')

ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
print(stdout.read())

transport.close()

