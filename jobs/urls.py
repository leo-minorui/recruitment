#!/usr/bin/enve python
# -*- coding: utf-8 -*-
# author: Leo
# file: urls
# datetime: 2021/7/19 7:42 下午
# Email: leo.minorui@gmail.com
# ide: PyCharm

from django.conf.urls import url
from jobs import views

urlpatterns = [
    # 职位列表
    url(r"^joblist/", views.joblist, name="joblist"),

    url(r"^job/(?P<job_id>\d+)/$", views.detail, name="detail")
]