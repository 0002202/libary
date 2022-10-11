from django.contrib import admin
from django.urls import path, include
from login.views import register, show_login, show_register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("denglu/", login, name="denglu"),   # 处理登陆
    path('login/', show_login),              # 登录页面
    path('register/', show_register, name='register'),  # 注册页面
    path('zhuce/', register),
    path("seat/", include("seat.urls"))      # 将seat下的所有提交到seat的路由文件进行处理
]