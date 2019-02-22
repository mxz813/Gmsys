#-*- coding:utf-8 -*-
from django.db import models

# Create your models here.
class PlanTitle(models.Model):
    plan_title = models.TextField(verbose_name="计划标题")

    class Meta:
        verbose_name ="计划标题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.plan_title