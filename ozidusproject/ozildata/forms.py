from django import forms

from .models import ZilData


class ZilDataForm(forms.ModelForm):
    class Meta:
        model = ZilData
        fields = '__all__'
        exclude = ('published_date', 'id',)