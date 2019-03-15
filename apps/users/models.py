# _*_ encoding:utf-8 _*_
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Q

# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="姓名", default="")
    job = models.CharField(max_length=50, verbose_name="职务",
                           choices=(("1", "工班长"), ("2", "安全员"), ("3", "物资员"), ("4", "综合管理员"), ("5", "宣传员"), ("0", "无")),
                           default="0", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(("male", "男"), ("female", "女")), default="male")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="", max_length=100,blank=True,null=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


    def message_nums(self):
        from apps.todolists.models import Todo
        return Todo.objects.filter(Q(member_name__icontains=self.nick_name)&Q(is_done=0)).count()