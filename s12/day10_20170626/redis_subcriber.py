#!/usr/bin/env python
# -*- coding: utf-8 -*-

from redis_helper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg = redis_sub.parse_response()#真正听
    print(msg)#有消息就打印没消息阻塞

