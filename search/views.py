# -*- coding: utf-8 -*-
import os
from . import views
from django.shortcuts import render,HttpResponse
from django.views.decorators import csrf
from TestModel.models import *
from django.db.models import Q
import json,requests
from django.core import serializers
# from django.views.decorators.csrf import csrf_exempt 
# @csrf_exempt

#网站查询
def Help_webs(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称","card":"学校标识码","mytitle":"请在下方输入要查询的学校名称或学校标识码进行查询", "table_title":table_title}
    return render(request, "webs.html", ctx)
#网站查询ajax
def Help_webs_ajax(request):
    pageNumber=request.POST['pageNumber']
    pageSize=request.POST['pageSize']
    p1=request.POST['PA1']
    mydata =webs.objects.filter(Q(category__contains=p1)).values()
    total=mydata.count()
    rows=list(mydata)
    resList = {"total":total,"rows":rows}
    ulist = json.dumps(resList,ensure_ascii=False)
    return HttpResponse(ulist)


#学校各类账号查询页面初始化
def Fschool_user(request):
    ctx ={}
    table_title=['学校账号','学校名称','系统名称','用户名称','账户类型','用户状态','备注']
    ctx['dic']={"url":"school_user/","name":"学校名称","card":"学校标识码","mytitle":"请在下方输入要查询的学校名称或学校标识码进行查询", "table_title":table_title}
    return render(request, "search.html", ctx)

#学校各类账号查询ajax
def Fschool_user_ajax(request):
    pageNumber=request.POST['pageNumber']
    pageSize=request.POST['pageSize']
    p1=request.POST['PA1']
    p2=request.POST['PA2']
    mydata =school_user.objects.filter(Q(a2__contains=p2)).values()
    total=mydata.count()
    # kk = serializers.serialize("json", mydata)
    rows=list(mydata)
    resList = {"total":total,"rows":rows}
    ulist = json.dumps(resList,ensure_ascii=False)
    return HttpResponse(ulist)

#学校基本信息查询
def Fschool_basic(request):
    ctx ={}
    table_title=['报考类别','报考学科','','','','','','','','',]
    ctx['dic']={"url":"school_user/","name":"学校名称","card":"学校标识码","mytitle":"请在下方输入要查询的学校名称或学校标识码进行查询", "table_title":table_title}
    return render(request, "search.html", ctx)

#教师成绩查询 
def Fteacher_examinstion(request):
    ctx ={}
    table_title=['报考类别','报考学科','','','','','','','','',]
    ctx['dic']={"url":"teacher_examination/","name":"姓名","card":"身份证号","mytitle":"请在下方输入你的姓名和身份证号进行查询", "table_title":table_title}
    return render(request, "search.html", ctx)
    
#学生资助信息查询
def Fstudent_funding(request):
    ctx ={}
    table_title=['学年度','学校名称','年级','班级','姓名','身份证号','家长姓名','资助类型','金额','备注',]
    ctx['json_data']="{}"
    ctx['dic']={"url":"student_funding/","name":"姓名","card":"身份证号","mytitle":"请在下方输入你要查询的姓名和身份证号进行查询", "table_title":table_title}
    return render(request, "search.html", ctx)

def Fschool_examination(request):
    ctx ={}
    table_title=['学年度','学校名称','年级','班级','姓名','身份证号','家长姓名','资助类型','金额','备注',]
    ctx['json_data']="{}"
    ctx['dic']={"url":"student_funding/","name":"姓名","card":"身份证号","mytitle":"请在下方输入你要查询的姓名和身份证号进行查询", "table_title":table_title}
    return render(request, "search.html", ctx)

