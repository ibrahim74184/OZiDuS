from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import KayitForm, GirisForm
from django.contrib import messages


# Create your views here.

def kayit(request):
    if request.method == "POST":
        form = KayitForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            yeniKayit = User(username=username)
            yeniKayit.set_password(password)
            yeniKayit.save()

            login(request, yeniKayit)
            return redirect("anonsduyuru")
        context = {
            "form": form
        }
        return render(request, "home/kayit.html", context)
    else:
        form = KayitForm()
        context = {
            "form": form
        }
        return render(request, "home/kayit.html", context)


def giris(request):
    form = GirisForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "Kullanıcı adı veya parola hatalı")
            return render(request, "home/giris.html", context)
        messages.success(request, "Hoşgeldin: " + username)
        login(request, user)
        return redirect('anonsduyuru')
    return render(request, "home/giris.html", context)


def cikis(request):
    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect("home:giris")


def kontrolpanel(request):
    return render(request, "home/kontrolpanel.html")
