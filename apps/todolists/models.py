# -*- coding:utf-8 -*-
from django.db import models
from users.models import UserProfile
import datetime

# Create your models here.
class Todo(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"发布者")
    member_name = models.CharField(max_length=50, verbose_name=u"成员姓名", default="")
    work_type = models.CharField(max_length=50, verbose_name=u"工作类型",
                           choices=(("1", u"安全管理"), ("2", u"生产管理"), ("3", u"质量管理"), ("4", u"综合管理"), ("5", u"物资管理"),("6", u"宣传工作"), ("0", u"日常工作")),
                           default="0")
    contents = models.TextField(verbose_name=u"待做事项")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    done_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"完成时间")
    plan_done_time = models.DateTimeField(default=datetime.datetime.now,verbose_name=u"计划完成时间")
    priority = models.IntegerField(choices=((1, "重要"), (2, "一般"), (3, "日常")), default=3, verbose_name=u"优先级")
    is_done = models.BooleanField(default=False,verbose_name=u"完成状态")

    class Meta:
        verbose_name = "待完成事项"
        verbose_name_plural = verbose_name
        ordering = ['priority','add_time']

    def __str__(self):
        return self.contents


class UsualTodo(models.Model):
    user_name = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"发布者")
    member_name = models.CharField(max_length=50, verbose_name=u"成员姓名", default="")
    work_type = models.CharField(max_length=50, verbose_name=u"工作类型",
                           choices=(("1", u"安全管理"), ("2", u"生产管理"), ("3", u"质量管理"), ("4", u"综合管理"), ("5", u"物资管理"),("6", u"宣传工作"), ("0", u"日常工作")),
                           default="0")
    contents = models.TextField(verbose_name=u"待做事项")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u"添加时间")
    done_time = models.DateTimeField(default=datetime.datetime.now, verbose_name=u"完成时间")
    plan_done_time = models.DateTimeField(default=datetime.datetime.now,verbose_name=u"计划完成时间")
    priority = models.IntegerField(choices=((1, "重要"), (2, "一般"), (3, "日常")), default=3, verbose_name=u"优先级")
    is_done = models.BooleanField(default=False,verbose_name=u"完成状态")

    class Meta:
        verbose_name = "日常计划"
        verbose_name_plural = verbose_name
        ordering = ['priority','add_time']

    def __str__(self):
        return self.contents