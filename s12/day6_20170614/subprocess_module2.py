#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

cmd = subprocess.run("ipconfig")
cmd = subprocess.Popen("ipconfig",stdout=subprocess.PIPE)
#cmd = subprocess.Popen("ipconfig",shell=True,stdout=subprocess.PIPE)

print(cmd)