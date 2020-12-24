from django import forms
from ozilanons.models import ZilData, OkulAksamZaman


class ZilDataForm(forms.ModelForm):
    class Meta:
        model = ZilData
        fields = '__all__'
        exclude = ('published_date', 'id')


class AksamZilDataForm(forms.ModelForm):
    class Meta:
        model = OkulAksamZaman
        fields = '__all__'
        exclude = ('published_date', 'id')
