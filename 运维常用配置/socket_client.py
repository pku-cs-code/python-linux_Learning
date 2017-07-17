#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
ip_port = ('127.0.0.1',9999)

sk =socket.socket()
sk.connect(ip_port)

sk.sendall(bytes('ÕÅrequests for occupying the Earth',encoding='utf-8'))

server_reply = sk.recv(1024)
print(str(server_reply,'utf8'))

while True:
    user_input = input(">>:").strip()
    sk.send(bytes(user_input,'utf8'))
    server_reply = sk.recv(1024)
    print(str(server_reply,'utf8'))

sk.close()
