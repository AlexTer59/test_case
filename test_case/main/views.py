from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def about(request):
    return render(request, 'main/about.html')


def location(request):
    return render(request, 'main/location.html')