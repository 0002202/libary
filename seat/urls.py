from django.urls import path
from seat.views import study_room, standard, leisure, update, sign_in, leave

urlpatterns = [
    path("A/", study_room),   # 处理自习室
    path("B/", standard),           # 处理标准区
    path("C/", leisure),            # 处理休闲区
    path("response/", update),      # 进行更新数据
    path("sign_in/", sign_in),      # 用户签到
    path("leave/", leave)           # 用户离馆后
]