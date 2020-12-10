from django.shortcuts import render, redirect, get_object_or_404

from ozilanons.models import ZilData
from ozilanons.tables import ZilayarTable
from ozilanons.forms import ZilDataForm

from datetime import datetime
from django_tables2 import SingleTableView


# Create your views here.

def index(request):
    return render(request, 'index.html')


class ZilDataListView(SingleTableView):
    model = ZilData
    table_class = ZilayarTable
    template_name = 'ayarlar/ayarlar.html'


def post_zildata_detail(request, pk):
    table_class = ZilayarTable
    table = get_object_or_404(table_class, pk=pk)
    return render(request, 'ayarlar/ayarlar.html', {'table': table})


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
