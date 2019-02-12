# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    management_work = models.CharField(max_length=50, verbose_name=u"分管工作", default="")
    gender = models.CharField(max_length=6, choices=(("male",u"男"),("female","女")), default="female")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username