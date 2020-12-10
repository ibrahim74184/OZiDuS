from django import forms
from .models import Duyurular


class DuyuruDataForm(forms.ModelForm):
    class Meta:
        model = Duyurular
        fields = '__all__'
        exclude = ('duyurutarihi', 'id')
