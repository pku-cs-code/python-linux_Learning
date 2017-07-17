#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))#阻塞的链接
channel = connection.channel()#生成一个管道

#channel.queue_declare(queue='hello')#又定义一个队列，没有就新建一个，保证这个代码不出错。有就忽略了
                                      #防止关闭就没了
#channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):#回调函数，必须是定义为callback函数，必须这么定义。只要定义了callback函数，固定地会给它传这个参数
    #ch：channel，method：方法
    print("[x] Received %r" %body)

channel.basic_consume(callback,#消息到了之后执行callback函数
                      # queue='hello',
                      queue='task_q1',
                      no_ack=True#不需要确认，False可以保证一定被消费完毕。消费完毕后会给服务器端发送一个确认
                                 #no_ack=True设置后，消费者端停止后任务会丢失。可以设置为False确保消息不会丢失
                                 # 如果server端停止后，任务依然会丢失，可以设置durable=True确保queues和messages不会丢失，即使服务端停止
                                 #这是持久化操作。如果事先定义了一个queue没有durable，那么只有重新定义才可以。在消费者和生产者都需要加这个参数

                      )

print("[*] Waiting for messages. To exit press CTRL+C")
channel.start_consuming()#这是后开始接收，开始阻塞
