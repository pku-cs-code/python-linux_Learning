#!/usr/bin/env python

import sys
#cur_path=sys.path
#print(cur_path)
import os
#print(__file__)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from config import settings


def db_auth(configs):
    if configs.DATABASE["user"] == 'root' and configs.DATABASE["password"] == '123':
        print("db authentication passed!")
        return True
    else:
        print("db auth error...")

def select(table,column):
    if db_auth(settings):
        if table == 'user':
            user_info = {
                "001":['alex',22,'engineer'],
                "002":['alex2',23,'chef'],
                "003":['alex3',25,'police'],
            }
            return user_info
    else:
        return None
