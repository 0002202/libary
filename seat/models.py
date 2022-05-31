from django.db import models


# 馆内座位模型
# class Seat(models.Model):
#     total = models.IntegerField(max_length=100, verbose_name="座位总数", default=1000)              # 座位总数，1000个
#     status = models.BooleanField(default=True)                           # 座位状态，Ture是空
#     floor = models.CharField(max_length=20, verbose_name="所在楼层")      # 座位所在楼层
#
#
# 楼层座位模型
class TotalSeat(models.Model):
    StudyRoom = models.CharField(max_length=100, verbose_name="自习室座位")
    Standard = models.CharField(max_length=100, verbose_name="标准座位")
    Leisure = models.CharField(max_length=100, verbose_name="休闲座位")


# 自习室座位
class StudyRoomSeat(models.Model):
    id = models.CharField(verbose_name="座位编号", max_length=1000, primary_key=True)  # 座位唯一编号
    status = models.IntegerField(default=0)                             # 座位状态，0是空，1表示已预约
    floor = models.CharField(max_length=5, verbose_name="所在楼层")      # 座位所在楼层
    power = models.IntegerField(default=1, verbose_name="拥有电源")      # 座位电源状态，1表示靠近电源，0表示不靠近电源
    stairs = models.IntegerField(default=1, verbose_name="靠近楼梯")     # 座位靠近楼梯，1表示靠近，0表示不靠近

    class Mate:
        db_name = "StudyRoom"


# 标准区座位
class StandardSeat(models.Model):
    id = models.CharField(verbose_name="座位编号", max_length=1000, primary_key=True)
    status = models.IntegerField(default=0)
    floor = models.CharField(max_length=5, verbose_name="所在楼层")
    power = models.IntegerField(default=1, verbose_name="拥有电源")
    stairs = models.IntegerField(default=1, verbose_name="靠近楼梯")

    class Mate:
        db_name = "Standard"


# 休闲区座位
class LeisureSeat(models.Model):
    id = models.CharField(verbose_name="座位编号", max_length=1000, primary_key=True)
    status = models.IntegerField(default=0)
    floor = models.CharField(max_length=5, verbose_name="所在楼层")
    power = models.IntegerField(default=1, verbose_name="拥有电源")
    stairs = models.IntegerField(default=1, verbose_name="靠近楼梯")

    class Mate:
        db_name = "Leisure"


