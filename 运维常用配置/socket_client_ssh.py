#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
ip_port = ('127.0.0.1',9999)

sk =socket.socket()
sk.connect(ip_port)

while True:
    user_input = input("cmd:").strip()
    sk.send(bytes(user_input,'utf8'))
    server_reply = sk.recv(1024)
    print(str(server_reply,'utf8'))

sk.close()
