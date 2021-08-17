from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'dota/index.html')


def categories(request, catid):
    return HttpResponse(f"<h1>Герої по категоріям</h1><p>{catid}</p>")