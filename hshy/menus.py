import os
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.shortcuts import render
from django.views.decorators import csrf
from django.contrib import auth
from django.contrib.auth import  login

def nbxt_menu():
    # 数据填报菜单 
    yearSetting= """ <a href="javascript:void(0);" src="/annualreport/yearSettingedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-date'">年度设置</a>"""
    student= """ <a href="javascript:void(0);" src="/annualreport/studentedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-group'">学生信息维护</a>"""
    teacher= """ <a href="javascript:void(0);" src="/annualreport/teacheredit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-user-gray'">教师信息维护</a>"""
    report= """ <a href="javascript:void(0);" src="/annualreport/reportedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-database-edit'">年报信息填报</a>"""
    dataFilling="""<div title="年报数据填报" data-options="iconCls:'icon-large-smartart'" style="padding:0px;">"""+ yearSetting + student + teacher + report + """</div>"""

    # 数据汇总菜单
    student= """ <a href="javascript:void(0);" src="/annualreport/studentSummary/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-group-go'">学生信息汇总</a>"""
    teacher= """ <a href="javascript:void(0);" src="/annualreport/teacherSummary/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-user-go'">教师信息汇总</a>"""
    report= """ <a href="javascript:void(0);" src="/annualreport/reportSummary/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-database-go'">报表数据汇总</a>"""
    dataSummary="""<div title="年报数据汇总" data-options="iconCls:'icon-large-shapes'" style="padding:0px;"> """ +  student + teacher + report + """</div>"""
    
    # 指标分析菜单 
    dataAnalysis="""<div title="年报指标分析" data-options="iconCls:'icon-large-chart'" style="padding:0px;"> </div>"""
    
    curriculum= """ <a href="javascript:void(0);" src="/curriculum/index/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-basket-go'">自动排课系统</a>"""
    toolsbox="""<div title="常用工具集" data-options="iconCls:'icon-large-clipart'" style="padding:0px;">"""+ curriculum +""" </div>"""

    menu=dataFilling + dataSummary + dataAnalysis + toolsbox 
    return menu

def search_menu():
    # 查询菜单 
    yearSetting= """ <a href="javascript:void(0);" src="/annualreport/yearSettingedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-search'">年度设置</a>"""
    student= """ <a href="javascript:void(0);" src="/annualreport/studentedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-search'">学生信息维护</a>"""
    teacher= """ <a href="javascript:void(0);" src="/annualreport/teacheredit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-search'">教师信息维护</a>"""
    report= """ <a href="javascript:void(0);" src="/annualreport/reportedit/" class="easyui-linkbutton cs-navi-tab"" data-options="iconCls:'icon-search'">年报信息填报</a>"""
    dataFilling="""<div title="数据填报" data-options="iconCls:'icon-large-smartart'" style="padding:0px;">"""+ yearSetting + student + teacher + report + """</div>"""

    menu=dataFilling 
    return menu


