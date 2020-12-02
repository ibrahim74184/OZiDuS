from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    evenNumberList = [item for item in range(2, 11, 2)]
    return render(request, 'home/index.html', {'evenNumberList': evenNumberList})


def detail(request):
    return HttpResponse("Detail sayfasına bakıyorsunuz")