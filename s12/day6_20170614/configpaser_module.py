#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.ConfigParser()
config["DEFAULT"] = {'ServerAliveInternal':'45',
                     'Compression':'yes',
                     'CompressionLevel':'9'

}
config['bitbucket.org'] = {}
config['bitbucket.org']['user'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini','w') as configfile:
    config.write(configfile)
