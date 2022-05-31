from django.shortcuts import render
from django.http import HttpResponse
from .models import StandardSeat, StudyRoomSeat, LeisureSeat
from login.models import user_seat
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import datetime


# 查找自习室的空闲座位
def study_room(request):
    # 查找自习室的座位状态为空的座位信息
    infor_list = StudyRoomSeat.objects.filter(status=0).values("id", "floor")  # 获取座位数据，values返回的是包含字典的列表
    # 判断是否查询到状态为0的座位
    if infor_list.exists():
        context = "自习室"
        long = len(infor_list)
        return render(request, "return.html", {'infor_list': infor_list, 'msg': context, 'len': long})  # 将数据返回到显示页面上
    else:
        return HttpResponse("暂时没有空座。")


# 查找标准区的空闲座位
def standard(request):
    # 查找标准区的座位状态为空的座位信息
    infor_list = StandardSeat.objects.filter(status=0).values("id", "floor")
    if infor_list.exists():

        context = "标准区"
        long = len(infor_list)
        return render(request, "return.html", {'infor_list': infor_list, 'msg': context, 'len': long})
    else:
        return HttpResponse("暂时没有空座。")


# 查找休闲区的空闲座位
def leisure(request):
    # 查找休闲区的座位状态为空的座位信息
    infor_list = LeisureSeat.objects.all().filter(status=0).values("id", "floor")
    if infor_list.exists():
        context = "休闲区"
        long = len(infor_list)
        return render(request, "return.html", {'infor_list': infor_list, 'msg': context, 'len': long})
    else:
        return HttpResponse("暂时没有空座。")


# 将选座数据在数据库中进行修改提交
def update(request):
    # 获取选择的座位编号
    localtime = str(datetime.datetime.now())   # 获取当前时间
    select_id = request.POST.get("select_id")
    # 判断输入的编号是属于什么类型的座位
    if "z" in select_id:  # 若座位类型属于自习室
        status_A = StudyRoomSeat.objects.filter(id=select_id).values("status")  # 该编号的座位状态
        if status_A[0].get("status") == 0:
            # 将用户的状态修改
            user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
            user_seat.objects.filter(seat_id=select_id).update(status='已预约')  # 将所选的用户状态置为1已预约
            user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)   # 在表中增加预约时间
            StudyRoomSeat.objects.filter(id=select_id).update(status=1)  # 修改所选座位状态为1已预约
            context = {"msg": select_id}
            return render(request, "response.html", context)
        else:
            return HttpResponse("座位编号有误！！！")

    elif "b" in select_id:
        status_B = StandardSeat.objects.filter(id=select_id).values("status")
        if status_B[0].get("status") == 0:
            # 将用户的状态修改
            user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
            user_seat.objects.filter(seat_id=select_id).update(status='已预约')
            user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)  # 在表中增加预约时间
            StandardSeat.objects.filter(id=select_id).update(status=1)
            context = {"msg": select_id}
            return render(request, "response.html", context)
        else:
            return HttpResponse("座位编号有误！！！")

    elif "x" in select_id:
        status_C = LeisureSeat.objects.filter(id=select_id).values("status")  # 休闲区
        if status_C[0].get("status") == 0:
            # 将用户的状态修改
            user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
            user_seat.objects.filter(seat_id=select_id).update(status='已预约')
            user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)  # 在表中增加预约时间
            LeisureSeat.objects.filter(id=select_id).update(status=1)
            context = {"msg": select_id}
            return render(request, "response.html", context)
        else:
            return HttpResponse("座位编号有误！！！")
    # 当都不符合时
    else:
        return HttpResponse("座位编号有误！！！")


# 进行用户签到，
def sign_in(request):
    now_time = datetime.datetime.now()  # 获取当前时间
    # 获取用户预约时的时间
    user_id = request.session.get("user")
    a1 = user_seat.objects.filter(User_id=user_id).values('timeStatus')[0].get('timeStatus')
    old_time = datetime.datetime.strptime(a1[:-7], "%Y-%m-%d %H:%M:%S")   # 将从数据库中取出数据并转化为能够进行计算的类型
    if (now_time - old_time).total_seconds() > 10:   # 签到时间减去预约时间是否大于10秒
        # 签到失败需要更新user_seat表中的状态，并跳转到预约界面
        user_seat.objects.filter(User_id=user_id).update(status="未预约", timeStatus=now_time)
        return render(request, "index.html")
    else:
        # 签到成功后，将user_seat表数据更新，将用户状态置为2，时间改变为入馆时间
        user_seat.objects.filter(User_id=user_id).update(status="已就坐", timeStatus=now_time)

        return render(request, "exhibit.html")


@csrf_exempt  # 忽略csrf认证
# 处理用户离馆情况，需要将用户的数据进行更新
def leave(request):
    userid = request.session.get("user")
    seatid = user_seat.objects.filter(User_id=userid).values("seat_id")[0].get("seat_id")  # 查询用户所选的座位编号
    user_seat.objects.filter(User_id=userid).delete()  # 将临时记录的表中的用户数据删除

    if "z" in seatid:
        StudyRoomSeat.objects.filter(id=seatid).update(status=0)
    elif "b" in seatid:
        StandardSeat.objects.filter(id=seatid).update(status=0)
    else:
        LeisureSeat.objects.filter(id=seatid).update(status=0)
    return redirect('/login/')  # 用户离馆后，返回到登录页面；没有删除session会默认登录
