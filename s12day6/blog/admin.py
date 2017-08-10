# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models

# Register your models here.

class EntryAdmin(admin.ModelAdmin):
    list_display = ('blog','headline','pub_date','mod_date','n_comments','n_pingbacks',)


admin.site.register(models.Author)
admin.site.register(models.Blog)
# admin.site.register(models.Entry)
admin.site.register(models.Entry,EntryAdmin)