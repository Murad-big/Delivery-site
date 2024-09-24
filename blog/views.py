from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'blog/home.html')


def about(request):

    return render(request, 'blog/О-нас.html')