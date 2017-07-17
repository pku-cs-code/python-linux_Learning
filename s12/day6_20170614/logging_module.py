#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

"""
#logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s',datefmt='%m-%d-%Y %I:%M:%S %p')
#logging.basicConfig(format='%(asctime)s %(message)s',datefmt='%m-%d-%Y %I:%M:%S %p')
logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s',datefmt='%m-%d-%Y %H:%M:%S')

logging.debug('This debug message should go to the log file')
logging.info('So should this info')
logging.warning('And this too warning')
"""
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)
#logger.setLevel(logging.CRITICAL)

#creat console handler and set level to debug
ch = logging.StreamHandler()  #赋给屏幕
ch.setLevel(logging.DEBUG)
#creat file handler and set level to warning
fh = logging.FileHandler("access.log")#赋给文件
fh.setLevel(logging.WARNING)
#fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s',datefmt='%m-%d-%Y %H:%M:%S')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s',datefmt='%m-%d-%Y %H:%M:%S')

ch.setFormatter(formatter)
fh.setFormatter(formatter2)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')





