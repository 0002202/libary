"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login.views import register, show_login, show_register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("denglu/", login, name="denglu"),
    path('login/', show_login),         # 登录页面
    path('register/', show_register, name='register'),  # 注册页面
    path('zhuce/', register),
    path("seat/", include("seat.urls"))    # 将seat下的所有提交到seat的路由文件进行处理
]