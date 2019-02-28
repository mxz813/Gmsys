#-*- coding:utf-8 -*-
from django.db import models
from users.models import UserProfile

# Create your models here.
class PlanTitle(models.Model):
    plan_title = models.CharField(max_length=100,default='',verbose_name="计划总标题")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="计划总标题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.plan_title

class PlanYear(models.Model):
    plan_year = models.IntegerField(default=2019,verbose_name="时间")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="计划时间"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}'.format(self.plan_year)


class PlanArticle(models.Model):
    article_title = models.CharField(max_length=100,default='',verbose_name="计划标题")
    article_year = models.ForeignKey(PlanYear,on_delete=models.CASCADE,verbose_name="时间")
    article_cont = models.TextField(verbose_name="计划内容")
    article_auth = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="发布人")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="计划内容"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_title

class Maintain(models.Model):
    process_title = models.CharField(max_length=100,default='',verbose_name="检修流程标题")
    process_cont = models.TextField(default='',verbose_name="检修流程内容")
    add_time = models.DateTimeField(auto_now=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="检修流程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.process_title