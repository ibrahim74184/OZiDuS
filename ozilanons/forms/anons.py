from django import forms
from ozilanons.models import DuyuruData


class DuyuruDataForm(forms.ModelForm):
    class Meta:
        model = DuyuruData
        fields = '__all__'
        exclude = ('duyurutarihi', 'id')
