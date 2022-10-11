from django.shortcuts import render
from django.http import HttpResponse
from .models import StandardSeat, StudyRoomSeat, LeisureSeat
from login.models import user_seat, Student, black_user
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import datetime
import random


# 过滤查询座位
def filter_seat(request):
    # 定义字典
    room_dict = {'自习室': StudyRoomSeat, '标准区': StandardSeat, '休闲区': LeisureSeat}
    # 获取用户选择的数据
    seat_room = request.POST.get('select_room')  # 座位类型
    seat_floor = request.POST.get('select_floor')  # 座位所在楼层
    seat_power = request.POST.get('power')  # 座位是否拥有电源
    seat_stairs = request.POST.get('stairs')  # 座位是否靠近走廊
    # priority = request.POST.get('priority')               # 用户选项的优先级
    # 将数据转换为能用的数据
    if seat_power is not None:
        seat_power = [1]
    else:
        seat_power = [0, 1]
        # 查询不靠近电源的座位
    if seat_stairs is not None:
        seat_stairs = [1]
    else:
        seat_stairs = [0, 1]
    # 处理数据
    context = seat_room
    seat_type = room_dict.get(seat_room)  # 获取座位类型
    # 判断用户选择的优先级
    # select_priority = {'座位类型':seat_type, '楼层':seat_floor, '靠近电源':'seat_power', '靠近走廊':'seat_stairs'}
    # seatinfor_priority = select_priority.get(priority)     # 获取用户优先级
    select_status = request.session.get("select_status", False)  # 通过session判读用户是否重复选座，非True则转为False
    if select_status is False:
        # 没有符合选座要求的座位
        try:
            # 查找所选类型中且符合选项的空位
            seat_list = seat_type.objects.filter(status=0, floor=seat_floor, power__in=seat_power,
                                                 stairs__in=seat_stairs).values("id", "floor", "power", "stairs")
            # print(seat_id)
            if seat_list.exists():
                long = len(seat_list)
                return render(request, "return.html",
                              {'infor_list': seat_list, 'msg': context, 'len': long})  # 将数据返回到显示页面上
            else:
                return render(request, "kongzuo.html")
        except ValueError:
            return render(request, "kongzuo.html")
    else:
        return HttpResponse("一个人只能选座一次")


# 查找自习室的空闲座位
def study_room(request):
    # 首先判断用户是否重复选座
    select_status = request.session.get("select_status", False)  # 非True则转为False
    if select_status is False:
        # 查找自习室的座位状态为空的座位信息
        seat_list = StudyRoomSeat.objects.filter(status=0).values("id", "floor", "power",
                                                                  "stairs")  # 获取座位数据，values返回的是包含字典的列表
        # 判断是否查询到状态为0的座位
        if seat_list.exists():
            context = "自习室"
            long = len(seat_list)  # 显示空位数量
            # 判断座位其他信息
            return render(request, "return.html", {'infor_list': seat_list, 'msg': context, 'len': long})  # 将数据返回到显示页面上
        else:
            return render(request, "kongzuo.html")
    else:
        return HttpResponse("一个人只能选座一次")


# 查找标准区的空闲座位
def standard(request):
    select_status = request.session.get("select_status", False)
    if select_status is False:
        # 查找标准区的座位状态为空的座位信息
        seat_list = StandardSeat.objects.filter(status=0).values("id", "floor", "power", "stairs")
        if seat_list.exists():

            context = "标准区"
            long = len(seat_list)
            return render(request, "return.html", {'infor_list': seat_list, 'msg': context, 'len': long})
        else:
            return render(request, "kongzuo.html")
    else:
        return HttpResponse("一个人只能选座一次")


# 查找休闲区的空闲座位
def leisure(request):
    select_status = request.session.get("select_status", False)
    if select_status is False:
        # 查找休闲区的座位状态为空的座位信息
        seat_list = LeisureSeat.objects.all().filter(status=0).values("id", "floor", "power", "stairs")
        if seat_list.exists():
            context = "休闲区"
            long = len(seat_list)
            return render(request, "return.html", {'infor_list': seat_list, 'msg': context, 'len': long})
        else:
            return render(request, "kongzuo.html")
    else:
        return HttpResponse("一个人只能选座一次")


# 随机选座
def random_seat(request):
    # 从三个类型的座位中随机挑选状态为0的座位
    seat_list = [StudyRoomSeat, StandardSeat, LeisureSeat]
    seat_type = random.choice(seat_list)  # 随机选择一个座位类型
    uid = request.session.get("order")       # 用户id
    # 没有空座位会报错 
    try:
        seatid_list = seat_type.objects.all().filter(status=0).values("id", "floor", "power",
                                                                      "stairs")  # 查找座位类型为空座的信息，是一个列表
        seat = random.choice(seatid_list)       # seat包含座位信息，是一个字典

        seatid = seat.get("id")  # 座位编号
        seattype = seat_type     # 座位类型
        seatfloor = seat.get("floor")  # 座位所在楼层
        seatpower = seat.get("power")  # 电源
        seatstairs = seat.get("stairs")  # 走廊
        request.session['random_seat'] = seatid  # 用session记录座位编号
        return render(request, "random_seat.html", {'t': seattype, 'n': seatid, 'f': seatfloor, 'p': seatpower, 's': seatstairs})
    except KeyError:
        return render(request, "kongzuo.html")


# 将选座数据在数据库中进行修改提交
def update(request):
    localtime = str(datetime.datetime.now())   # 获取当前时间
    select_id = request.POST.get("select_id")  # 获取选择的座位编号
    # 判断用户是否选择随机选座，可能会直接选座
    if select_id is None:
        select_id = request.session.get('random_seat')  # 将记录座位的session值取出来

    # 判断输入的编号是属于什么类型的座位
    if "z" in select_id:  # 若座位类型属于自习室
        # 可能座位号不存在
        try:
            status_A = StudyRoomSeat.objects.filter(id=select_id).values("status")  # 该编号的座位状态
            if status_A[0].get("status") == 0:
                # 将用户的状态修改
                user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
                user_seat.objects.filter(seat_id=select_id).update(status='已预约')  # 将所选的用户状态置为1已预约
                user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)  # 在表中增加预约时间
                # 防止被人重复预约，先在数据库中进行修改数据
                StudyRoomSeat.objects.filter(id=select_id).update(status=1)  # 修改所选座位状态为1已预约
                floor = StudyRoomSeat.objects.filter(id=select_id).values("floor")[0].get('floor')
                context = {"msg": select_id, "floor": floor}
                # 防止重复选座，记录session值
                request.session['select_status'] = True  # 记录用户选座状态
                return render(request, "response.html", context)
            else:
                return HttpResponse("座位编号有误！！！")
        except IndexError:
            return HttpResponse("座位编号有误！！ ")

    elif "b" in select_id:
        try:
            status_B = StandardSeat.objects.filter(id=select_id).values("status")
            if status_B[0].get("status") == 0:
                # 将用户的状态修改
                user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
                user_seat.objects.filter(seat_id=select_id).update(status='已预约')
                user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)  # 在表中增加预约时间
                StandardSeat.objects.filter(id=select_id).update(status=1)
                floor = StandardSeat.objects.filter(id=select_id).values("floor")[0].get('floor')
                context = {"msg": select_id, "floor": floor}
                request.session['select_status'] = True
                return render(request, "response.html", context)
            else:
                return HttpResponse("座位编号有误！！！")
        except IndexError:
            return HttpResponse("座位编号有误!！！！ ")
    elif "x" in select_id:
        try:
            status_C = LeisureSeat.objects.filter(id=select_id).values("status")  # 休闲区
            if status_C[0].get("status") == 0:
                # 将用户的状态修改
                user_seat.objects.filter(seat_id="未预约座位").update(seat_id=select_id)
                user_seat.objects.filter(seat_id=select_id).update(status='已预约')
                user_seat.objects.filter(seat_id=select_id).update(timeStatus=localtime)  # 在表中增加预约时间
                LeisureSeat.objects.filter(id=select_id).update(status=1)
                floor = LeisureSeat.objects.filter(id=select_id).values("floor")[0].get('floor')
                context = {"msg": select_id, "floor": floor}
                request.session['select_status'] = True
                return render(request, "response.html", context)
            else:
                return HttpResponse("座位编号有误！！！")
        except IndexError:
            return HttpResponse("座位编号有误!！！！ ")
    # 当都不符合时
    else:
        return HttpResponse("座位编号有误！！！")


# 用户签到失败扣分
def reduce(request, uid):
    i = Student.objects.filter(User_id=uid).values('integral')[0].get('integral')  # 获取用户当前信誉积分（未扣分前）
    text = {}
    if int(i) == 1:
        Student.objects.filter(User_id=uid).update(integral=0)       # 扣为0
        HttpResponse("由于您的信誉积分过低，将停止使用该系统一周！")
        # 停用系统！！
        # 当用户的信誉积分为0后，则无法使用该预约系统
    elif int(i) == 3:
        Student.objects.filter(User_id=uid).update(integral=2)       # 扣1分
        # j = Student.objects.filter(User_id=uid).values('integral')[0].get('integral')  # 获取最新的信誉积分
    elif int(i) == 2:
        Student.objects.filter(User_id=uid).update(integral=1)       # 扣1分


# 进行用户签到
def sign_in(request):
    res = {}
    now_time = datetime.datetime.now()          # 获取当前时间
    # 获取用户预约时的时间
    user_id = request.session.get("order")       # 当前登录的用户id
    time_date = user_seat.objects.filter(User_id=user_id).values('timeStatus')[0].get('timeStatus')     # 获取当前用户的预约时间
    old_time = datetime.datetime.strptime(time_date[:-7], "%Y-%m-%d %H:%M:%S")  # 将从数据库中取出数据并转化为能够进行计算的类型
    # print(old_time, type(old_time))
    # 判断签到是否超时
    if (now_time - old_time).total_seconds() > 10:  # 签到时间减去预约时间是否大于10秒
        # 签到失败需要更新user_seat表中的状态，并跳转到预约界面
        user_seat.objects.filter(User_id=user_id).update(status="未预约", timeStatus=now_time)
        del request.session['select_status']  # 删除用户的选座状态
        # 用户信誉积分减少
        reduce(request, user_id)        # 调用积分处理函数，进行处理信誉积分

        # 先进行扣分，再查询当前信誉分
        is_integral = Student.objects.filter(User_id=user_id).values("integral")[0].get('integral')
        res["uid"] = user_id            # 用户编号
        res["integral"] = is_integral   # 用户积分
        res["msg"] = "由于您超时签到，您的信誉积分将扣1分！若信誉积分低于1分，将停用一个周预约系统！\n您当前的信誉积分为%s分" % is_integral
        # 若信誉分低于1分，则跳转到非登录页面
        if is_integral > 0:
            return render(request, "index.html", res)  # 重新返回选座页面
        else:
            # 同时将该用户存入黑名单，并开始计时
            black_now_time = datetime.datetime.now()  # 获取信誉分为0的时间
            data = black_user(User_id=user_id, timeStatus=black_now_time)
            data.save()     # 只进行保存数据

            return render(request, "integral.html", res)
    else:
        # 签到成功后，将user_seat表数据更新，将用户状态置为已就坐，时间改变为入馆时间
        user_seat.objects.filter(User_id=user_id).update(status="已就坐", timeStatus=now_time)
        # 判断用户就座状态
        request.session['seat_status'] = True  # 记录用户就座情况
        return render(request, "exhibit.html")


@csrf_exempt  # 忽略csrf认证
# 处理用户离馆情况，需要将用户的数据进行更新
def leave(request):
    # 删除session，可能没有session
    try:
        del request.session['select_status']  # 删除用户的选座状态
        del request.session['random_seat']     # 删除用户随机选座的编号
        del request.session['is_login']  # 删除用户的登陆状态
    except KeyError:
        del request.session['is_login']

    userid = request.session.get("order")
    seatid = user_seat.objects.filter(User_id=userid).values("seat_id")[0].get("seat_id")  # 获取用户所选的座位编号
    user_seat.objects.filter(User_id=userid).delete()  # 将临时记录的表中的用户数据删除
    # 修改座位状态，判断座位属于哪个类型的
    if "z" in seatid:
        StudyRoomSeat.objects.filter(id=seatid).update(status=0)  # 更新离馆后座位状态
    elif "b" in seatid:
        StandardSeat.objects.filter(id=seatid).update(status=0)
    else:
        LeisureSeat.objects.filter(id=seatid).update(status=0)
    del request.session['order']  # 删除用户登陆账号
    return redirect('/login/')   # 用户离馆后，返回到登录页面；没有删除session会默认登录
