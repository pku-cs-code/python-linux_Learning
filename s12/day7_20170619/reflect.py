#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
class WebServer(object):
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def start(self):
        print("Server is starting...")

    def stop(self):
        print("Server is stopping..")

    def restart(self):
        self.stop()
        self.start()
def test_run(ins,name):
    print("running...",name,ins.host)

if __name__ == "__main__":
    server = WebServer('localhost',333)
    server2 = WebServer('localhost',333)
    #print(sys.argv[1])
    if hasattr(server,sys.argv[1]):
        function = getattr(server,sys.argv[1]) #获取server.start的内存地址
        function()  #server start
    # setattr(server,'run',test_run)#给实例绑定了一个test_run，只是在这个实例server里有
    # server.run(server,'zhang')
    #server2.run(server,'zhang')
    #delattr(server,'host')
    delattr(WebServer,'start')
    print(server.restart())
    """cmd_dic ={
        'start':server.start,
        'stop':server.stop,

    }
    if sys.argv[1] == "start":
        cmd_dic[sys.argv[1]]()
    """