from django.urls import path,re_path 
from search import views 

urlpatterns = [ 
    path('help_webs/',views.Help_webs),
    path('help_webs/ajax/',views.Help_webs_ajax),
    path('school_examination/',views.Fschool_examination),
    path('school_user/',views.Fschool_user),
    path('school_user/ajax/',views.Fschool_user_ajax),
    path('school_basic_information/',views.Fschool_examination),
    path('teacher_examination/',views.Fteacher_examinstion),

    ] 
