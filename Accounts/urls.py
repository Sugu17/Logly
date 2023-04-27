from django.urls import path
from .views import *

app_name='Accounts'
urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login_user"),
    # path("logout_user/", logout_user, name="logout_user"),
]