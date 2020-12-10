from django import forms
from ozilanons.models import Duyurular


class DuyuruDataForm(forms.ModelForm):
    class Meta:
        model = Duyurular
        fields = '__all__'
        exclude = ('duyurutarihi', 'id')
