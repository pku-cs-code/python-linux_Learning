#!/usr/bin/env python
# -*- coding: utf-8 -*-


import optparse

from twisted.internet.protocol import ClientFactory, Protocol


def parse_args():
    usage = """ usage: %prog [options] [hostname]:port...
    This is the Get Poetry Now! client, Twisted version 3.0
    Run it like this:
    
    python get-poetry-1.py port1 port2 port3...

    """
    #python get-poetry-1.py port1 port2 port3...是说可以从多个服务器端收数据

    parser = optparse.OptionParser(usage)
    _, addresses = parser.parse_args()#前一个返回的数据不要，用_接收
    print('==addr:',_,addresses)

    if not addresses:
        print(parser.format_help())
        parser.exit()

    def parse_address(addr):
        if ":" not in addr:
            host = "127.0.0.1"#区分ip地址，可能是127.0.0.1:8000
            port = addr
        else:
            host, port = addr.split(':',1)#判断后面接的port有没有":"，没有则是本机
        if not port.isdigit():
            parser.error("Ports must be intergers.")
        return host, int(port)

    # return parse_address(addresses)
    return map(parse_address, addresses)#map把后面列表里的每一个值作为参数传到前面
    #map(lambda x:x*x,[1,2,3,4,5]返回[1,4,9,16,25]

class PoetryProtocol(Protocol):

    poem = ''
    def dataReceived(self, data):
        self.poem += data
        #self.factory = PoetryClientFactory#这是twisted自己写死的。子类调父类要经过factory
        print("[%s] recv:[%s]" %(self.transport.getPeer(),len(self.poem)))
    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):#不是twisted里的方法，是自己定义的
        self.factory.poem_finished(poem)#twisted，子类调父类

class PoetryClientFactory(ClientFactory):
    protocol = PoetryProtocol#handle method，protocal是关键字,需要这么写
    def __init__(self, callback):
        self.callback = callback
    def poem_finished(self,poem):
        self.callback(poem)
        #self.get_poem(poem)

def get_poetry(host, port, callback):
    """"dowmload a poem from given host and port and
    callback(poem) when the poem is complete.
    """
    from twisted.internet import reactor
    factory = PoetryClientFactory(callback)
    reactor.connectTCP(host, port, factory)

def poetry_main():
    addresses = parse_args()
    from twisted.internet import reactor
    poems = []

    def got_poem(poem):
        poems.append(poem)
        if len(poems) == len(addresses):
            reactor.stop()
    for address in addresses:
        host, port = address
        get_poetry(host, port, got_poem)
    reactor.run()

    print("---main done---")




if __name__ == '__main__':
    poetry_main()

