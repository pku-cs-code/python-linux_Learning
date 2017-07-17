#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    try:
        num1 = input("num1:")
        num2 = input("num2:")
        a = range(10)
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        #a[11]
    except KeyboardInterrupt as e:
        print('entered ctrl+c')
    except EOFError as e:
        print('ctrl+D')
    except ValueError as e:#ÕûÊýÖµ³ö´í
        print("value err",e)
    except ImportError as e:
        print("index err",e)
    # except Exception, e:
    except Exception as e:#ÄÜ²¶×½ËùÓÐµÄÒì³£¡£ExpectionÊÇ´íÎóÀàÐÍ£¬exÒì³£´íÎóÐÅÏ¢
        print('³öÏÖÒì³££¬ÐÅÏ¢ÈçÏÂ£º')
        print(e)

