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


class gongsiModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.gongsi
        exclude = ('Count', 'user')


def gongsi_list(request):
    data_dict = {}
    search_data = request.POST.get('data', "")
    if search_data:
        data_dict["content__contains"] = search_data
        models.History.objects.create(content=search_data)
    queryset = models.gongsi.objects.filter(**data_dict).order_by('-Count')
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data": search_data,
    }
    return render(request, 'gongsi/gongsi.html', context)


def gongsi_list_jianjie(request):
    data_dict = {}
    search_data = request.POST.get('data', "")
    if search_data:
        data_dict["content__contains"] = search_data
    queryset = models.gongsi.objects.filter(**data_dict, leixing=1).order_by('-Count')
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data": search_data,
    }
    return render(request, 'gongsi/gongsi.html', context)


def gongsi_add(request):
    if request.method == "GET":
        form = gongsiModelForm()
        return render(request, 'gongsi/gongsi_add.html', {"form": form})
    form = gongsiModelForm(data=request.POST, files=request.FILES)
    print(form)
    if form.is_valid():
        print(1)
        form.save()  # 定义的是那个类就自动存储到哪个类里面
        return redirect('/gongsi_list/')
    return render(request, 'gongsi/gongsi_add.html', {"form": form})


def gongsi_read(request, nid):
    # models.LunTan.objects.create()
    CC = models.gongsi.objects.filter(id=nid).first()
    a = CC.Count
    a += 1
    models.gongsi.objects.filter(id=nid).update(Count=a)

    data = models.gongsi.objects.filter(id=nid).first()
    lianjie = data.content
    return redirect(lianjie)
    # return render(request, 'LunTan/luntan_read.html', {"data": data})

def gongsi_admin(request):
    # # models.LunTan.objects.create()
    # if request.method == 'GET':
    #     return render(request, 'LunTan/pwd.html')
    # pwd = request.POST.get("password")
    # if pwd == "123456":
    data = models.gongsi.objects.all()
    return render(request, 'gongsi/gongsi_admin.html', {"data": data})


def gongsi_delete(request, nid):
    # id = request.GET.get(nid)
    if request.method == 'GET':
        return render(request, 'gongsi/pwd.html')
    pwd = request.POST.get("password")
    if pwd == "123456":
        models.gongsi.objects.filter(id=nid).delete()
        data = models.gongsi.objects.all()
        return render(request, 'gongsi/gongsi_admin.html', {"data": data})
    # return HttpResponse("删除成功")