from django.urls import path
from . import views

urlpatterns = [
    path('fc/',views.free_course, name='free'),
    path('bg/',views.blog, name='blog')
]

