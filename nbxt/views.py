#-*- coding: utf-8 -*-
import os
from . import views
from django.shortcuts import render,HttpResponse
from django.views.decorators import csrf
from django.http import JsonResponse
from nbxt.models import *
from django.db.models import Q
import json,requests
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

def indux(request):
    ctx ={}
    table_title=['类别','网站名称','网址']
    ctx['dic']={"url":"help_webs/","name":"学校名称", "table_title":table_title}
    return render(request, "login.html", ctx)

def Freportedit(request):
    ctx ={}
    table_title=['年报信息填报']
    ctx['dic']={"table_title":table_title}
    return render(request, "annualreport/reports.html", ctx)

def reporteditFajax(request):
    pageNumber=request.POST['pageNumber']
    pageSize=request.POST['pageSize']
    p1=request.POST['PA1']
    mydata =webs.objects.filter(Q(category__contains=p1)).values()
    total=mydata.count()
    rows=list(mydata)
    resList = {"total":total,"rows":rows}
    ulist = json.dumps(resList,ensure_ascii=False)
    return HttpResponse(ulist)

@csrf_exempt
def Freportmenu(request):
    ppower=request.GET['power']
    ppid=request.GET['pid']
    pbxlx=request.GET['bxlx'] #办学类型
    if pbxlx==0:
        mydata=tablepower.objects.filter(pid=ppid,power=ppower).extra(select={'id': 'mid'}).values('id','text')
    else:
        mydata=tablepower.objects.filter(pid=ppid,power=ppower,schooltype=pbxlx).extra(select={'id': 'mid'}).values('id','text')
    menu=[entry for entry in mydata]
    menu=list(menu)
    menu=json.dumps(menu,ensure_ascii=False)
    print(menu)
    return HttpResponse(menu,'application/json') 

def Fjjload(request):
    schoolid=request.GET['schoolid']
    tableid=request.GET['table']
    tableName=request.GET['tablename']
    schooldata=jj1001.objects.filter(c01=schoolid).values('c01','c02')
    schoolname=list(schooldata)
    ctx ={}
    tableTitle=['序号']
    tableData=globals()['jj'+ tableid].objects.filter(schoolid='2021'+schoolid,versionid='01').values()
    tableData=list(tableData)
    ctx['dic']={"title":tableTitle,"data":tableData,"tableid":tableid,"tableName":tableName,"schoolname":schoolname}
    return render(request, "annualreport/Basic/JJ"+tableid+".html",ctx)


   


