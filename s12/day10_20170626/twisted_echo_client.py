#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twisted.internet import reactor,protocol

class EchoClient(protocol.Protocol):

    def connectionMade(self):#链接一建立成功就会自动调用此方法
        print("connection is built, sending data..")
        self.transport.write(b'hello zhang!')

    def dataReceived(self, data):
        print("server said:",data)
        self.transport.loseConnection()#有数据没传完它会传完了再给你关闭

    def connectionLost(self, reason):
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient#类似socket中的handler

    def clientConnectionFailed(self, connector, reason):
        print("connection failed - bye")
        reactor.stop()
    def clientConnectionLost(self, connector, reason):
        print("connection lost - bye")
        reactor.stop()

def main():
    f = EchoFactory()
    reactor.connectTCP('localhost',9000,f)
    reactor.run()

if __name__ == '__main__':
    main()


