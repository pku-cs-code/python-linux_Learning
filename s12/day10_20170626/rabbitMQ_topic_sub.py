#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',
                         type='topic')

result = channel.queue_declare(exclusive=True)#不指定queue名字，rabbit会随机分配一个名字，exclusive=True会在使用此queue的消费者断开后，自动将queue删除
queue_name = result.method.queue

binding_keys = sys.argv[1:]#跟一个或者多个参数
if not binding_keys:
    sys.stderr.write("Usage: %s [binding_key]...\n"%sys.argv[0])
    sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(exchange='topic_logs',
                       queue=queue_name,
                       routing_key=binding_key)#一个queue绑定了多个routing_key

print("[*] Waiting for logs. To exit press CTRL+C.")

def callback(ch, method, properties, body):
    print("[x] %r:%r"%(method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()