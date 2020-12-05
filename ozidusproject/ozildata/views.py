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
    post = get_object_or_404(ZilData, pk=pk)
    return render(request, 'ozildata/zilayardata.html', {'table': post})


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
