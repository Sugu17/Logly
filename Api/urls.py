from django.urls import path,include
from .views import *

app_name='Api'

urlpatterns = [
    path('',update,name='update'),
]