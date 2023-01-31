from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
     path('',views.home,name='home'),
#path('details',views.details,name='details'),
path('delete/<int:taskid>/',views.delete,name='delete'),
     path('update/<int:id>/',views.update,name='update'),
     path('cbvindex/',views.Tasklistview.as_view(),name='cbvindex'),
     path('cbvdetails/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetails'),
     path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
     path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
]
