from django.urls import path
from . import views

urlpatterns = [
    path('',views.course, name='machinelearning'),
    path('ds/', views.Data_Science, name='datascience'),
    path('bd/',views.Big_Data, name='bigdata'),
    path('da/',views.Data_analytics, name='analytics'),
    path('dl/',views.Deep_Learning, name='deeplearning'),
]