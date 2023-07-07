from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='login.html'), name='Login'),
    path('logout/', login_required(LogoutView.as_view(next_page='/')), name='Logout'),
    path('core/', include(('core.urls','core'))),
    path('users/', include(('users.urls','users'))),
    path('clients/', include(('clients.urls','client'))),
]
