# -*-coding:utf-8 -*-
from django.urls import path,include
from .views import QuestionsView,QuestionBankView
app_name = 'que'
urlpatterns = [
    path('dayly/', QuestionsView.as_view(), name="question"),
    path('bank/', QuestionBankView.as_view(), name="questionbank"),
]