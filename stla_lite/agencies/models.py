from django.db import models



class Agency(models.Model):
    """
    High-level Agency model. Now only with two fields.
    """
    agency_name=models.CharField(
        verbose_name='Agency Name'
        , max_length=100
        )
        
    agency_acronym=models.CharField(
        verbose_name='Agency Acronym'
        , max_length=10
        )
        
    agency_code=models.IntegerField(
        verbose_name='Agency Code' # RIFANS code.
        , max_length=3
        , primary_key=True
        )
    
    def __str__(self):
        return self.agency_name
    

class CostCenter(models.Model):
    """
    Cost Center within an agency.
    """
    agency=models.ForeignKey(
        Agency
        , on_delete=models.CASCADE
        )
    cost_center_name=models.CharField(
        verbose_name='Cost Center Name'
        , max_length=40
        )
    cost_center_code=models.IntegerField(
        verbose_name='Cost Center Code' # RIFANS
        )
    
    def __str__(self):
        return "{} - {}".format(
            self.agency_name
            , self.cost_center_name
            )