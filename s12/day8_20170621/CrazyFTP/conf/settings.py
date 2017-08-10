#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

BIND_HOST = '0.0.0.0'
BIND_PORT = 9999

USER_HOME ='%s/var/users' %BASE_DIR
USER_ACCOUNT ={
    'alex':{'password':'alex123',
            'quotation':1000000,#1GB
            'expire':'2016-01-22'
            },
    'rain':{'password':'rain123',
            'quotation':2000000,
            'expire':'2016-01-22'

    }
}

if __name__ == '__main__':
    pass