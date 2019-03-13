# _*_ encoding:utf-8 _*_
from django.db import models
from plans.models import PlanYear
from datetime import datetime
from DjangoUeditor.models import UEditorField

# Create your models here.
class Scheduling(models.Model):
    sch_title = models.CharField(default='',max_length=100,verbose_name='排班标题')
    contents = UEditorField(verbose_name='排班内容', width=600, height=300, toolbars="full",
                            imagePath="information/ueditor/%(basename)s_%(datetime)s.%(extname)s",
                            filePath="information/ueditor/%(basename)s_%(datetime)s.%(extname)s", default='',blank=True,null=True)
    scheduling_year =models.ForeignKey(PlanYear,on_delete=models.CASCADE,verbose_name="排班年份",default=1)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "排班计划"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.sch_title