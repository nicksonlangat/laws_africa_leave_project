from django.db import models

from core.utils import get_workdays, validate_dates

# Create your models here.
class Staff(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
         verbose_name_plural = "Company Staff"
    

class Leave(models.Model):
    LEAVE_TYPE_CHOICES = (
        ('Normal leave', 'Normal leave'),
        ('Sick leave', 'Sick leave'),
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='company_staff')
    start_date = models.DateField()
    end_date = models.DateField()
    leave_type = models.CharField(max_length=250, choices = LEAVE_TYPE_CHOICES)
    number_of_leave_days = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        start_date = self.start_date
        end_date = self.end_date
        validate_dates(start_date, end_date)
        self.number_of_leave_days=get_workdays(start_date, end_date)
        super(Leave, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'Leave request for {self.staff.first_name} {self.staff.last_name} from {self.start_date} to {self.end_date}'
    
    class Meta:
         verbose_name_plural = "Leave Requests"
