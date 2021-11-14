#-*- coding: utf-8 -*-
from nbxt.models import jj1001 
import os
from django.shortcuts import render,HttpResponse
from django.views.decorators import csrf
from django.http import JsonResponse
from main.models import *
from django.db.models import Q,F
import json,requests
from django.forms.models import model_to_dict
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt
def Fregion(request):
    levels=int(request.GET['levels'])
    ppid=request.GET['pid']
    if levels<=3:
        mydata=regioncode.objects.filter(pid=ppid).values()
        menu=[entry for entry in mydata]
        menu=list(menu)
        menu=json.dumps(menu,ensure_ascii=False)
        return HttpResponse(menu,'application/json') 
    else: 
        if len(ppid)==12:
            mydata=jj1001.objects.filter(pid=ppid).extra(select={'id':'c01','text':'c02','level':'c26'}).values('id','text','level')
        else:
            mydata=jj1001.objects.filter(c01=ppid).extra(select={'id':'c01','text':'c02','level':'c26'}).values('id','text','level')
        menu=[entry for entry in mydata]
        menu=list(menu)
        menu=json.dumps(menu,ensure_ascii=False)
        return HttpResponse(menu,'application/json') 
    

 
