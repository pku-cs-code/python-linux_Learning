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
    except ValueError as e:#����ֵ����
        print("value err",e)
    except ImportError as e:
        print("index err",e)
    # except Exception, e:
    except Exception as e:#�ܲ�׽���е��쳣��Expection�Ǵ������ͣ�ex�쳣������Ϣ
        print('�����쳣����Ϣ���£�')
        print(e)

