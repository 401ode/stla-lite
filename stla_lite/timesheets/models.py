from django.db import models
from stla_lite.users.models import User, Employee, Supervisor
from stla_lite.grants.models import GrantAward, GrantAwardTask
from django.utils.encoding import python_2_unicode_compatible
from stla_lite.payperiods.models import PayPeriod, Holiday

@python_2_unicode_compatible
class Timesheet(models.Model):
    """
    The model that collates activity information.
    """
    UNSUBMITTED='unsubmitted' # Draft form.
    SUBMITTED='submitted' # Submitted to Supervisor
    REJECTED_SUP='rejected_sup' # Rejected by Supervisor
    APPROVED_SUP='approved' # Approved by Supervisor
    REJECTED_HR='rejected_hr'# Rejected by HR
    PROCESSED_HR='processed_hr' # Processed by HR
    PAID='paid' # Paid.
    TIMESHEET_STATUSES=(
        (UNSUBMITTED, 'Not Yet Submitted')
        , (SUBMITTED, 'Submitted to Supervisor')
        , (REJECTED_SUP, 'Rejected by Supervisor - Awaiting Revision')
        , (APPROVED_SUP, 'Approved by Supervisor - Awaiting HR Review')
        , (REJECTED_HR, 'Rejected by HR - Awaiting Revision')
        , (PROCESSED_HR, 'Processed by HR')
        , (PAID, 'Paid')
        )
    
    status=models.CharField(
        ("Timesheet Status")
        , choices=TIMESHEET_STATUSES
        , default=UNSUBMITTED
        , max_length=30
        )
    
    employee=models.ForeignKey(Employee
        , on_delete=models.CASCADE
        )
    
    # TODO: Need to work out this key relationship.
    # current_owner=models.ForeignKey(
    #     Employee
    #     )
    
    pay_period=models.ForeignKey(
        PayPeriod
    )
    
    created_date=models.DateField(
        auto_now_add=True
        )
    
    last_modified_date=models.DateField(
        auto_now=True
        )
    
    def submit(self):
        """
        There will be a form button to submit. 
        That button should transfer ownership to the supervisor for approval.
        """
        pass
    
    def approve(self):
        """
        If a supervisor, approve and pass to hr.
        If HR, approve and pass for payroll/GL.
        """
        pass
    def reject(self, User):
        """
        If a supervisor, reject and pass back to employee.
        If HR, reject and pass back to employee.
        """
        pass

@python_2_unicode_compatible
class Activity(models.Model):
    """
    The actual hour breakdown of a timesheet, including its category, how much time was spent on a thing.
    Need to get actual payroll codes to plug in here.
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
    
    timesheet=models.ForeignKey(Timesheet
        , on_delete=models.CASCADE
        )
    
    activity_date=models.DateField()
    
    hours=models.DecimalField(
        verbose_name='Hours spent on this activity'
        , max_digits=3
        , decimal_places=1
        )
    
    activity_category=models.CharField(
        verbose_name= 'Activity Category'
        , choices=CATEGORIES
        , default=REGULAR
        , max_length=30
        )
    
    grant_award_id=models.ForeignKey(
        GrantAward
        , on_delete=models.CASCADE
        , verbose_name='Grant Award for this activity.'
        )
    
    grant_award_task_id=models.ForeignKey(GrantAwardTask
        , on_delete=models.CASCADE
        )
    
    created_date=models.DateField(
        auto_now_add=True
        )
    
    last_modified_date=models.DateField(
        auto_now=True
        )
