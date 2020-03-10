from django.contrib import admin

# Register your models here.
from leave.models import LeaveRequest

admin.site.register(LeaveRequest)
