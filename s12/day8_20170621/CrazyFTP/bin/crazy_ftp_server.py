#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from modules import main

if __name__ == '__main__':
    Entrypoint = main.ArgvHandler(sys.argv)#处理参数
