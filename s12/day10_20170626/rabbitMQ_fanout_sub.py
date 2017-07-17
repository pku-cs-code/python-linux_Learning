#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))#阻塞的链接
channel = connection.channel()#生成一个管道

channel.exchange_declare(exchange='logs',
                         type='fanout'#发布方不需要声明队列
                         )
result = channel.queue_declare(exclusive=True)#不指定queue名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',#把queue绑定到exchange才能接收消息
                    queue=queue_name
                    )

print("[*] Waiting for logs. To exit press CTRL+C")

def callback(ch, method, properties, body):
    print("[x] %r" %body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True
                      )

channel.start_consuming()

