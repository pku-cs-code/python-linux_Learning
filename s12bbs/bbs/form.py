#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from bbs import models

class ArticleModelForm(ModelForm):

    class Meta:
        model = models.Article
        exclude = ('author','pub_date','priority')

    def __init__(self,*args,**kwargs):
        super(ArticleModelForm,self).__init__(*args,**kwargs)
        # self.fields['qq'].widget.attrs['class'] = 'form-control'#这一句话就加样式了
        # print("dir(self):---",dir(self))
        for field_name in self.base_fields:#把所有的字段取出来,把所有的字段取出来加样式
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class':'form-control'})

