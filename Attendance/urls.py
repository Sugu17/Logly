from django.urls import path,include
from .views import *

app_name='Attendance'

urlpatterns = [
    path('',index,name='index'),
    path('<int:date_id>/',detail,name='detail'),
]
