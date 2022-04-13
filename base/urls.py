#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include

from base import views
from base.library import viewes
from base.gongsi import vieww
from base.luntan import view
from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from base.wenjuan import wenjuanview

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),  # 固定写法
    path('', views.index1, name='index1'),
    path('sign/', views.sign, name='sign'),
    path('register/', views.register, name='register'),
    path('index1/', views.index1, name='index1'),
    path('logout/', views.logout, name='logout'),
    path('person/<str:name>/', views.person, name='person'),
    path('person/edit/<str:name>/', views.person_edit, name='person'),
    path('person/luntan/<str:name>/', views.person_luntan, name='person'),
    path('person/person_check/', views.person_check, name='person_check'),
    path('luntan_add/', view.luntan_add),
    path('luntan_list/', view.luntan_list),
    path('luntan_list/tiezi/', view.luntan_list_tiezi),
    path('luntan_list/kecheng/', view.luntan_list_kecheng),
    path('luntan_read/<int:nid>/', view.luntan_read),
    path('luntan_delete/<int:nid>/', view.luntan_delete),
    path('luntan_list/admin/', view.luntan_admin),
    path('chat/', views.chat, name='chat'),
    path('chat/<str:room_name>/', views.room, name='room'),
    path('form/', views.form, name='form'),
    path('yuan/', views.yuan, name='yuan'),
    path('submit/', views.submit, name='submit'),
    # 测试
    path('add_book/', viewes.add_book),
    path('show_books/', viewes.show_books),

    path('wenjuan/disc/', wenjuanview.Disc),
    path('wenjuan/mbti/', wenjuanview.Mbti),
    path('about/', wenjuanview.about),

    path('gongsi_add/', vieww.gongsi_add),
    path('gongsi_list/', vieww.gongsi_list),
    path('gongsi_list/jianjie/', vieww.gongsi_list_jianjie),
    path('gongsi_read/<int:nid>/', vieww.gongsi_read),
    path('gongsi_delete/<int:nid>/', vieww.gongsi_delete),
    path('gongsi_list/admin/', vieww.gongsi_admin),
]
