#!/usr/bin/enve python
# -*- coding: utf-8 -*-
# author: Leo
# file: urls
# datetime: 2021/7/19 7:42 下午
# Email: leo.minorui@gmail.com
# ide: PyCharm

from django.conf.urls import url
from jobs import views
from django.urls import path

urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name="joblist"),

    # 职位详情
    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail"),

    # 首页自动跳转到 职位列表
    url(r"^$", views.joblist, name="name"),

    # 提交简历
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),

    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail')



]