from django.shortcuts import render, redirect, get_object_or_404


def home_views(request):
    return render(request, 'home/index.html')

