#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host="192.168.31.60")
        self.chan_sub = 'fm104.5'#d订阅
        self.chan_pub = 'fm88.8'#发布

    def public(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()#打开收音机
        pub.subscribe(self. chan_sub)#拧到那个台
        pub.parse_response()#准备听
        return pub
