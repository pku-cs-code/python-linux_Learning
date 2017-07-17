#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config.read('example.ini')
#改写
# sec = config.remove_section('topsecret.server.com')
# config.write(open('example2.cfg','w'))

sec = config.has_section('alex')
# sec = config.has_section('bitbucket.org')
# print(sec)
if sec == False:
    config.add_section('alex')
    config['alex']['age'] = '21'
config.write(open('example2.ini','w'))

# config.set('alex','age','22')
# config.write(open('example2.ini','w'))

# config.remove_option('alex','age')
config.remove_section('alex')

config.write(open('example2.ini','w'))

