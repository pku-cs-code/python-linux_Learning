# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

import models

admin.site.register(models.Customer)
admin.site.register(models.ConsultantRecord)
admin.site.register(models.ClassList)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.UserProfile)
admin.site.register(models.Course)
admin.site.register(models.School)




