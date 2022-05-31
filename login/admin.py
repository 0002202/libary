from django.contrib import admin
from .models import Student


# 将模型提交给管理员进行管理
admin.site.register(Student)