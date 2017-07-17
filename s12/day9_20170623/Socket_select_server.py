#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import sys
#import Queue
import queue


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建一个ssocket
server.setblocking(0)#不阻塞，不管recv或者send都不阻塞。0，False

server_address = ('localhost',10001)
print(sys.stderr,'starting up on %s port %s' %server_address)
server.bind(server_address)
server.listen(5)

#select()方法接收并监控3个通信列表，第一个是所有的输入的data，就是外部要发过来的数据
#第二个是输出，第三个是错误信息

#sokets from which we expect to read
inputs = [ server ]
#sockets to which we expect to write
outputs = [ ]#空列表

#outgoing message queues(socket:Queue)
message_queues = {}

while inputs:#客户端所有的input都放到server中了
    print('\nwaiting for the next event')
    readable, writable, exceptional = select.select(inputs,outputs,inputs)#有数据过滤就变成活跃的了
    #readable, writable, exceptional = select.select(inputs, outputs, inputs,2)#设置超时为2秒
    #输出要么正确，要么错误。不知道哪个出错了所以都放在select，让select挑错
    #当把inputs、outputs、excepal（这里跟inputs共用）传给select后，它返回3个list，我们赋值为readable, writable, exceptional
    #readable list代表有数据可以接收，writable list代表里面存放着的数据可以send，连接出错时会放到exceptional中
    #readable list有三种可能状态，第一种是main  server socket，代表server端已经ready来接收新的连接

    #为了能让main server同时处理过个连接，下面吧mian server的socket设为非阻塞模式
    #handle inputs
    for s in readable:
        if s is server:#返回的server说明是就绪的，因为有新连接才会就绪，就绪说明一定是有新客户端连接过来
            connection, client_address = s.accept()#有新连接就接收进来
            print(sys.stderr,"new connection from",client_address)
            connection.setblocking(0)
            inputs.append(connection)#先把数据存起来，防止接收不到其他连接数据。返回了说明接收了数据

            message_queues[connection] = queue.Queue()#发过来的数据都存在队列里，是单一连接独有的一个que
        else:#不是新连接则是一个有数据的连接
            data = s.recv(1024)
            if data:
                print(sys.stderr,'received "%s" from %s' %(data,s.getpeername()))
                message_queues[s].put(data)#data放到队列里
                if s not in outputs:
                    outputs.append(s)
            else:#没收到数据的情况
                print('closing',client_address,'after reading no data')
                if s in outputs:
                    outputs.remove(s)#客户端断开了就不用给它返回数据了
                inputs.remove(s)#inputs中也删除掉
                s.close()#关闭这个连接
                del message_queues[s]#删除队列


    for s in writable:
        try:
            netx_msg = message_queues[s].get_nowait()#获取数据
        except queue.Empty:#获取不到数据
            print('output queue for',s.getpeername(),'is empty')
            outputs.remove(s)
        else:#获取到数据
            print('sending "%s" to %s'%(netx_msg,s.getpeername()))
            s.send(netx_msg)

    for s in exceptional:#异常
        print('handling exceptional condition for',s.getpeername())
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        del message_queues[s]















