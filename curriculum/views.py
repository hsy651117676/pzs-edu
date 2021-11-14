#-*- coding: utf-8 -*-
import os
from . import views
from django.shortcuts import render,HttpResponse
from django.views.decorators import csrf
from django.http import JsonResponse
from nbxt.models import *
from curriculum.models import *
from django.db.models import Q
import json,requests
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
def Findex(request):
    ctx ={}
    tableTitle=['序号']
    ctx['dic']={"title":tableTitle}
    return render(request, "curriculum/index.html",ctx)

def FschoolSite(request):
    ctx ={}
    tableTitle=['序号']
    ctx['dic']={"title":tableTitle}
    return render(request, "curriculum/schoolsite.html",ctx)

def FgradeClass(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    data=[{"level":"01","code":"一年级","name":"一","num":1},
            {"level":"02","code":"二年级","name":"二","num":1},
            {"level":"03","code":"三年级","name":"三","num":1},
            {"level":"04","code":"四年级","name":"四","num":1},
            {"level":"05","code":"五年级","name":"五","num":1},
            {"level":"06","code":"六年级","name":"六","num":1},
            {"level":"07","code":"七年级","name":"七","num":1},
            {"level":"08","code":"八年级","name":"八","num":1},
            {"level":"09","code":"九年级","name":"九","num":1},
            {"level":"10","code":"高中一年级","name":"高一","num":1},
            {"level":"11","code":"高中二年级","name":"高二","num":1},
            {"level":"12","code":"高中三年级","name":"高三","num":1}
            ]
    ctx['dic']={"data":data,"name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/gradeclass.html",ctx)

def FclassHour(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/classhour.html",ctx)

def FsetTeacher(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/setteacher.html",ctx)

def FsetCourse(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    data=[{"level":"01","code":"语文","name":"一","num":1},
            {"level":"02","code":"数学","name":"二","num":1},
            {"level":"03","code":"英语","name":"三","num":1},
            {"level":"04","code":"历史","name":"四","num":1},
            {"level":"05","code":"五年级","name":"五","num":1},
            {"level":"06","code":"六年级","name":"六","num":1},
            {"level":"07","code":"七年级","name":"七","num":1},
            {"level":"08","code":"八年级","name":"八","num":1},
            {"level":"09","code":"九年级","name":"九","num":1},
            {"level":"10","code":"高中一年级","name":"高一","num":1},
            {"level":"11","code":"高中二年级","name":"高二","num":1},
            {"level":"12","code":"高中三年级","name":"高三","num":1}
            ]
    ctx['dic']={"data":data,"name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/setcourse.html",ctx)

def FautoCourse(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/autocourse.html",ctx)

def FoutCourse(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称", "table_title":table_title}
    return render(request, "curriculum/outcourse.html",ctx)

@csrf_exempt
def Fmenu(request):
    menu=[{"id":11,"text":"1学校场地"},{"id":12,"text":"2年级班级"},{"id":13,"text":"3课时设置"},{"id":14,"text":"4科目设置"},{"id":15,"text":"5任课教师"},{"id":16,"text":"6开始排课"},{"id":17,"text":"7排课结果"}]
    menu=json.dumps(menu,ensure_ascii=False)
    return HttpResponse(menu,'application/json') 

