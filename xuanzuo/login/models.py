from django.db import models


# 注册系统的用户信息
class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="姓名", blank=False)
    User_id = models.CharField(max_length=100, verbose_name="学号", primary_key=True)  # 主键
    email = models.EmailField(verbose_name="邮箱", default="", blank=False)
    password = models.CharField(max_length=100, verbose_name="密码", blank=False)
    integral = models.IntegerField(verbose_name="信誉积分", default=3, blank=False)  # 用户的信誉积分，默认为3

    class Mate:
        db_table = "userDate"


# 只记录登入系统的用户，登出系统后将其删除
class user_seat(models.Model):
    User_id = models.CharField(max_length=1000, verbose_name="学号", primary_key=True)  # 主键
    seat_id = models.CharField(max_length=1000, verbose_name="所坐位置", blank=False, default="未预约座位")
    # 用户是预约状态或已就坐状态，默认都是未预约状态，1表示预约，2表示已就坐
    status = models.CharField(max_length=100, verbose_name="用户状态", default="未预约")
    timeStatus = models.CharField(max_length=1000, default=0, blank=False)  # 预约时间，当用户预选了座位之后进行时间登记


# 黑名单，记录用户拉黑时间，构建有效期
class black_user(models.Model):
    User_id = models.CharField(max_length=100, verbose_name="学号", primary_key=True)  # 主键
    timeStatus = models.CharField(max_length=1000, default=0, blank=False)  # 拉黑时间,默认0
    # 若时间已经过一周，则信誉分加1分，并退出黑名单;（信誉积分最大3分）
