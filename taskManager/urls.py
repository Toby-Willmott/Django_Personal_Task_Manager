from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as task_views

urlpatterns = [
        path('', task_views.index, name='index'),
        path('register/', task_views.register, name='register'),
        path('login/', auth_views.LoginView.as_view(template_name='taskManager/login.html'), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
