#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from app01 import models

class BookForm(forms.Form):
    name = forms.CharField(max_length=10)
    #publisher_id = forms.IntegerField(widget=forms.Select)#widget只是一个输入框
    publish_date = forms.DateField()


class BookModelForm(forms.ModelForm):
    class Meta:
        model = models.Book
        #fields = ('name','publish_date')
        exclude = ()

        widgets = {
            'name': forms.TextInput(attrs={'class':"form-control"}),
        }
