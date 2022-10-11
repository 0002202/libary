from django.shortcuts import render
from login.models import Student
from seat.models import LeisureSeat, StandardSeat, StudyRoomSeat
from .models import order_seat


# 处理用户预约座位
def show_order(request):
    # 获取用户信息
    user_id = request.session.get('order')
    # 只有用户信誉积分等于3分时，才可以使用预约座位的功能
    order_integral = Student.objects.filter(User_id=user_id).values("integral")[0].get('integral')
    if order_integral != 3:
        return render(request, "index.html", {'msg': '您的信誉积分不足3分，不能使用预约系统', 'uid': user_id, 'integral': order_integral})
    else:
        # 进入预约选座页面
        return render(request, "yuyue.html")


# 查询座位
def select_order_seat():
    # 查询被预约的座位
    order_seat_list = order_seat.objects.values_list('Seat_id', 'day', 'day_time')
    # 查询所有座位
    # for j in range(len(order_seat_list)):
    #     order_seat_id = [i for i in order_seat_list][j][0]  # 座位编号
    #     order_seat_day = [i for i in order_seat_list][j][1]  # 日期天数
    #     order_seat_time = [i for i in order_seat_list][j][2]  # 具体时间
    return order_seat_list

# 进行预约座位的处理
def seat_order(request):
    # seat_id =
    select_order_seat()
