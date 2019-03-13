# -*-coding:utf-8 -*-
from xadmin import views
import xadmin
from .models import CourseType,QuestionBank,MemberQuestionRecord

class CourseTypeAdmin(object):
    list_display = ('course_name', 'add_time',)
    list_filter = ['course_name', 'add_time']
    search_fields = ['course_name']
    model_icon = 'fa fa-question'


class QuestionBankAdmin(object):
    list_display = ('question_title', 'add_time','answer','course_type')
    list_filter = ['question_title', 'add_time','answer','course_type']
    search_fields = ['question_title','answer','course_type']
    model_icon = 'fa fa-question'

class MemberQuestionRecordAdmin(object):
    list_display = ('record_question_title','record_answer','course_type','user_name', 'add_time',)
    list_filter = ['record_question_title','record_answer','course_type','user_name','add_time']
    search_fields = ['record_question_title','record_answer','course_type','user_name']
    model_icon = 'fa fa-question'



xadmin.site.register(CourseType, CourseTypeAdmin)
xadmin.site.register(QuestionBank, QuestionBankAdmin)
xadmin.site.register(MemberQuestionRecord, MemberQuestionRecordAdmin)