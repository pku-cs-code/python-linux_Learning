#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print("building secure connection chanel...")
    def handle(self):#handle是必须要定义的
        while True:
            print("New Conn:",self.client_address)
            data = self.request.recv(1024)
            if not data:break
            print("Client Says:",data.decode())
            self.request.send(data)
    def finish(self):
        print("client conn is done...")


if __name__ == '__main__':
    HOST,PORT = "localhost",50007
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()

