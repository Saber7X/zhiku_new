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


class DiscModel(BootStrapModelForm):
    class Meta:
        model = models.Disc
        exclude = ('user',)

def Disc(request):
    if request.method == 'GET':
        form = DiscModel()
        return render(request, 'wenjuan/wenjuan.html', {"form": form, "title":"Disc问卷", "content": "看看自己是属于哪一种人格特质。在每一个大标题中的四个选择题中只选择一个最符合你自己的。"})
    form = DiscModel(data= request.POST)
    if form.is_valid():
        form.save()
        row_object = form.cleaned_data
        a = 0
        b = 0
        c = 0
        d = 0
        for i in row_object:
            if row_object[i] == 1:
                a += 1
            if row_object[i] == 2:
                b += 1
            if row_object[i] == 3:
                c += 1
            if row_object[i] == 4:
                d += 1
        if a >10:
            return render(request, 'wenjuan/DISCans.html', {"a":"高D型特质的人可以称为是“天生的领袖”。", "b":"在情感方面，D型人一个坚定果敢的人，酷好变化，喜欢控制，干劲十足，独立自主，超级自信。可是，由于比较不会顾及别人的感受，所以显得粗鲁、霸道、没有耐心、穷追不舍、不会放松。D型人不习惯与别人进行感情上的交流，不会恭维人，不喜欢眼泪，匮乏同情心。 ", "c": "在工作方面，D型人是一个务实和讲究效率的人，目标明确，眼光全面，组织力强，行动迅速，解决问题不过夜，果敢坚持到底，在反对声中成长。但是，因为过于强调结果， D型人往往容易忽视细节，处理问题不够细致。爱管人、喜欢支使他人的特点使得D型人能够带动团队进步，但也容易激起同事的反感。", "d": "在人际关系方面， D型人喜欢为别人做主，虽然这样能够帮助别人做出选择，但也容易让人有强迫感。由于关注自己的目标， D型人在乎的是别人的可利用价值。喜欢控制别人，不会说对不起。", "e": "积级进取、争强好胜、强势、爱追根究底、直截了当、主动的开拓者、坚持意见、自信、直率"})
        if b >10:
            return render(request, 'wenjuan/DISCans.html', {"a":"高I型的人通常是较为活泼的团队活动组织者", "b":"I型人是一个情感丰富而外露的人，由于性格活跃，爱说，爱讲故事，幽默，彩色记忆，能抓住听众，你常常是聚会的中心人物。是一个天才的演员，天真无邪，热情诚挚，喜欢送礼和接受礼物，看重人缘。情绪化的特点使得你容易兴奋，喜欢吹牛、说大话，天真，永远长不大，富有喜剧色彩。但是，似乎也很容易生气，爱抱怨，大嗓门，不成熟。", "c": "在工作方面，I型人是一个热情的推动者，总有新主意，色彩丰富，说干就干，能够鼓励和带领他人一起积极投入工作。可是，I型人似乎总是情绪决定一切，想哪儿说哪儿，而且说得多干得少，遇到困难容易失去信心，杂乱无章，做事不彻底，爱走神儿，爱找借口。喜欢轻松友好的环境，非常害怕被拒绝。", "d": "在人际关系方面，I型人容易交上朋友，朋友也多。关爱朋友，也被朋友称赞。爱当主角，爱受欢迎喜欢控制谈话内容。可是，喜欢即兴表演的特点使得I型人常常不能仔细理解别人，而且健忘多变。", "e": "有影响力、有说服力、友好、善于言辞、健谈、乐观积极、善于交际"})
        if c >10:
            return render(request, 'wenjuan/DISCans.html', {"a":"高S型的人通常较为平和，知足常乐，不愿意主动前进", "b":"在情感方面，S型人是一个温和主义者，悠闲，平和，有耐心，感情内藏，待人和蔼，乐于倾听，遇事冷静，随遇而安。 S型喜欢使用一句口头禅：“不过如此。”这个特点使得S型总是缺乏热情，不愿改变。", "c": "在工作方面， S型能够按部就班地管理事务，胜任工作并能够持之以恒。奉行中庸之道，平和可亲，一方面习惯于避免冲突，另一方面也能处变不惊。但是， S型似乎总是慢吞吞的，很难被鼓动，懒惰，马虎，得过且过。由于害怕承担风险和责任，宁愿站在一边旁观。很多时候， S型总是焉有主意，有话不说，或折衷处理。 ", "d": "在人际关系方面， S型是一个容易相处的人，喜欢观察人、琢磨人，乐于倾听，愿意支持。可是，由于不以为然， S型也可能显得漠不关心，或者嘲讽别人。", "e": "可靠、深思熟虑、亲切友好、有毅力、坚持不懈、善倾听者、全面周到、自制力强"})
        if d >10:
            return render(request, 'wenjuan/DISCans.html', {"a":"高C型的人通常是喜欢追求完美的专业型人才", "b":"在情感方面，C型人是一个性格深沉的人，严肃认真，目的性强，善于分析，愿意思考人生与工作的意义，喜欢美丽，对他人敏感，理想主义。但是， C型人总是习惯于记住负面的东西，容易情绪低落，过分自我反省，自我贬低，离群索居，有忧郁症倾向。", "c": "在工作方面， C型人是一个完美主义者，高标准，计划性强，注重细节，讲究条理，整洁，能够发现问题并制订解决问题的办法，喜欢图表和清单，坚持己见，善始善终。但是， C型人也很可能是一个优柔寡断的人，习惯于收集信息资料和做分析，却很难投入到实际运作的工作中来。容易自我否定，因此需要别人的认同。同时，也习惯于挑剔别人，不能忍受别人的工作做不好。", "d": "对待人际关系方面， C型人一方面在寻找理想伙伴，另一方面却交友谨慎。能够深切地关怀他人，善于倾听抱怨，帮助别人解决困难。但是， C型人似乎始终有一种不安全感，以致于感情内向，退缩，怀疑别人，喜欢批评人事，却不喜欢别人的反对。", "e": "遵从、仔细、有条不紊、严谨、准确、完美主义者、逻辑性强"})
    return render(request, 'wenjuan/wenjuan.html')

class MbtiModel(BootStrapModelForm):
    class Meta:
        model = models.Mbti
        exclude = ('user',)
def Mbti(request):
    if request.method == 'GET':
        form = MbtiModel()
        return render(request, 'wenjuan/wenjuan.html', {"form": form, "title":"MBTI问卷", "content": "MBTI测试前须知：1、参加测试的人员请务必诚实、独立地回答问题，只有如此，才能得到有效的结果。\n 2、《性格分析报告》展示的是你的性格倾向，而不是你的知识、技能、经验。\n 3、MBTI提供的性格类型描述仅供测试者确定自己的性格类型之用，性格类型没有好坏，只有不同。每一种性格特征都有其价值和优点，也有缺点和需要注意的地方。清楚地了解自己的性格优劣势，有利于更好地发挥自己的特长，而尽可能的在为人处事中避免自己性格中的劣势，更好地和他人相处，更好地作重要的决策。\n 4、本测试分为四部分，共93题；需时约18分钟。所有题目没有对错之分，请根据自己的实际情况选择。选择A或者B，请“√”。只要你是认真、真实地填写了测试问卷，那么通常情况下你都能得到一个确实和你的性格相匹配的类型。希望你能从中或多或少地获得一些有益的信息。"})
    form = MbtiModel(data= request.POST)
    if form.is_valid():
        form.save()
        row_object = form.cleaned_data
        # print(row_object)
        E = 0
        I = 0
        S = 0
        N = 0
        T = 0
        F = 0
        J = 0
        P = 0
        # print(row_object)
        for i in row_object:
            # print(row_object[i])
            if row_object[i] == 1:
                E += 1
            if row_object[i] == 2:
                I += 1
            if row_object[i] == 3:
                S += 1
            if row_object[i] == 4:
                N += 1
            if row_object[i] == 5:
                T += 1
            if row_object[i] == 6:
                F += 1
            if row_object[i] == 7:
                J += 1
            if row_object[i] == 8:
                P += 1
        # print(E,I,S,N,T,F,J,P)
        str = ""
        if E<=I:
            str += 'I'
        if E>I:
            str += 'E'
        if S<=N:
            str += 'N'
        if S>N:
            str += 'S'
        if T<=F:
            str += 'F'
        if T>F:
            str += 'T'
        if J<=P:
            str += 'P'
        if J>P:
            str += 'J'
        if str == 'ISTJ':
            return render(request, 'wenjuan/MBTIans1.html')
        if str == 'ISFJ':
            return render(request, 'wenjuan/MBTIans2.html')
        if str == 'INFJ':
            return render(request, 'wenjuan/MBTIans3.html')
        if str == 'INTJ':
            return render(request, 'wenjuan/MBTIans4.html')
        if str == 'ISTP':
            return render(request, 'wenjuan/MBTIans5.html')
        if str == 'ISFP':
            return render(request, 'wenjuan/MBTIans6.html')
        if str == 'INFP':
            return render(request, 'wenjuan/MBTIans7.html')
        if str == 'INTP':
            return render(request, 'wenjuan/MBTIans8.html')
        if str == 'ESTP':
            return render(request, 'wenjuan/MBTIans9.html')
        if str == 'ESFP':
            return render(request, 'wenjuan/MBTIans10.html')
        if str == 'ENFP':
            return render(request, 'wenjuan/MBTIans11.html')
        if str == 'ENTP':
            return render(request, 'wenjuan/MBTIans12.html')
        if str == 'ESTJ':
            return render(request, 'wenjuan/MBTIans13.html')
        if str == 'ESFJ':
            return render(request, 'wenjuan/MBTIans14.html')
        if str == 'ENFJ':
            return render(request, 'wenjuan/MBTIans15.html')
        if str == 'ENTJ':
            return render(request, 'wenjuan/MBTIans16.html')
    return render(request, 'wenjuan/wenjuan.html')


def about(request):
    return render(request, 'about.html')