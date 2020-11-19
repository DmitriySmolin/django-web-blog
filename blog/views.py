from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h2>Привет мир!</h2>')


def contacts(request):
    return HttpResponse('<h2>Страница с контактами</h2>')
