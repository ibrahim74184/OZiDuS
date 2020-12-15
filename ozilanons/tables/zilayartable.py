import django_tables2 as tables
import django_tables2.utils as ztb
from ozilanons.models import ZilData, OkulAksamZaman


class ZilayarTable(tables.Table):

    class Meta:
        model = ZilData
        template_name = 'django_tables2/bootstrap.html'
        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'zilgun', 'active',)

        exclude = ('published_date', 'id', )
        order_by = 'zilgun'


class AksamZilayarTable(tables.Table):
    class Meta:
        model = OkulAksamZaman
        template_name = 'django_tables2/bootstrap.html'

        sequence = ('dersbaslangicsaati', 'toplanmasuresi',
                    'ogretmenzilsuresi', 'derssayisi', 'derssuresi', 'tenefussuresi',
                    'oglenarasiders', 'oglenarasisuresi', 'zilgun', 'active',)

        exclude = ('published_date', 'id',)
        order_by = 'zilgun'
