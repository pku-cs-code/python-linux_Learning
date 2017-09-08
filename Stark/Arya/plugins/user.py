#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Arya.backends.base_model import BaseSaltModel

class User(BaseSaltModel):

    def uid(self,*args,**kwargs):
        pass
    def gid(self):
        pass
    def shell(self):
        pass
    def home(self):
        pass

# class RedhatUser(User):
#     pass

class UbuntuUser(User):
    def home(self):
        print('in ubuntu home')




