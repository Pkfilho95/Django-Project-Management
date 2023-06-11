from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

class RedirectView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/core/index/')

class IndexView(TemplateView):
    template_name = 'index.html'