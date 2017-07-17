#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading

def run(n):
    HOST = 'localhost'
    PORT = 8001

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    #while True:
    #msg = bytes(input(">>:"),encoding="utf8")
    msg = bytes(str(n),encoding="utf8")
    #if len(msg) == 0:continue
    s.sendall(msg)
    data = s.recv(1024)

    print("Received.",repr(data))


    s.close()

res_list = []
for i in range(10000):#并发10000个线程
    t = threading.Thread(target=run,args=[i,])
    t.start()
    res_list.append(t)

for r in res_list:
    r.join()

