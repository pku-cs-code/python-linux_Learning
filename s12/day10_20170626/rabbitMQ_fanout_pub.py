#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()#生成一个管道

#在管道里声明一个queue
#channel.queque_declare(queue='hello')

channel.exchange_declare(exchange='logs',
                         type='fanout'#发布方不需要声明队列
                         )

message = ' '.join(sys.argv[1:]) or "info: Hello World!"#脚本执行发消息。没指定则发送info
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message

)

print("[x] Sent %r" %message)
connection.close()

