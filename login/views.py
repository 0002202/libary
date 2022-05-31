from django.shortcuts import render
from .models import Student, user_seat


# 展示注册页面
def show_register(request):
    return render(request, 'register.html')


# 处理注册表单数据，将获取到的数据存入数据库
def register(request):
    context = {}
    # 获取表单数据
    user_id = request.POST.get("id")
    name = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    re_password = request.POST.get("re_password")
    data = Student(User_id=user_id, name=name, email=email, password=password)
    # 判断用户名是否重复和两次密码是否一致
    if password == re_password:
        data.save()  # 将获取到的数据进行保存数据库
        context['msg'] = '注册成功'
        return render(request, "register.html", context)
    else:
        context['msg'] = '两次密码不一致！！！'
        return render(request, "register.html", context)


def show_login(request):
    is_login = request.session.get("is_login", False)
    if is_login:       # 如果携带的 session为True，则直接返回主页面
        userid = request.session.get("user")
        # 将用户记录到user_seat表中
        return re
        # return render(request, "index.html", context={'name': userid})
    else:
        return render(request, "login.html")


# 处理登录表单数据
def login(request):
    context = {}
    userID = request.POST.get("user_id")
    pd = request.POST.get("password")
    # 将获取到的数据在数据库中进行查找，若存在则登录成功
    # 获取数据库中内容,判断密码是否一致
    password = Student.objects.filter(User_id=userID).values("password")
    if pd == password[0].get('password'):  # 登录成功
        context["name"] = userID  # 返回用户名
        data = user_seat(User_id=userID)  # 将登入的用户记录在表中
        data.save()
        request.session['is_login'] = True
        request.session['user'] = userID
        return render(request, "index.html", context)
    else:
        context["msg"] = "账号或密码出错！！！"
        return render(request, 'login.html', context)
