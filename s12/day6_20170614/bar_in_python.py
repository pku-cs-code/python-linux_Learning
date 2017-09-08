#!/usr/bin/env python
# -*- coding: utf-8 -*-



class Foo(object):
    boo = 40
    _boo = 50
    __boo = 60  # _Foo__boo
    def __init__(self):
        self.__booo = 70

    def __test(self):   #_Foo__test
        print "__test"

if __name__ == '__main__':
    print Foo.boo
    print Foo._boo
    #print Foo.__boo
    print Foo._Foo__boo
    foo = Foo()
    print('result of foo._boo:', foo._boo)
    print foo._Foo__booo
    foo._Foo__test()


