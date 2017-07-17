#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pika
import uuid

class FibonacchiRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,#basic_consume先声明要监听哪个queue。
                                   queue=self.callback_queue)#callback_queue是随机的

    def on_response(self, ch, method, props, body):#相当于回调
        if self.corr_id == props.correlation_id:#传输和返回的queue不一样，防止交叉出错
            self.response = body

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to = self.callback_queue,#回复server端时的queue
                                       correlation_id = self.corr_id,#识别client端回复的标志
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()#只要self.response为None，就不断去queue里接收
        return int(self.response)



fibonaci_rpc = FibonacchiRpcClient()

print("[x] Requesting fib(30)")
response = fibonaci_rpc.call(30)
print("[.] Got %r" %response)

