# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from apps.todolists.models import Todo
from users.models import UserProfile
from datetime import datetime
from django.http import HttpResponseRedirect



# Create your views here.

class TodolistView(View):
    def get(self, request):
        if request.user.is_authenticated:
            all_todo = Todo.objects.all()
            all_usernames = UserProfile.objects.all()
            return render(request, "todolist.html", {
                "all_todo": all_todo,
                "all_usernames": all_usernames,
        })
        else:
            return render(request, "login.html",{})

    def post(self, request):
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
            todo.contents = request.POST.get("todotext","")
            todo.priority = request.POST.get("priority_modal")
            todo.work_type = request.POST.get("work_type_modal")
            todo.is_done = False
            todo.member_name = ','.join(request.POST.getlist("member_name_modal"))
            todo.save()
            return HttpResponseRedirect('/todolist/')

class DeltodoView(View):
    def get(self,request):
       trans_id = request.GET.get("id")
       Todo.objects.filter(id = trans_id).delete()
       return HttpResponseRedirect('/todolist/')


class DonetodoView(View):
    def get(self,request):
        trans_id = request.GET.get("id")
        querytodo = Todo.objects.filter(id = trans_id).update(is_done = True,done_time = datetime.now())
        return HttpResponseRedirect('/todolist/')


class RetodoView(View):
    def get(self,request):
        trans_id = request.GET.get("id")
        querytodo = Todo.objects.filter(id = trans_id).update(is_done = False,add_time = datetime.now())
        return HttpResponseRedirect('/todolist/')



