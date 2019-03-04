#-*- coding:utf-8 -*-
from django.db import models
from users.models import UserProfile

# Create your models here.
class CourseType(models.Model):
    course_name = models.CharField(verbose_name="系统名称",default="",max_length=10)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="系统名称"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course_name

class QuestionBank(models.Model):
    question_title = models.TextField(verbose_name="题目",default="")
    answer = models.TextField(verbose_name="答案",default="")
    course_type = models.ForeignKey(CourseType,on_delete=models.CASCADE,verbose_name="系统名")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="题库"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.question_title

class MemberQuestionRecord(models.Model):
    record_question_title = models.ForeignKey(QuestionBank,on_delete=models.CASCADE,verbose_name="题目",default="")
    record_answer = models.TextField(verbose_name="答案",default="")
    course_type = models.ForeignKey(CourseType,on_delete=models.CASCADE,verbose_name="系统名")
    user_name = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name="答题人")
    add_time = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")

    class Meta:
        verbose_name ="成员答题记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.record_answer