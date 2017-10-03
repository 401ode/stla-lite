from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime

@python_2_unicode_compatible
class PayPeriod(models.Model):
    """
    The pay period in which an activity takes place. 
    As of right now, manually established.
    """
    start_date=models.DateField()
    end_date=models.DateField()
    
    def __str__(self):
        return "{} - {}".format(
            self.start_date
            , self.end_date
            )
            
class Holiday(models.Model):
    """
    A way of defining a date which should default to a holiday.
    """
    holiday_date=models.DateField()
    holiday_name=models.CharField(
        verbose_name='Holiday Name'
        , max_length=40)
        
    def __str__(self):
        return "{} - {}".format(self.holiday_name, self.holiday_date)