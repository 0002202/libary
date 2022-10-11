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
        context['msg'] = '注册成功.'
        return render(request, "register.html", context)
    else:
        context['msg'] = '两次密码不一致！！！'
        return render(request, "register.html", context)


# 展示登陆页面
def show_login(request):
    is_login = request.session.get("is_login", False)
    if is_login:  # 如果携带的session为True，则直接返回主页面
        userID = request.session.get("order")
        integral = Student.objects.filter(User_id=userID).values("integral")[0].get('integral')
        if integral == 0:
            return render(request, "integral.html")
        return render(request, "index.html", context={'name': userID, 'integral': integral})
    else:
        return render(request, "login.html")


# 处理登录表单数据
def login(request):
    context = {}
    userID = request.POST.get("user_id")
    pd = request.POST.get("password")
    # 获取数据库中内容,判断信息是否满足
    password = Student.objects.filter(User_id=userID).values("password")[0].get('password')
    is_integral = Student.objects.filter(User_id=userID).values("integral")[0].get('integral')
    if password == pd and is_integral != 0:  # 密码正确
        context["uid"] = userID  # 返回学号
        context["integral"] = is_integral  # 返回用户当前信誉积分
        # 判断用户是否已经存在表中
        select_status = request.session.get("select_status", False)  # 获取选座状态，非True则转为False
        if select_status is False:  # 若为True则代表用户已经记录在表中
            data = user_seat(User_id=userID)  # 将登入的用户记录在表中
            data.save()
        request.session['is_login'] = True  # 记录用户登陆状态
        request.session['order'] = userID    # 记录用户编号
        return render(request, "index.html", context)
    else:
        if is_integral == 0 and password == pd:
            return render(request, "integral.html")
        else:
            context["msg"] = "账号或密码出错！！！"
            return render(request, 'login.html', context)
