#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import gevent
import socket
from gevent import socket,monkey
monkey.patch_all()#把各种网络接口库变为非阻塞的

def server(port):
    s = socket.socket()
    s.bind(('0.0.0.0',port))
    s.listen(5000)#最多监听5000个连接
    while True:
        cli, addr = s.accept()
        gevent.spawn(handle_request, cli,addr)#将cli客户端socket对象传给协程

def handle_request(s):
    try:
        while True:
            data = s.recv(1024)
            print("recv:",data)
            s.send(data)
            if not data:
                s.shutdown(socket.SHUT_WR)#把跟客户端的对象销毁。告诉客户端服务器要断开

    except Exception as ex:
        print(ex)
    finally:
        s.close()

if __name__ == "__main__":
    server(8001)

