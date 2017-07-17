#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')
result = channel.queue_declare(exclusive=True)#不指定queue名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue

severities = sys.argv[1:]#绑定一个或多个队列
if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n"%sys.argv[0])
    sys.exit(1)

for severity in severities:#队列里绑定多个routing_key,相当于检测多个路由
    channel.queue_bind(exchange='direct_logs',
                       queue=queue_name,
                       routing_key=severity)

print("[*] Waiting for logs. To exit press CTRL+C.")

def callback(ch, method, properties, body):
    print("[x] %r:%r"%(method.routing_key,body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()



