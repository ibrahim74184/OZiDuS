from django import forms
from ozilanons.models import DuyuruData


class DuyuruDataForm(forms.ModelForm):
    class Meta:
        model = DuyuruData
        metin = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))
        fields = ('metin',)
        exclude = ('duyurutarihi', 'id')

