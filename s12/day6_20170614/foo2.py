#!/usr/bin/env python
# -*- coding: utf-8 -*-


from foo import *
from foo import _bar,__bar
if __name__ == '__main__':
    print locals()
