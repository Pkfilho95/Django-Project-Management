from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import RegisterUserForm, RegisterPositionForm
from .models import UserProfile, Position

class RegisterUserView(View):
    template_name = 'register_user.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': RegisterUserForm})

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST or None)

        if form.is_valid():
            user = User.objects.create_user(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )

            UserProfile.objects.create(
                user = user,
                name = f'{user.first_name} {user.last_name}'.capitalize(),
                position = form.cleaned_data['position']
            )

            messages.success(request, 'User created successfully!')
            return HttpResponseRedirect('/users/users-list/')

        return render(request, self.template_name, {'form': form})

class UsersListView(ListView):
    model = UserProfile
    template_name = 'users_list.html'
    context_object_name = 'users'

class RegisterPositionView(FormView):
    template_name = 'register_position.html'
    form_class = RegisterPositionForm
    success_url = '/users/positions-list/'

    def form_valid(self, form):
        Position.objects.create(
            position = form.cleaned_data['position']
        )
        return super().form_valid(form)

class PositionsListView(ListView):
    model = Position
    template_name = 'positions_list.html'
    context_object_name = 'positions'