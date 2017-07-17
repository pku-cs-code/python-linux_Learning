#!/usr/bin/env python
#coding:utf-8
## -*- coding: utf-8 -*-

import socket
import subprocess
ip_port = ('127.0.0.1',9999)

sk =socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server waiting...")
    conn,addr = sk.accept()
    while True:
            client_data = conn.recv(1024)
            if not client_data:break
            print('recv:cmd ',str(client_data,'utf8'))
            cmd = str(client_data,'utf-8').strip()
            cmd_result = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
            conn.send(cmd_result.stdout.read())
            #server_response = input("\033[32;1m>>:\033[0m").strip()
            #conn.send(bytes(server_response,'utf8'))
    conn.close()
