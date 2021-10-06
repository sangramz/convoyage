from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.signIn, name='signIn'),
    path('register/', views.signUp, name='signUp'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tender-submission/', views.tenderSubmission, name='tenderSubmission'),
    
]
