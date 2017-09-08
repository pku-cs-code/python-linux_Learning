#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, first_name, last_name):
        """Constructor"""
        self.first_name = first_name
        self.last_name = last_name

    # ----------------------------------------------------------------------
    @property
    def full_name(self):
        """
        Return the full name
        """
       # return "%s %s" % (self.first_name, self.last_name)

        print "%s %s" % (self.first_name, self.last_name)


person = Person('zhagn','cai')
person.full_name
person.first_name = 'zzz'
person.full_name


