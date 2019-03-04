# -*-coding:utf-8 -*-
from django import forms



class TodoForm(forms.Form):
    add_todo = forms.CharField(widget=forms.Textarea,required=True)
    work_type = forms.CharField(required=True)
    priority = forms.CharField(required=True)
    member_name = forms.CharField(required=True)

class TodoModalForm(forms.Form):
    todotext = forms.CharField(widget=forms.Textarea,required=True)
    work_type_modal = forms.CharField(required=True)
    priority_modal = forms.CharField(required=True)
    member_name_modal = forms.CharField(required=True)

class UsualTodoModalForm(forms.Form):
    usual_todotext = forms.CharField(widget=forms.Textarea,required=True)
    usual_work_type_modal = forms.CharField(required=True)
    usual_priority_modal = forms.CharField(required=True)
    usual_member_name_modal = forms.CharField(required=True)



