# -*- coding: utf-8 -*-
#
# authors: Vipin
#
# Created on Tue June 4 2019

# -- Internal Libraries
from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
	path('create', views.CommentCreate.as_view(), name='comment_create'),
    path('<int:pk>', views.CommentDetail.as_view(), name='comment_detail')
]
