from django.urls import path,re_pathfrom . import viewsurlpatterns = [    path('students/',views.students),    path('grades/', views.grades),    path('login/', views.login),    path('main/', views.main),]