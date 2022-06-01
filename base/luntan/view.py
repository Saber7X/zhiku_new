import os

from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from base.utils.bootstrap import BootStrapForm
from base.utils.bootstrap import BootStrap
from base.utils.bootstrap import BootStrapModelForm
from base.utils.bootstrap import BootStrapForm
from base.models import LunTan
from base import models
from base.utils.pagination import Pagination
from django import forms


class LunTanModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.LunTan
        exclude = ('Count','user',)


def luntan_list(request):
    data_dict = {}
    search_data = request.POST.get('data', "")
    if search_data:
        data_dict["title__contains"] = search_data
        models.History.objects.create(content=search_data)
    queryset = models.LunTan.objects.filter(**data_dict).order_by('-Count')
    hot = models.LunTan.objects.all()[0:5]

    page_object = Pagination(request, queryset)
    his = models.History.objects.all()
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data": search_data,
        "tip": "推荐总榜",
        "his": his,
        "hot": hot
    }
    return render(request, 'LunTan/home.html', context)


def luntan_list_tiezi(request):
    data_dict = {}
    search_data = request.POST.get('data', "")
    if search_data:
        data_dict["content__contains"] = search_data
    queryset = models.LunTan.objects.filter(**data_dict, leixing=1).order_by('-Count')
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data": search_data,
        "tip": "好文推荐"
    }
    return render(request, 'LunTan/home.html', context)


def luntan_list_kecheng(request):
    data_dict = {}
    search_data = request.POST.get('data', "")
    his = models.History.objects.all()
    if search_data:
        data_dict["content__contains"] = search_data
        models.History.objects.creat(content=search_data)
    queryset = models.LunTan.objects.filter(**data_dict, leixing=2).order_by('-Count')
    page_object = Pagination(request, queryset)
    hot = queryset[0:5]
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data": search_data,
        "tip": "课程推荐",
        "luntan": "active",
        "his": his,
        "hot": hot
    }
    
    return render(request, 'LunTan/home.html', context)


def luntan_add(request):
    if request.method == "GET":
        form = LunTanModelForm()
        return render(request, 'LunTan/luntan_add.html', {"form": form})
    form = LunTanModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()  # 定义的是那个类就自动存储到哪个类里面
        # models.LunTan.objects.filter(**form.cleaned_data).first().user = request.session["info"]
        # print(form.cleaned_data)
        form.cleaned_data.pop('img')
        print(request.session["info"])
        models.LunTan.objects.filter(**form.cleaned_data).update(user=request.session["info"])
        # print(models.LunTan.objects.filter(**form.cleaned_data).first())
        return redirect('/luntan_list/')
    return render(request, 'LunTan/luntan_add.html', {"form": form})


def luntan_read(request, nid):
    # models.LunTan.objects.create()
    CC = models.LunTan.objects.filter(id=nid).first()
    a = CC.Count
    a += 1
    models.LunTan.objects.filter(id=nid).update(Count=a)

    data = models.LunTan.objects.filter(id=nid).first()
    if data.shuxing == 1:
        lianjie = data.content
        return redirect(lianjie)
    else:
        hot = models.LunTan.objects.all()[0:5]
        return render(request, 'LunTan/luntan_read.html', {"data": data, "hot":hot})

def luntan_admin(request):
    # # models.LunTan.objects.create()
    # if request.method == 'GET':
    #     return render(request, 'LunTan/pwd.html')
    # pwd = request.POST.get("password")
    # if pwd == "123456":
    data = models.LunTan.objects.all()
    return render(request, 'LunTan/luntan_admin.html', {"data": data})

def luntan_delete(request, nid):
    # id = request.GET.get(nid)
    if request.method == 'GET':
        return render(request, 'LunTan/pwd.html')
    pwd = request.POST.get("password")
    if pwd == "123456":
        models.LunTan.objects.filter(id = nid).delete()
        data = models.LunTan.objects.all()
        return render(request, 'LunTan/luntan_admin.html', {"data": data})
    # return HttpResponse("删除成功")