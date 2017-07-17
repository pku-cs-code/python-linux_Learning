#!/usr/bin/env python
#coding:utf-8
## -*- coding: utf-8 -*-

import socket
ip_port = ('127.0.0.1',9999)

sk =socket.socket()
sk.bind(ip_port)
sk.listen(5)

while True:
    print("server waiting...")
    conn,addr = sk.accept()

    client_data = conn.recv(1024)
    print(str(client_data,'utf8'))
    #print(clien_data)
    conn.sendall(bytes('dont answer', 'utf-8'))
    while True:
            client_data = conn.recv(1024)
            print('recv:',str(client_data,'utf8'))
            if not client_data:break
            conn.send(client_data)
            #server_response = input("\033[32;1m>>:\033[0m").strip()
            #conn.send(bytes(server_response,'utf8'))
    conn.close()
