from Attendance.models import Attendance,Date
from django.utils.timezone import datetime
import csv

def get_date_record():
    date=datetime.now()
    today,created=Date.objects.get_or_create(date=date.strftime('%Y-%m-%d'))
    return today

def initialize():
    date=get_date_record()
    with open('Attendance/management/student_details.csv',mode='r') as file:
        heading=next(file)
        reader=csv.reader(file)
        for student in reader:
            Attendance.objects.create(name=student[0],reg_no=student[1],log_date=date)
    