from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'test': 'HEJ PÅ DIG'}
    return render(request, 'shop/index.html', context)
