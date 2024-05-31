from django.contrib import admin 
from django.urls import path 
from . import views 

app_name = 'main'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('myhistory/', views.HistoryView.as_view(), name='myhistory'),
    path('', views.query_view, name='query_view'),
]
