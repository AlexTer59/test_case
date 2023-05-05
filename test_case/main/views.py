from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def about(request):
    return HttpResponse("<h4>Страница о нас</h4>")


def location(request):
    return HttpResponse("<h4>Мы тут</h4>")