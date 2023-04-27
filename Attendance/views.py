from django.shortcuts import render,get_list_or_404
from .models import Date
# Create your views here.

def index(request):
    context={'date_list':get_list_or_404(Date)}
    return render(request,'Attendance/index.html',context=context)

def detail(request,date_id):
    date=Date.objects.get(pk=date_id)
    attendance_objects=date.attendances.all()
    data_list=[]
    for attendance in attendance_objects:
        data={}
        list=[attendance.period_1,
              attendance.period_2,
              attendance.period_3,
              attendance.period_4,
              attendance.period_5,
              attendance.period_6,
              attendance.period_7
            ]
        data['Name']=attendance.name
        data['Register Number']=attendance.reg_no
        data['Period 1']='Present' if attendance.period_1 else 'Absent'
        data['Period 2']='Present' if attendance.period_2 else 'Absent'
        data['Period 3']='Present' if attendance.period_3 else 'Absent'
        data['Period 4']='Present' if attendance.period_4 else 'Absent'
        data['Period 5']='Present' if attendance.period_5 else 'Absent'
        data['Period 6']='Present' if attendance.period_6 else 'Absent'
        data['Period 7']='Present' if attendance.period_7 else 'Absent'
        data['Status']=True if sum(list)>4 else False
        data_list.append(data)
    return render(request,'Attendance/detail.html',context={'data_list':data_list})
