from django.shortcuts import render, redirect, get_object_or_404

from ozilanons.models import ZilData, OkulAksamZaman, DersZamanlama
from ozilanons.tables import ZilayarTable, AksamZilayarTable
from ozilanons.forms import ZilDataForm, AksamZilDataForm
from datetime import datetime
from django_tables2 import SingleTableView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from scripts.oziliuret import ZilUret
# Create your views here.


def index(request):
    return render(request, 'ayarlar/index.html')


def anonsduyuru(request):
    return render(request, 'ayarlar/anonsduyuru.html')


def cikis(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('login')


def zilayarmenu(request):
    #print(Zuret.uret())
    return render(request, 'ayarlar/zilayarmenu.html')


def login_zil(request):
    messages.success(request, 'Giriş Yapıldı')
    return render(request, 'registration/login.html')


class ZilDataListView(SingleTableView):
    model = ZilData
    table_class = ZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'
    #context_table_name = 'table'
    tables = [ZilData.objects.all(), ]
    DersZamanlama.objects.all().delete()
    data = ZilUret(ZilData, DersZamanlama)
    data.uret()

    table_pagination = {
        "per_page": 10
    }


class AksamZilDataListView(SingleTableView):
    model = OkulAksamZaman
    table_class = AksamZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'


def post_zildata_new(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            try:
                post.save()
            except IntegrityError:
                Print("Aynı değer gitirildi")
            finally:
                return redirect('zilayarmenu')
    else:
        form = ZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def post_aksamzildata_new(request):
    if request.method == "POST":
        form = AksamZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            try:
                post.save()
            except IntegrityError:
                Print("Aynı değer gitirildi")
            finally:
                return redirect('index')
    else:
        form = AksamZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def icerikSil(request, id):
    icerik = get_object_or_404(IcerikModel, id=id)
    icerik.delete()
    messages.success(request, 'İçerik silindi')
    return redirect("icerik:index")


def guncelle(request, id):
    icerik = get_object_or_404(ZilData, id=id)
    form = ZilDataForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik = form.save(commit=False)
        icerik.user = request.user
        icerik.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('ozildata')
    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})

