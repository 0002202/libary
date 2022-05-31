from django.contrib import admin
from .models import StandardSeat, StudyRoomSeat, LeisureSeat

admin.site.register(StandardSeat)
admin.site.register(StudyRoomSeat)
admin.site.register(LeisureSeat)