#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Arya.backends.base_model import BaseSaltModel

class CMD(BaseSaltModel):
    print('in cmd module')#会执行，写成__init__调用方法就不会自动执行了