from django.shortcuts import redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Attendance.models import Attendance, Date
import json
# Create your views here.
@csrf_exempt
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        date_object = Date.objects.get(date=data['Date'])
        record = Attendance.objects.get(
            reg_no=data['Roll Number'], log_date=date_object.date_id)
        match int(data['Period ID']):
            case 1:
                record.period_1 = True
            case 2:
                record.period_2 = True
            case 3:
                record.period_3 = True
            case 4:
                record.period_4 = True
            case 5:
                record.period_5 = True
            case 6:
                record.period_6 = True
            case 7:
                record.period_7 = True
            case _:
                return HttpResponse("Invalid period id!")
        record.save()
        redirect(f'reverse(Attendance:detail)/{date_object.date_id}')
        return HttpResponse("Data recieved")
    else:
        return HttpResponse("API site")
