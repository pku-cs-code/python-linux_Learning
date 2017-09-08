#!/usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):
    def foo(self,x):
        print "executing foo(%s,%s)"%(self,x)

    @classmethod
    def class_foo(cls,x):
        print "executing class_foo(%s,%s)"%(cls,x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)"%x
    @staticmethod
    def static_foo2():
        print "'test static_foo2"

# A.static_foo2()
a=A()
#class_foo(A,'test')
A.class_foo('A.class_foo:')
a.class_foo('class_foo test')
# a.static_foo('stattic_method_test_without_class')
# A.static_foo('test_static_method')
# a.static_foo('test')
# a.static_foo2()
# A.static_foo2()

