from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return render(request, 'home.html', {'key': 'value'})
    return HttpResponse('home')


def profile(request):
    return render(request, 'dashboard/profile.html', {'key': 'value'})
    # return HttpResponse('profile')