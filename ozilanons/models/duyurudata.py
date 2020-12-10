from django.db import models


# Create your models here.

class Duyurular(models.Model):
    zilaktif = models.SmallIntegerField(verbose_name='Aktif',default=1)
    metin = models.TextField(verbose_name='Metin')
    mp3yolu = models.TextField(verbose_name='Path')
    guncellendi = models.SmallIntegerField(verbose_name='Güncel', default=0)

    def __str__(self):
        return self.metin

    class Meta:

        db_table = 'cal_duyur'
