#!/usr/bin/env python
# -*- coding: utf-8 -*-


from twisted.internet import protocol
from twisted.internet import reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):#还要twisted一收到数据就会调用此方法
        self.transport.write(data)#把收到的数据返回给客户端

def main():
    factory = protocol.ServerFactory()#定义基础工厂
    factory.protocol = Echo#处理socket的方法

    reactor.listenTCP(9000,factory)
    reactor.run()

if __name__ == '__main__':
    main()

