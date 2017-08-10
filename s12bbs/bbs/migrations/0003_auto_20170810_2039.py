# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20170810_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='head_img',
            field=models.ImageField(default=0, upload_to='', verbose_name='文章标题图片'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_type',
            field=models.IntegerField(choices=[(1, '评论'), (2, '点赞')], default=1),
        ),
    ]
