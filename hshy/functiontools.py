#-*- coding: utf-8 -*-
import os
from . import views
from django.shortcuts import render,HttpResponse
from django.views.decorators import csrf
from django.http import JsonResponse
from nbxt.models import *
from django.db.models import Q,F
import json,requests
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt
def treemenu(request):
    ppower=request.GET['power']
    ppid=request.GET['pid']
    ctx ={}
    table_title=['表名称']
    mydata=tablepower.objects.filter(pid=ppid,power=ppower).extra(select={'id': 'mid'}).values('id','text')
    menu=[entry for entry in mydata]
    menu=list(menu)
    menu=json.dumps(menu,ensure_ascii=False)
    print(menu)
    #menu='''[{"id":"1","text":"kj","state":"open"}]'''
    ctx['dic']={"table_title":table_title,"menu":menu}
    return HttpResponse(menu,'application/json') 


   
