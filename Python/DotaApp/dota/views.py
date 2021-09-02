from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world")


def categories(request):
    return HttpResponse("<h1>Hello world I am </h1>")