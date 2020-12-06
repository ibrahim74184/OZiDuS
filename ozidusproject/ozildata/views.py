from django.shortcuts import render, redirect, get_object_or_404
from .models import ZilData
from .tables import ZilayarTable
from .forms import ZilDataForm
from datetime import datetime
from django_tables2 import SingleTableView


# Create your views here.

def index(request):
    return render(request, 'ozildata/index.html')


class ZilDataListView(SingleTableView):
    model = ZilData
    table_class = ZilayarTable
    template_name = 'ozildata/zilayardata.html'


def post_detail(request, pk):
    table_class = ZilayarTable
    table = get_object_or_404(table_class, pk=pk)
    return render(request, 'zilayarlari', {'table': table})


def post_new(request):
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
                Print("Aynı değer gitildi")
            finally:
                return redirect('zilayarlari', )
    else:
        form = ZilDataForm()
    return render(request, 'ozildata/post_edit.html', {'form': form})
