# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from apps.todolists.models import Todo, UsualTodo
from users.models import UserProfile
from django.http import HttpResponseRedirect
from .forms import TodoForm, TodoModalForm,UsualTodoModalForm
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import datetime
from django.db.models import Q


# Create your views here.

class TodolistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            all_todo = Todo.objects.all().order_by("is_done")
            all_usernames = UserProfile.objects.all()

            # 筛选是否完成
            is_done = request.GET.get('isd',"")
            if is_done:
                all_todo = all_todo.filter(is_done=is_done).order_by("priority")

            # 优先级筛选
            priority = request.GET.get('pr', "")
            if priority:
                all_todo = all_todo.filter(priority=priority)
            # 取出工作类型
            work_type = request.GET.get('wt', "")
            if work_type:
                all_todo = all_todo.filter(work_type=work_type)

            # 日期筛选:start_date
            start_date = request.GET.get('st', "")
            end_date = request.GET.get('et', "")
            if start_date:
                all_todo = all_todo.filter(plan_done_time__range=(start_date, end_date))

            # 名字筛选
            member_name = request.GET.get('gn', "")
            if member_name:
                all_todo = all_todo.filter(member_name__icontains=member_name)

            # 删除事项
            del_id = request.GET.get("delid")
            if del_id:
                Todo.objects.filter(id=del_id).delete()

            # 完成事项
            done_id = request.GET.get("doneid")
            if done_id:
                Todo.objects.filter(id=done_id).update(is_done=True, done_time=datetime.datetime.now())

            # 恢复事项
            redo_id = request.GET.get("redoid")
            if redo_id:
                Todo.objects.filter(id=redo_id).update(is_done=False, add_time=datetime.datetime.now())

            # TODOLIST进行分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            objects = ['john', 'edward', 'josh', 'frank']

            # Provide Paginator with the request object for complete querystring generation

            p = Paginator(all_todo, 20, request=request)

            todos = p.page(page)

            return render(request, "todolist.html", {
                "all_todo": todos,
                "all_usernames": all_usernames,
                "priority": priority,
                "work_type": work_type,
                "is_done": is_done,
                "start_date": start_date,
                "end_date": end_date,
                "member_name": member_name,

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
                todo.plan_done_time = request.POST.get("plandonetime")
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
                todo.add_time = datetime.datetime.now()
                todo.plan_done_time = request.POST.get("plandonetime_modal")
                todo.save()
                return HttpResponseRedirect('/todolist/')
        else:
            return render(request, "todolist.html", {
                "msg": "提交信息不能为空",
                "add_todo_form": add_todo_form,
                "all_todo": all_todo,
                "all_usernames": all_usernames,
            })


class UsualtodoView(View):
    def get(self, request):
        if request.user.is_authenticated:
            usual_todo = UsualTodo.objects.all().filter(user_name_id=request.user.id).order_by("-add_time")
            all_usernames = UserProfile.objects.all()

            # 筛选是否完成
            is_done = request.GET.get('isd', "")
            if is_done:
                usual_todo = usual_todo.filter(is_done=is_done).order_by("-done_time")

            # 优先级筛选
            priority = request.GET.get('pr', "")
            if priority:
                usual_todo = usual_todo.filter(priority=priority).order_by("add_time")
            # 取出工作类型
            work_type = request.GET.get('wt', "")
            if work_type:
                usual_todo = usual_todo.filter(work_type=work_type)

            # 日期筛选:start_date
            start_date = request.GET.get('st', "")
            end_date = request.GET.get('et', "")
            if start_date:
                usual_todo = usual_todo.filter(done_time__range=(start_date, end_date)).order_by("add_time")

            # 名字筛选
            member_name = request.GET.get('gn', "")
            if member_name:
                usual_todo = usual_todo.filter(member_name=member_name).order_by("add_time")

            # 删除事项
            del_id = request.GET.get("delid")
            if del_id:
                UsualTodo.objects.filter(id=del_id).delete()

            # 完成事项
            done_id = request.GET.get("doneid")
            if done_id:
                UsualTodo.objects.filter(id=done_id).update(is_done=True, done_time=datetime.datetime.now())

            # 恢复事项
            redo_id = request.GET.get("redoid")
            if redo_id:
                UsualTodo.objects.filter(id=redo_id).update(is_done=False, add_time=datetime.datetime.now())

            # TODOLIST进行分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1

            objects = ['john', 'edward', 'josh', 'frank']

            # Provide Paginator with the request object for complete querystring generation

            p = Paginator(usual_todo, 20, request=request)

            todos = p.page(page)

            return render(request, "usualtodolist.html", {
                "usual_todo": todos,
                "all_usernames": all_usernames,
                "priority": priority,
                "work_type": work_type,
                "is_done": is_done,
                "start_date": start_date,
                "end_date": end_date,
                "member_name": member_name,
            })

    def post(self, request):
        all_todo = UsualTodo.objects.all()
        all_usernames = UserProfile.objects.all()
        add_todo_form = TodoForm(request.POST)
        add_todomodal_form = TodoModalForm(request.POST)
        usual_todomodal_form = UsualTodoModalForm(request.POST)

        if add_todo_form.is_valid() or add_todomodal_form.is_valid() or usual_todomodal_form.is_valid():
            usual_todotext = request.POST.get("usual_todotext","")
            add_todo = request.POST.get("add_todo")

            if add_todo != None:
                todo = UsualTodo()
                todo.user_name_id = request.user.id
                todo.contents = request.POST.get("add_todo")
                todo.priority = request.POST.get("priority")
                todo.work_type = request.POST.get("work_type")
                todo.is_done = False
                todo.member_name = ','.join(request.POST.getlist("member_name"))
                todo.plan_done_time = request.POST.get("plandonetime")
                todo.save()
                return HttpResponseRedirect('/usualtodo/')
            elif usual_todotext !="":
                todo = UsualTodo()
                todo.id = request.POST.get("id")
                todo.user_name_id = request.user.id
                todo.contents = request.POST.get("usual_todotext", "")
                todo.priority = request.POST.get("usual_priority_modal")
                todo.work_type = request.POST.get("usual_work_type_modal")
                todo.is_done = False
                todo.member_name = ','.join(request.POST.getlist("usual_member_name_modal"))
                todo.add_time = datetime.datetime.now()
                todo.plan_done_time = request.POST.get("usual_plandonetime_modal")
                todo.save()
                return HttpResponseRedirect('/usualtodo/')
            else:
                todo = Todo()
                todo.user_name_id = request.user.id
                todo.contents = request.POST.get("todotext", "")
                todo.priority = request.POST.get("priority_modal")
                todo.work_type = request.POST.get("work_type_modal")
                todo.is_done = False
                todo.member_name = ','.join(request.POST.getlist("member_name_modal"))
                todo.add_time = datetime.datetime.now()
                todo.plan_done_time = request.POST.get("plandonetime_modal")
                todo.save()
                return HttpResponseRedirect('/usualtodo/')
        else:
            return render(request, "usualtodolist.html", {
                "msg": "提交信息不能为空",
                "add_todo_form": add_todo_form,
                "all_todo": all_todo,
                "all_usernames": all_usernames,
            })
