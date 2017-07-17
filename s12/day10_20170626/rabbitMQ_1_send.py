#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()#生成一个管道

#在管道里声明一个queue
#channel.queue_declare(queue='hello')
channel.queue_declare(queue='task_q1',durable=True)#如果注释掉这行代码，没有声明queue，代码可能出错，此时durable设置为True
#已经存在的queue，再声明为durable会报错
#设置queue为持久化后，关闭rabbitMQ服务端，再启动，客户端可以识别到这个queue，但之前的消息会丢失，只会持久化queue
#如果需要对message持久化，可以加入参数
#这个版本的rabbitMQ好像是默认message和queue都持久化了。关闭recv端，当服务端新建queue持久化，运行send端程序，关闭rabbitMQ后
#再启动，recv端程序queue设置为服务端对应的queue，启动recv端，这时能收到消息，说明queue和message都是对应上了的



#向队列里发数据，不能直接往queue里发数据，得先把数据放入管道，有点像路由器，exchange可以过滤消息，默认用default过滤器
channel.basic_publish(exchange='',
                      routing_key='task_q1',#往哪个queue里发数据
                      body='Hello World_task_q12!'
)#消息想持久化加上delivery_mode = 2，delivery_mode模式有二十多种
print("[x] Sent 'hello world!'")
connection.close()
