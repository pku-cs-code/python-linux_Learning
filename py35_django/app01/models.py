from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)#后面的最大长度是必须设置的
    password = models.CharField(max_length=32)
    age = models.IntegerField()