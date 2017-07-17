#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket#socket是一个标准库
ip_port = ('127.0.0.1',9999)#后面的9999一定是数字

sk =socket.socket()#声明tcp或者udp，默认是tcp
sk.bind(ip_port)
sk.listen(5)#最大允许连5个

while True:
    print("server waiting...")
    conn,addr = sk.accept()#等待链接进来，有链接过来就建立链接，没有就一直等待，addr是客户端地址
                            #客户端的ip和端口获取后生成一个实例，这个实例只为这个客户端服务，conn是实例
                            #有新的客户端连接则生成新的实例

    clien_data = conn.recv(1024)#1024是1024字节或者bit，2和3不一样
    print(str(clien_data,'utf8'))
    conn.sendall(bytes("不要回答，不要回答，不要回答",'utf-8'))

    conn.close()