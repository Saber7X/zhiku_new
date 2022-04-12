import hashlib
import os

from django.contrib import auth
from django.contrib.sites import requests
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, HttpRequest, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime
from docxtpl import DocxTemplate
from base import models, forms
from base.forms import LoginForm, RegisterModelForm, personForm, diaochaModel
from base.models import UserInfo


def index(request):
    return render(request, 'index.html')


# 登录

def hash_code(s, salt='site'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def sign(request):
    """ 用户名和密码登录 """
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'sign.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            username = models.UserInfo.objects.get(username=username)
        except:
            message = '用户不存在！'
            return render(request, 'sign.html', locals())

        if username.password == password:
            request.session["info"] = username.username
            request.session['is_login'] = True
            request.session['user_id'] = username.id

            # return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
            return redirect('/')
            # return render(request, 'index1.html', locals())
        else:
            message = '密码不正确！'
            return render(request, 'index.html', locals())

    login_form = forms.LoginForm()
    return render(request, 'sign.html', locals())


from base.utils.bootstrap import BootStrapModelForm
from base.utils.bootstrap import BootStrapForm


class PersonModel(BootStrapModelForm):
    class Meta:
        model = models.Person1
        exclude = ('user',)


def register(request):
    if request.method == 'GET':
        form = RegisterModelForm()
        return render(request, 'register.html', {'form': form})

    form = RegisterModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        n = form.cleaned_data['username']
        models.Person1.objects.create(user=n)
        return JsonResponse({'status': True, 'data': '/sign/'})

    return JsonResponse({'status': False, 'error': form.errors})


# 注销
def logout(request):
    request.session.clear()
    return redirect('/')


# return render(request, 'index1.html')
def person_check(request):
    form = personForm(data=request.POST)
    birth = form.cleaned_data['birth']
    school = form.cleaned_data['school']
    company = form.cleaned_data['company']
    profession = form.cleaned_data['profession']
    address = form.cleaned_data['address']
    return render(request, "person.html")


def index1(request):
    username = request.session.get('username', None)
    return render(request, "index1.html", {'userinfo': username})


def person(request, name):
    if request.method == 'GET':
        # print(name)
        form = models.Person1.objects.filter(user=name).first()
        return render(request, 'person.html', {'form': form})


def person_edit(request, name):
    ins = models.Person1.objects.filter(user=name).first()
    if request.method == 'GET':
        form = PersonModel(instance=ins)
        return render(request, 'person_edit.html', {'form': form})
    form = PersonModel(data=request.POST, instance=ins)  # 获取post传来的数据
    if form.is_valid():
        form.save()  # 所以保存时就是修改哪一行的数据，而不是新增了
        return redirect('/person/' + request.session['info'])

    return render(request, 'person_edit.html', {'form': form})

def person_luntan(request, name):
    form = models.LunTan.objects.filter(user=name)
    print(name)
    print(form)
    return render(request, 'person_luntan.html', {'form': form, 'name': name})

def chat(request):
    return render(request, 'message/chat.html')


def room(request, room_name):
    return render(request, 'message/room.html', {
        'room_name': room_name
    })


def submit(request):
    if request.method == 'GET':
        form_diaocha = diaochaModel()
        return render(request, 'biaodan/submit.html', {"form_diaocha": form_diaocha})

    form_diaocha = diaochaModel(data=request.POST)
    if form_diaocha.is_valid():
        # print(form_diaocha)
        form_diaocha.save()
        filename = 'test.docx'  # 所生成的word文档需要以.docx结尾，文档格式需要
        filepath = 'C:\\Users\\DELL\\Djangosizhi'
        template_path = os.getcwd() + '\\guihua.docx'
        template = DocxTemplate(template_path)
        shouye = {
            'school': form_diaocha.cleaned_data['school'],
            'username': form_diaocha.cleaned_data['user'],
            'college': form_diaocha.cleaned_data['college'],
            'teacher': form_diaocha.cleaned_data['teacher'],
            'edu_number': form_diaocha.cleaned_data['edu_number'],
            'class_room': form_diaocha.cleaned_data['class_room'],
            'part_1_1': form_diaocha.cleaned_data['part_1_1'],
            'part_1_2': form_diaocha.cleaned_data['part_1_2'],
            'part_1_3': form_diaocha.cleaned_data['part_1_3'],

            'part_2_1': form_diaocha.cleaned_data['part_2_1'],
            'part_2_2': form_diaocha.cleaned_data['part_2_2'],
            'part_2_3': form_diaocha.cleaned_data['part_2_3'],

            'part_3_1': form_diaocha.cleaned_data['part_3_1'],
            'part_3_2': form_diaocha.cleaned_data['part_3_2'],
            'part_3_3': form_diaocha.cleaned_data['part_3_3'],

            'part_4_1': form_diaocha.cleaned_data['part_4_1'],
            'part_4_2': form_diaocha.cleaned_data['part_4_2'],
            'part_4_3': form_diaocha.cleaned_data['part_4_3'],
            'part_4_4': form_diaocha.cleaned_data['part_4_4'],

            'part_5_1': form_diaocha.cleaned_data['part_5_1'],
            'part_5_2': form_diaocha.cleaned_data['part_5_2'],
            'part_5_3': form_diaocha.cleaned_data['part_5_3'],
            'part_5_4': form_diaocha.cleaned_data['part_5_4'],
            'part_5_5': form_diaocha.cleaned_data['part_5_5'],
            'part_5_6': form_diaocha.cleaned_data['part_5_6'],
            'part_5_7': form_diaocha.cleaned_data['part_5_7'],

            'part_6_1': form_diaocha.cleaned_data['part_6_1'],
            'part_6_2': form_diaocha.cleaned_data['part_6_2'],
            'part_6_3': form_diaocha.cleaned_data['part_6_3'],
            'part_6_4': form_diaocha.cleaned_data['part_6_4'],
            'part_6_5': form_diaocha.cleaned_data['part_6_5'],

            'part_7_1': form_diaocha.cleaned_data['part_7_1'],
            'part_7_2': form_diaocha.cleaned_data['part_7_2'],
            'part_7_3': form_diaocha.cleaned_data['part_7_3'],
            'part_7_4': form_diaocha.cleaned_data['part_7_4'],
            'part_7_5': form_diaocha.cleaned_data['part_7_5'],

            'part_8_1': form_diaocha.cleaned_data['part_8_1'],
            'part_8_2': form_diaocha.cleaned_data['part_8_2'],
            'part_8_3': form_diaocha.cleaned_data['part_8_3'],
            'part_8_4': form_diaocha.cleaned_data['part_8_4'],
            'part_8_5': form_diaocha.cleaned_data['part_8_5'],

            'part_9_1': form_diaocha.cleaned_data['part_9_1'],
            'part_9_2': form_diaocha.cleaned_data['part_9_2'],

            'part_10_1': form_diaocha.cleaned_data['part_10_1'],
            'part_10_2': form_diaocha.cleaned_data['part_10_2'],
            'part_10_3': form_diaocha.cleaned_data['part_10_3'],
            'part_10_4': form_diaocha.cleaned_data['part_10_4'],
            'part_10_5': form_diaocha.cleaned_data['part_10_5'],

            'part_11_1': form_diaocha.cleaned_data['part_11_1'],
            'part_11_2': form_diaocha.cleaned_data['part_11_2'],
            'part_11_3': form_diaocha.cleaned_data['part_11_3'],
            'part_11_4': form_diaocha.cleaned_data['part_11_4'],
            'part_11_5': form_diaocha.cleaned_data['part_11_5'],

            'part_12_1': form_diaocha.cleaned_data['part_12_1'],
            'part_12_2': form_diaocha.cleaned_data['part_12_2'],
            'part_12_3': form_diaocha.cleaned_data['part_12_3'],
            'part_12_4': form_diaocha.cleaned_data['part_12_4'],
            'part_12_5': form_diaocha.cleaned_data['part_12_5'],

            'part_13_1': form_diaocha.cleaned_data['part_13_1'],
            'part_13_2': form_diaocha.cleaned_data['part_13_2'],
            'part_13_3': form_diaocha.cleaned_data['part_13_3'],
            'part_13_4': form_diaocha.cleaned_data['part_13_4'],
            'part_13_5': form_diaocha.cleaned_data['part_13_5'],

            'part_14_1': form_diaocha.cleaned_data['part_14_1'],
            'part_14_2': form_diaocha.cleaned_data['part_14_2'],
            'part_14_3': form_diaocha.cleaned_data['part_14_3'],
            'part_14_4': form_diaocha.cleaned_data['part_14_4'],
            'part_14_5': form_diaocha.cleaned_data['part_14_5'],

            'part_15_1': form_diaocha.cleaned_data['part_15_1'],
            'part_15_2': form_diaocha.cleaned_data['part_15_2'],
            'part_15_3': form_diaocha.cleaned_data['part_15_3'],
            'part_15_4': form_diaocha.cleaned_data['part_15_4'],

            'part_16_1': form_diaocha.cleaned_data['part_16_1'],
            'part_16_2': form_diaocha.cleaned_data['part_16_2'],
            'part_16_3': form_diaocha.cleaned_data['part_16_3'],
            'part_16_4': form_diaocha.cleaned_data['part_16_4'],
        }
        template.render(shouye)
        template.save(os.path.join(filepath, filename))
        response = StreamingHttpResponse(read_file(os.path.join(filepath, filename), 512))
        response['Content-Type'] = 'application/msword'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
        # time.sleep(10)
        return response
    return render(request, 'biaodan/form.html')


def yuan(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'biaodan/submit.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'form': form(),
        }
    )


# 流方式读取文件
def read_file(file_name, size):
    with open(file_name, mode='rb') as fp:
        while True:
            c = fp.read(size)
            if c:
                yield c
            else:
                break


def form(request):
    filename = 'test.docx'  # 所生成的word文档需要以.docx结尾，文档格式需要
    filepath = 'C:\\Users\\DELL\\Djangosizhi'
    template_path = os.getcwd() + '\\guihua.docx'
    template = DocxTemplate(template_path)
    form = diaochaModel(request.POST)
    shouye = {
        'school': form.cleaned_data['school']
    }
    template.render(shouye)
    template.save(os.path.join(filepath, filename))
    response = StreamingHttpResponse(read_file(os.path.join(filepath, filename), 512))
    response['Content-Type'] = 'application/msword'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    # time.sleep(10)
    return response
