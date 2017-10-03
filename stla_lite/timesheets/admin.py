from django.contrib import admin
from .models import Timesheet, Activity

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    pass