# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-09 07:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'permissions': (('can_del_customer', '\u53ef\u4ee5\u5220\u9664\u7528\u6237'),)},
        ),
    ]