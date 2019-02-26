# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from apps.todolists.models import Todo
from users.models import UserProfile
from datetime import datetime
from django.http import HttpResponseRedirect
from .forms import TodoForm,TodoModalForm
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

class TodolistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            all_todo = Todo.objects.all()
            all_usernames = UserProfile.objects.all()

            #优先级筛选
            priority= request.GET.get('pr',"")
            if priority:
                all_todo =all_todo.filter(priority=priority)
            #取出工作类型
            work_type = request.GET.get('wt', "")
            if work_type:
                all_todo = all_todo.filter(work_type=work_type)

            #筛选是否完成
            is_done = request.GET.get('isd', "")
            if is_done:
                all_todo = all_todo.filter(is_done=is_done)

            #删除事项
            del_id = request.GET.get("delid")
            if del_id:
                Todo.objects.filter(id=del_id).delete()

            #完成事项
            done_id = request.GET.get("doneid")
            if done_id:
                Todo.objects.filter(id=done_id).update(is_done=True, done_time=datetime.now())

            #恢复事项
            redo_id = request.GET.get("redoid")
            if redo_id:
                Todo.objects.filter(id=redo_id).update(is_done=False, add_time=datetime.now())

            #对TODOLIST进行分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            objects = ['john', 'edward', 'josh', 'frank']

            # Provide Paginator with the request object for complete querystring generation

            p = Paginator(all_todo, 10,request=request)

            todos = p.page(page)


            return render(request, "todolist.html", {
                "all_todo": todos,
                "all_usernames": all_usernames,
                "priority": priority,
                "work_type": work_type,
                "is_done": is_done,

            })
        else:
            return render(request, "login.html", {})


    def post(self, request):
        all_todo = Todo.objects.all()
        all_usernames = UserProfile.objects.all()
        add_todo_form = TodoForm(request.POST)
        add_todomodal_form = TodoModalForm(request.POST)

        if add_todo_form.is_valid() or add_todomodal_form.is_valid():
            # add_todotext = request.POST.get("todotext","")
            add_todo = request.POST.get("add_todo")

            if add_todo != None:
                todo = Todo()
                todo.user_name_id = request.user.id
                todo.contents = request.POST.get("add_todo")
                todo.priority = request.POST.get("priority")
                todo.work_type = request.POST.get("work_type")
                todo.is_done = False
                todo.member_name = ','.join(request.POST.getlist("member_name"))
                todo.save()
                return HttpResponseRedirect('/todolist/')
            else:
                todo = Todo()
                todo.id = request.POST.get("id")
                todo.user_name_id = request.user.id
                todo.contents = request.POST.get("todotext", "")
                todo.priority = request.POST.get("priority_modal")
                todo.work_type = request.POST.get("work_type_modal")
                todo.is_done = False
                todo.member_name = ','.join(request.POST.getlist("member_name_modal"))
                todo.save()
                return HttpResponseRedirect('/todolist/')
        else:
            return render(request, "todolist.html", {
                "msg": "提交信息不能为空",
                "add_todo_form": add_todo_form,
                "all_todo": all_todo,
                "all_usernames": all_usernames,
            })
