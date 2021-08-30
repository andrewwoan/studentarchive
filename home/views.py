from django.shortcuts import render, redirect
from .models import HomeText


def home(request):
    hometext = HomeText.objects.all()
    context = {'hometext': hometext}
    return render(request, 'home/homepage.html', context)
