from django.contrib import admin
from .models import PayPeriod, Holiday

@admin.register(PayPeriod, Holiday)
class PayPeriodAdmin(admin.ModelAdmin):
    pass