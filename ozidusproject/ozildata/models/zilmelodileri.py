from django.db import models


# Create your models here.

class ZilMelodi(models.Model):
    melodiad = models.TextField(verbose_name='Melodi Adı')
    yol = models.TextField(verbose_name='Path')

    def __str__(self):
        return self.melodiad

    class Meta:
        managed = True
        db_table = 'melodipath'
