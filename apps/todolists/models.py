# -*- coding:utf-8 -*-
from django.db import models
from users.models import UserProfile

# Create your models here.
class Todo(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"发布者")
    contents = models.TextField(verbose_name=u"待做事项")
    add_time = models.DateTimeField(auto_now=True, verbose_name=u"添加时间")
    done_time = models.DateTimeField(auto_now=True, verbose_name=u"完成时间")
    priority = models.IntegerField(choices=((1, "重要"), (2, "一般"), (3, "日常")), default=3, verbose_name=u"优先级")
    is_done = models.BooleanField(default=False,verbose_name=u"完成状态")

    class Meta:
        verbose_name = "待完成事项"
        verbose_name_plural = verbose_name
        ordering = ['priority','add_time']

    def __str__(self):
        return self.contents