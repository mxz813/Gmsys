# -*- coding:utf-8 -*-
from django.db import models
from datetime import datetime
from users.models import UserProfile
from DjangoUeditor.models import UEditorField


# Create your models here.
class Information(models.Model):
    title = models.CharField(max_length=100, verbose_name="信息标题", default="")
    contents = UEditorField(verbose_name='信息内容', width=600, height=300, toolbars="full",
                            imagePath="information/ueditor/%(basename)s_%(datetime)s.%(extname)s", filePath="information/ueditor/%(basename)s_%(datetime)s.%(extname)s",default='')
    author = models.ForeignKey(UserProfile, verbose_name="作者", on_delete=models.CASCADE, blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "信息中心"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Links(models.Model):
    title = models.CharField(max_length=100, verbose_name="链接标题", default="")
    url = models.URLField(default="", verbose_name="链接地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "网站链接"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Atsintroduce(models.Model):
    title = models.CharField(max_length=100, verbose_name="简介标题", default="")
    contents = UEditorField(verbose_name='简介内容', width=600, height=300, toolbars="full",
                            imagePath="atsintroduce/ueditor/%(basename)s_%(datetime)s.%(extname)s",
                            filePath="atsintroduce/ueditor/%(basename)s_%(datetime)s.%(extname)s", default='',blank=True,null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "班组简介"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Notice(models.Model):
    contents = UEditorField(verbose_name='公告内容', width=600, height=300, toolbars="full",
                            imagePath="notice/ueditor/%(basename)s_%(datetime)s.%(extname)s",
                            filePath="notice/ueditor/%(basename)s_%(datetime)s.%(extname)s", default='',blank=True,null=True)
    sld = UEditorField(verbose_name='安全文件学习', width=600, height=300, toolbars="full",
                       imagePath="notice/ueditor/%(basename)s_%(datetime)s.%(extname)s",
                       filePath="notice/ueditor/%(basename)s_%(datetime)s.%(extname)s", default='', blank=True,
                       null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "公告内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format('公告、安全文件学习')


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name="标题",blank=True,null=True)
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100,blank=True,null=True)
    url = models.URLField(max_length=200, verbose_name="访问地址", default='',blank=True,null=True)
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name