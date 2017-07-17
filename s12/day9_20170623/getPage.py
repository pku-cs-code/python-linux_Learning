#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent import monkey;monkey.patch_all()
import  gevent
#from urllib2 import urlopen
from urllib.request import urlopen

def f(url):
    print('GET: %s'%url)
    resp = urlopen(url)
    data = resp.read()
    print("%d bytes received from %s."%(len(data),url))

gevent.joinall([
    gevent.spawn(f,'https://www.python.org'),
    gevent.spawn(f,'https://www.baidu().com'),
    gevent.spawn(f,'https://github.com'),
]
)
