#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys

messages = ['This is the message',
            'It will be sent',
            'in parts',

]

server_address = ('localhost',10001)

socks = [socket.socket(socket.AF_INET,socket.SOCK_STREAM),
         socket.socket(socket.AF_INET,socket.SOCK_STREAM),
         socket.socket(socket.AF_INET,socket.SOCK_STREAM),
         socket.socket(socket.AF_INET,socket.SOCK_STREAM),


]

print(sys.stderr,'connecting to %s port %s'%server_address)

for s in socks:
    s.connect(server_address)

for message in messages:
    #send messages on both sockets
    for s in socks:
        print(sys.stderr,'%s:sending"%s"'%(s.getpeername(),message))
        s.send(bytes(message,'utf8'))
    #read reponse on both sockets
    for s in socks:
        data = s.recv(1024)
        print(sys.stderr,'%s:received "%s"'%(s.getsockname(),data))
        if not data:
            print(sys.stderr,'closing socket',s.getsockname())
            s.close()

