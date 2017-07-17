#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    count = 10
    def __init__(self,name):
        self.name = name
        self.num = None
        #self.__num = None  #私有属性，外部不可以访问
    hobbie = "meat"

    @classmethod
    def talk(cls):
        print("%s is talking..." %cls.hobbie)
    #@staticmethod
    #def talk():




"""
    #@property
    #def total_players(self):
"""
