from django.db import models


# Create your models here.

class ZilData(models.Model):
    dersbaslangicsaati = models.TimeField(verbose_name='Derslerin Başlangıç Saati', default='09:00:00', auto_now=False)
    toplanmasuresi = models.SmallIntegerField(verbose_name='Toplanma Süresi', default=600)
    ogretmenzilsuresi = models.SmallIntegerField(verbose_name='Öğretmen Ders Bildirim Zili', default=180)
    derssayisi = models.SmallIntegerField(verbose_name='Günlük Ders Sayısı', default=10)
    derssuresi = models.SmallIntegerField(verbose_name='Ders Süresi', default=1800)
    tenefussuresi = models.SmallIntegerField(verbose_name='Tenefüs Süresi', default=600)
    oglenarasiders = models.SmallIntegerField(verbose_name='Öğlen Arası', default=6)
    oglenarasisuresi = models.SmallIntegerField(verbose_name='Öğlen Arası Süresi', default=2700)
    zilgun = models.SlugField(verbose_name='Tanımlanan Gün', unique=True)
    active = models.BooleanField(verbose_name='Aktif Pasif', default=False)

    def __str__(self):
        return self.zilgun

    class Meta:
        managed  = True
        db_table = 'zildefault'
