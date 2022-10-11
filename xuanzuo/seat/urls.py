from django.urls import path
from seat.views import study_room, standard, leisure, update, sign_in, leave, random_seat, filter_seat
from order.views import show_order, seat_order
urlpatterns = [
    path("filter/", filter_seat),     # 过滤选座
    path("A/", study_room),           # 处理自习室
    path("B/", standard),             # 处理标准区
    path("C/", leisure),              # 处理休闲区
    path("random/", random_seat),     # 随机选座
    path("response/", update),        # 进行更新数据
    path("sign_in/", sign_in),        # 用户签到
    path("leave/", leave),            # 用户离馆后
    path("show_order/", show_order),  # 展示预约座位
    path("order/", seat_order)        # 预约座位
]