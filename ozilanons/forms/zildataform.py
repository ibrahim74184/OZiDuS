from django import forms

from ozilanons.models import ZilData
from django.utils.translation import gettext as _


class ZilDataForm(forms.ModelForm):

    class Meta:
        model = ZilData
        fields = '__all__'
        exclude = ('published_date', 'id', 'zilgun')
        dersbaslangicsaati = forms.TimeField()