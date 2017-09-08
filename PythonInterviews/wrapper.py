#!/usr/bin/env python
# -*- coding: utf-8 -*-


def login(func):
    def wrapper(*args,**kwargs):
        print("wrapper test")

        return func()


    return wrapper

@login
def func():
    print('use wrapper test')

if __name__ == '__main__':


    func()

