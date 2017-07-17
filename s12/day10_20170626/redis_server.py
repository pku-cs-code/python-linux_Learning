#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

r = redis.Redis(host="192.168.31.60")
r.publish("fm104.5","hello ok?")

r.publish("fm104.5","test1")
