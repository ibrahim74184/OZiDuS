from django.db import models


# Create your models here.

class Duyurular(models.Model):
    duyurumetin = models.TextField(verbose_name='Metin')
    duyurutarihi = models.TimeField(verbose_name='Saati')
    duyurukayittarihi = models.DateTimeField(verbose_name='Kayıt Tarihi', auto_now_add=True)
    duyuruaktif = models.BooleanField(verbose_name='Aktif', default=False)
    duyuruperiyod = models.PositiveSmallIntegerField(verbose_name='Tekrar Sayısı')

    def __str__(self):
        return self.duyurumetin

    class Meta:
        managed = True
        db_table = 'duyurular'
