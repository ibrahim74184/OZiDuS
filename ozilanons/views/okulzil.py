from django.shortcuts import render, redirect, get_object_or_404

from ozilanons.models import ZilData, OkulAksamZaman
from ozilanons.tables import ZilayarTable, AksamZilayarTable
from ozilanons.forms import ZilDataForm, AksamZilDataForm
from datetime import datetime
from django_tables2 import SingleTableView


# Create your views here.

def index(request):
    return render(request, 'ayarlar/index.html')


def zilayarmenu(request):
    return render(request, 'ayarlar/zilayarmenu.html')


def login_zil(request):
    return render(request, 'registration/login.html')


class ZilDataListView(SingleTableView):
    model = ZilData
    table_class = ZilayarTable
    template_name = 'ayarlar/ayarlar.html'


class AksamZilDataListView(SingleTableView):
    model = OkulAksamZaman
    table_class = AksamZilayarTable
    template_name = 'ayarlar/ayarlar.html'


def post_zildata_new(request):
    if request.method == "POST":
        form = ZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.zilgun = post.xzilgun
            post.published_date = datetime.today()
            try:
                post.save()
            except IntegrityError:
                Print("Aynı değer gitirildi")
            finally:
                return redirect('index')
    else:
        form = ZilDataForm()

    return render(request, 'ayarlar/post_zildata_edit.html', {'form': form})


def post_aksamzildata_new(request):
    if request.method == "POST":
        form = AksamZilDataForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.zilgun = post.xzilgun
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


"""class OkulZamanDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "ayarlar/okulzaman_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=ZilData.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['okulzilzaman'] = self.object
        return context

    def get_queryset(self):
        return self.object.zildata_set.all()
"""
