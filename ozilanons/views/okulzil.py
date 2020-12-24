from django.shortcuts import render, redirect, get_object_or_404

from ozilanons.models import ZilData, OkulAksamZaman, DersZamanlama, DuyuruData
from ozilanons.tables import ZilayarTable, AksamZilayarTable
from ozilanons.forms import ZilDataForm, AksamZilDataForm, DuyuruDataForm
from datetime import datetime
from django_tables2 import SingleTableView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from scripts.oziliUret import ZilUret

# Create your views here.
bayrak = True


def index(request):
    return render(request, 'ayarlar/index.html')


def anonsduyuru(request):
    """if request.method == "POST":
        form = DuyuruDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            post.save()
            return redirect('zilayarmenu')
    else:
        form = DuyuruDataForm()"""
    return render(request, 'ayarlar/anonsduyuru.html')


def cikis(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('login')


def zilayarmenu(request):
    # print(Zuret.uret())
    return render(request, 'ayarlar/zilayarmenu.html')


def login_zil(request):
    messages.success(request, 'Giriş Yapıldı')
    return render(request, 'registration/login.html')


def ZilListView(request):
    global bayrak
    if bayrak:
        DersZamanlama.objects.all().delete()
        data = ZilUret(ZilData, DersZamanlama)
        data.uret()
        bayrak = False
    ziltanimi = ZilData.objects.all()
    context = {'ziltanimi': ziltanimi}
    return render(request, 'ayarlar/new_ayarlar_detail.html', context)


def ZilListViewAksam(request):
    ziltanimi = OkulAksamZaman.objects.all()
    context = {'ziltanimi': ziltanimi}
    return render(request, 'ayarlar/new_ayarlar_detail.html', context)


class ZilDataListView(SingleTableView, ZilUret):
    model = ZilData
    table_class = ZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'
    # context_table_name = 'table'
    # tables = [ZilData.objects.all(), ]
    table_pagination = {
        "per_page": 10
    }


class AksamZilDataListView(SingleTableView):
    model = OkulAksamZaman
    table_class = AksamZilayarTable
    template_name = 'ayarlar/ayarlar_detail.html'


def new_post_zildata(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            post.save()
            return redirect('zilayarmenu')
    else:
        form = ZilDataForm()
    return render(request, 'ayarlar/new_ayarlar.html', {'form': form})


def post_zildata_new(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = datetime.today()
            post.save()
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
            post.save()
            return redirect('zilayarmenu')
    else:
        form = AksamZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def zilikapat(request):
    icerik = get_object_or_404(DuyuruData, id=1)
    form = ZilDurumForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik = form.save(commit=False)
        # icerik.zilaktif = 1
        icerik.user = request.user
        icerik.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('duyurumetin')
    return render(request, 'ayarlar/anonsduyuru.html', {'form': form})


def duyurumetin(request):
    metin = get_object_or_404(DuyuruData, id=1)
    form = DuyuruDataForm(request.POST or None, request.FILES or None, instance=metin)
    if form.is_valid():
        metin = form.save(commit=False)
        metin.guncellendi = 1
        metin.user = request.user
        metin.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('duyurumetin')

    return render(request, 'ayarlar/anonsduyuru.html', {'form': form})


def icerikSil(request, id):
    icerik = get_object_or_404(ZilData, id=id)
    form = ZilDataForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik.delete()
        messages.success(request, 'İçerik silindi')
        return redirect("zillistview")
    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def guncelle(request, id):
    icerik = get_object_or_404(ZilData, id=id)
    form = ZilDataForm(request.POST or None, request.FILES or None, instance=icerik)
    if form.is_valid():
        icerik = form.save(commit=False)
        icerik.user = request.user
        icerik.save()
        messages.success(request, 'İçerik Güncellendi')
        return redirect('zillistview')
    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})
