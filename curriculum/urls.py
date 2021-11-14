from django.urls import path,re_path
from curriculum import views

urlpatterns = [
        path('11/',views.FschoolSite),
        path('12/',views.FgradeClass),
        path('13/',views.FclassHour),
        path('14/',views.FsetCourse),
        path('15/',views.FsetTeacher),
        path('16/',views.FautoCourse),
        path('17/',views.FoutCourse),
        path('index/',views.Findex),
        path('index/menu',views.Fmenu),
       ]
