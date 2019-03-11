# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from users.models import UserProfile

# Create your models here.
class Information(models.Model):
    title = models.CharField(max_length=100, verbose_name="信息标题", default="")
    contents = models.TextField(verbose_name="信息内容")
    author = models.ForeignKey(UserProfile,verbose_name="作者", on_delete=models.CASCADE,blank=True,null=True)
    image = models.ImageField(default='', upload_to="information/%Y/%m", verbose_name="内容附图", max_length=100,blank=True,null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "信息中心"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title


class Links(models.Model):
    title = models.CharField(max_length=100, verbose_name="链接标题", default="")
    url = models.URLField(default="",verbose_name="链接地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "网站链接"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title


class Atsintroduce(models.Model):
    title = models.CharField(max_length=100, verbose_name="简介标题", default="")
    contents = models.TextField(verbose_name="简介内容")
    image = models.ImageField(default='', upload_to="atsintroduce/%Y/%m", verbose_name="班组照片", max_length=100,blank=True,null=True)
    logo = models.ImageField(default='', upload_to="logo/%Y/%m", verbose_name="班组LOGO", max_length=100,blank=True,null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


    class Meta:
        verbose_name = "班组简介"
        verbose_name_plural = verbose_name


    def __str__(self):
        return self.title

