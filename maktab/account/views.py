from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
# from django.views.generic.edit import CreateView
from django.views.generic import View
from .forms import LoginForm


class LoginPageView(View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return reverse_lazy('home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})