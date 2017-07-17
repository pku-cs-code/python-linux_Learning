#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

def run(n):
    print('[%s]-----running----\n'%n)
    time.sleep(2)
    print('---done---')
def main():
    for i in range(5):
        t = threading.Thread(target=run,args=[i,])

        t.start()
        #t.join(1)
        print('starting thread',t.getName())


m =threading.Thread(target=main,args=[])
m.setDaemon(True)#将主线程设置为daemon时，它退出时其他子线程都会退出
m.start()
m.join(timeout=3)#如果timeout设置为3，则不阻塞了。设置为daemon后join后就不好使了

print('main thread is alive:',m.is_alive())
print('---main thread done---')

#print()

