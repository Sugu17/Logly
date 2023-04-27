from django.db import models
from django.utils import timezone
# choices=('Present','Absent')
# Create your models here.


class Date(models.Model):
    date_id=models.AutoField(primary_key=True)
    date = models.DateField(max_length=255,default=timezone.now)
    def __str__(self) -> str:
        return (self.date.strftime("%B %d %Y"))

class Attendance(models.Model):
    name = models.CharField(max_length=256,default='Victor')
    reg_no = models.IntegerField(default=100)
    period_1 = models.BooleanField(default=False)
    period_2 = models.BooleanField(default=False)
    period_3 = models.BooleanField(default=False)
    period_4 = models.BooleanField(default=False)
    period_5 = models.BooleanField(default=False)
    period_6 = models.BooleanField(default=False)
    period_7 = models.BooleanField(default=False)
    log_date= models.ForeignKey(Date,on_delete=models.CASCADE,related_name='attendances')
    def __str__(self):
        return f"{self.reg_no}-{self.log_date.date.strftime('%B %d %Y')}"



