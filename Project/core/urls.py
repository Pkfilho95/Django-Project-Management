from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('redirect/', login_required(RedirectView.as_view()), name="Redirect"),
    path('index/', login_required(IndexView.as_view()), name="Index"),
]