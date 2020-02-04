from django.shortcuts import redirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        return redirect('/events')
    else:
        return redirect('login')
