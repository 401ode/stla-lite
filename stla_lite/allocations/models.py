from django.db import models
from stla_lite.grants.models import GrantAwardTask
from django.core.exceptions import ValidationError

class Allocation(models.Model):
    """
    At a minimum, need a spot for: 
    - The associated grant.
    - The legacy account number?
    - The RISAIL Account Number?
    - Definitely the RIFANS account number.
    - The percentage of that task paid by the given Grant task.
    """
    grant_task=models.ForeignKey(
        GrantAwardTask
        , on_delete=models.CASCADE
        )
    rifans_account_number=models.CharField(
        verbose_name='RIFANS Account Number'
        , max_length=30
        )
    task_grant_percentage=models.DecimalField(
        verbose_name='Percentage of this task paid for by this grant task.'
        , max_digits=5
        , decimal_places=4
        )
    
    
    def clean(self):
        """
        1. Check if self.task_grant_percentage + fk grant_task.percent_allotted > 1.
            1.1 If > 1, raise ValidationError? 
            1.2 If < 1, grant_task.percentage_allotted = self.% + grant_grant_task.% 
        
        """
        if self.task_grant_percentage + self.grant_task.percent_allotted > 1.0:
            raise ValidationError(
                'Adding this allocation would over-allocate the associated grant task.'
                )