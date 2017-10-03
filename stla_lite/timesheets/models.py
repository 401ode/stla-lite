from django.db import models
from stla_lite.users.models import Employee, Supervisor
from stla_lite.grants.models import GrantAward, GrantAwardTask
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Timesheet(models.Model):
    """
    The model that collates activity information.
    """
    employee=models.ForeignKey(Employee
        , on_delete=models.CASCADE
        )

@python_2_unicode_compatible
class Activity(models.Model):
    """
    The actual hour breakdown of a timesheet, including how much time was spent on a thing.
    """
    REGULAR='regular'
    VACATION='vacation'
    SICK='sick'
    PERSONAL='personal'
    BEREAVEMENT='bereavement'
    HOLIDAY='holiday'
    JURY_DUTY='jury_duty'
    WORKERS_COMP='workers_comp'
    UNION_DUTIES='union_duties'
    TRAINING_CONF_SEM='training_conf_sem'
    OTHER='other'
    CATEGORIES=(
        (REGULAR, 'Regular Time')
        , (VACATION, 'Vacation')
        , (SICK, 'Sick')
        , (PERSONAL, 'Personal')
        , (BEREAVEMENT, 'Bereavement')
        , (HOLIDAY, 'Holiday')
        , (JURY_DUTY, 'Jury Duty')
        , (WORKERS_COMP, 'Workers Compensation')
        , (UNION_DUTIES, 'Union Duties')
        , (TRAINING_CONF_SEM, 'Training, Conference, or Seminar')
        , (OTHER, 'Other')
        )
    activity_category=models.CharField(
        ('Activity Category')
        , choices=CATEGORIES
        , default=REGULAR
        )
    
    grant_award_id=models.ForeignKey(GrantAward
        , on_delete=models.CASCADE
        )
    grant_award_task_id=models.ForeignKey(GrantAwardTask
        , on_delete=models.CASCADE
        )
    