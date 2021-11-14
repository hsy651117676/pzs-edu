from main import views
from django.urls import path,include,re_path

urlpatterns = [
    path('regiontree', views.Fregion),
      ]

