# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import MemberList

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # List all users
    path('users/', views.users, name='users'),

    path('member_list/', views.MemberList.as_view(), name='member_list'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
