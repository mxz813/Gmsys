from django.shortcuts import render
from django.views.generic.base import View
from .models import CourseType,QuestionBank,MemberQuestionRecord
from django.http import HttpResponseRedirect
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from users.utils import LoginRequiredMixin
# Create your views here.

class QuestionsView(LoginRequiredMixin,View):
    def get(self,request):
        all_question = QuestionBank.objects.all().order_by('?')[:1]

        return render(request,'question.html',{
        "all_question":all_question
        })

    def post(self,request):

        record = MemberQuestionRecord()
        record.user_name_id = request.user.id
        record.record_answer = request.POST.get('answer_question')
        record.course_type_id = request.POST.get('course_type_id')
        record.record_question_title_id = request.POST.get('record_question_title_id')
        record.save()
        return HttpResponseRedirect('/que/bank/?qn='+record.record_question_title_id)

class QuestionBankView(LoginRequiredMixin,View):
    def get(self,request):
        all_question = QuestionBank.objects.all()

        #题号搜索
        question_id =request.GET.get('qn',"")
        if question_id:
            all_question = all_question.filter(id= question_id)

        # question进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = ['john', 'edward', 'josh', 'frank']

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_question, 50, request=request)

        questions = p.page(page)

        return render(request,'questionbank.html',{
        "all_question":questions,
        "question_id":question_id
        })