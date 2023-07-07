from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('register-user/', login_required(RegisterUserView.as_view()), name='Register User'),
    path('users-list/', login_required(UsersListView.as_view()), name='Users List'),
    path('register-position/', login_required(RegisterPositionView.as_view()), name='Register Position'),
    path('positions-list/', login_required(PositionsListView.as_view()), name='Positions List'),
]