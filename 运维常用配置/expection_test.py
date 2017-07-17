#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    num1 = input("num1:")
    num2 = input("num2:")
    a = range(10)
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        a[11]
    except ValueError as e:#整数值出错
        print("value err",e)
    except ImportError as e:
        print("index err",e)
    # except Exception, e:
    except Exception as e:#能捕捉所有的异常。Expection是错误类型，ex异常错误信息
        print('出现异常，信息如下：')
        print(e)

