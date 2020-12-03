from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import ZilData
from .forms import ZilDataForm
from datetime import datetime


# Create your views here.

def GunZiliOlustur():
    zil2 = ZilData.objects.all()
    for gun in range(len(zil2)):
        print(zil2[gun].zilgun)


def index(request):
    zil1 = ZilData.objects.all()
    GunZiliOlustur()
    evenNumberList = [item for item in zil1]
    return render(request, 'ozildata/index.html', {'evenNumberList': evenNumberList})


"""
def detail(request):
    return HttpResponse("Dijatal Pano sayfasına bakıyorsunuz")

"""


def post_detail(request, pk):
    post = get_object_or_404(ZilData, pk=pk)
    return render(request, 'ozildata/index.html', {'post': post})


# post_detail.html


def post_new(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ZilDataForm()

    return render(request, 'ozildata/post_edit.html', {'form': form})
