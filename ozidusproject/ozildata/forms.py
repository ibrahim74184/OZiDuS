from django import forms

from .models import ZilData


class ZilDataForm(forms.ModelForm):
    class Meta:
        model = ZilData
        fields = ('toplanmasuresi', 'ogretmenzilsuresi', 'derssayisi', 'derssuresi',
                  'tenefussuresi', 'oglenarasiders', 'zilgun', 'dersbaslangicsaati',
                  'oglenarasisuresi', 'active')
        exclude = ('published_date', 'id',)