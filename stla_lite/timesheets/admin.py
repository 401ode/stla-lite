from django.contrib import admin
from .models import Timesheet, Activity

@admin.register(Timesheet, Activity)
class TimesheetAdmin(admin.ModelAdmin):
    pass