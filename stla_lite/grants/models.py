from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class GrantAward(models.Model):
    """
    The class for holding information regarding Federal or other grants to which 
    time can be allotted.
    
    For RI-specific purposes, these will be created dynamically based on data in the
    GrantGrantTaskExport GovGrants GMS object.
    
    These objects should not be maintained manually in this system, but modified using
    the standard GMS process.
    """
    grant_award_id=models.CharField(
        verbose_name='Grant Award ID'
	    , primary_key=True
	    , max_length=40
	)
    grant_award_description=models.CharField(
        verbose_name='Grant Award Description'
    	, unique=False
    	, blank=True
    	, max_length=100
    	)
    grant_award_start_date=models.DateField(
        null=False
    	)
    grant_award_end_date=models.DateField(
        null=False
    	)

    	
@python_2_unicode_compatible
class GrantAwardTask(models.Model):
    """
    The class for holding information regarding Federal or other Grant Award Tasks to which 
    time can be allotted.
    
    For RI-specific purposes, these will be created dynamically based on data in the
    GrantGrantTaskExport GovGrants GMS object.
    
    These objects should not be maintained manually in this system, but modified using
    the standard GMS process.
    """
    grant_award_task_id=models.CharField(
        verbose_name='Grant Award Task ID'
    	, primary_key=True
    	, max_length=40
    	)
    grant_award_id=models.ForeignKey(
        GrantAward
        , on_delete=models.CASCADE
        )
    grant_award_task_description=models.CharField(
        verbose_name='Grant Award Task Description'
    	, unique=False
    	, blank=True
    	, max_length=100
    	)
    grant_award_task_start_date=models.DateField(
        null=False
    	)
    grant_award_task_end_date=models.DateField(
        null=False
    	)