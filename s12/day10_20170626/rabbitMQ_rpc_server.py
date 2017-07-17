#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()#生成一个管道

#在管道里声明一个queue
channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def on_request(ch, method, props, body):
    n = int(body)

    print("[.] fib(%s)" %n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,#回给客户端的queue
                     properties=pika.BasicProperties(correlation_id=\
                                                     props.correlation_id),#区别消息的标志，可能是同一个客户端给一个server发消息需要区分

                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)#同时只处理一个任务
channel.basic_consume(on_request, queue='rpc_queue')

print("[x] Awating RPC requests")
channel.start_consuming()#阻塞模式

