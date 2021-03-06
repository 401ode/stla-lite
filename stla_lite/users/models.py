from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):
    """
    Generic user class, inheriting from AbstractUser
    
    Used heavily in admin section. 
    """
    	
    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

@python_2_unicode_compatible
class Employee(User):
    """
    An Employee is a sub-class of user. Even if said employee never logs into this system, they'll still have a user representation here.
    """
    job_title = models.CharField(
        verbose_name='Job Title'
        , unique=False
        , blank=False
        , max_length=255
        )
    employee_id_number = models.IntegerField(
        verbose_name='Employee ID Number'
        , unique=True
        )
    
    # supervisor_id=models.ForeignKey(
    #     'Employee'
    #     , verbose_name='Supervisor'
    #     , null=True
    #     , on_delete=models.CASCADE
    #     , limit_choices_to={'is_supervisor': True}
    #     )

    is_supervisor=models.BooleanField(
        default=False
        )

    is_hr_staff=models.BooleanField(
        default=False
        )
    
    emergency_contact_name=models.CharField(
        verbose_name='Emergency Contact Name'
        , unique=False
        , blank=False
        , max_length=100
        )

    emergency_contact_phone=models.CharField(
        verbose_name='Emergency Contact Number'
        , unique=False
        , blank=False
        , max_length=15 # Should be more scientific
                        # (i.e. 3-area code, 3-exchange,
                        # 4-zone), but 20 is fine for now.
        )
    physical_working_location=models.CharField(
        # Used to check for people during emergency situations.
        verbose_name='Normal Physical Working Location'
        , unique=False
        , blank=False
        , max_length=100
        )
    
    # Job Classification Designations
    COMPETITIVE = 'CC'
    NON_COMPETITIVE = 'NC'
    UN_CLASSIFIED = 'US'
    NON_CLASSIFIED = 'NS'
    
    JOB_CLASSIFICATIONS = (
        (COMPETITIVE, 'Competitive Classified'),
        (NON_COMPETITIVE, 'Non-Competitive Classified'),
        (UN_CLASSIFIED, 'Unclassified Service'),
        (NON_CLASSIFIED, 'Non-Classified Service')
        )
    job_classification = models.CharField(
        max_length=2
        , default=NON_CLASSIFIED
        )
    eligible_for_overtime=models.BooleanField(
        default=False
        )
        
    # Need to think about where to keep track of lookback data.
    class Meta:
        verbose_name='Employee'
        verbose_name_plural='Employees'