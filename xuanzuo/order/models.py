from django.db import models


# 创建预约座位数据库
class order_seat(models.Model):
    User_id = models.CharField(max_length=100, verbose_name="学号")
    Seat_id = models.CharField(max_length=100, verbose_name="座位编号", primary_key=True, blank=False)  # 主键
    day = models.CharField(max_length=100, verbose_name="日期", blank=False)
    day_time = models.CharField(max_length=100, verbose_name="时间段", blank=False)
    # integral = models.IntegerField(verbose_name="信誉积分", default=3, blank=False)  # 用户的信誉积分，默认为3
