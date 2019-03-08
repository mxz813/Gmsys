# _*_ encoding:utf-8 _*_
from django.db import models
from plans.models import PlanYear
from datetime import datetime

# Create your models here.
class Scheduling(models.Model):
    sch_title = models.CharField(default='',max_length=100,verbose_name='排班标题')
    image = models.ImageField(default='',upload_to="scheduling/%Y/%m", verbose_name="排班表", max_length=100)
    scheduling_year =models.ForeignKey(PlanYear,on_delete=models.CASCADE,verbose_name="排班年份",default=1)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "排班计划"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sch_title