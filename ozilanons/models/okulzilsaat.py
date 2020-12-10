from django.db import models


# Create your models here.

class DersZamanlama(models.Model):
    gun_id = models.PositiveSmallIntegerField(verbose_name='id', primary_key=True)

    ilk1 = models.TextField(default='')
    ogr1 = models.TextField(default='')
    cik1 = models.TextField(default='')

    ilk2 = models.TextField(default='')
    ogr2 = models.TextField(default='')
    cik2 = models.TextField(default='')

    ilk3 = models.TextField(default='')
    ogr3 = models.TextField(default='')
    cik3 = models.TextField(default='')

    ilk4 = models.TextField(default='')
    ogr4 = models.TextField(default='')
    cik4 = models.TextField(default='')

    ilk5 = models.TextField(default='')
    ogr5 = models.TextField(default='')
    cik5 = models.TextField(default='')

    ilk6 = models.TextField(default='')
    ogr6 = models.TextField(default='')
    cik6 = models.TextField(default='')

    ilk7 = models.TextField(default='')
    ogr7 = models.TextField(default='')
    cik7 = models.TextField(default='')

    ilk8 = models.TextField(default='')
    ogr8 = models.TextField(default='')
    cik8 = models.TextField(default='')

    ilk9 = models.TextField(default='')
    ogr9 = models.TextField(default='')
    cik9 = models.TextField(default='')

    ilk10 = models.TextField(default='')
    ogr10 = models.TextField(default='')
    cik10 = models.TextField(default='')

    ilk11 = models.TextField(default='')
    ogr11 = models.TextField(default='')
    cik11 = models.TextField(default='')

    ilk12 = models.TextField(default='')
    ogr12 = models.TextField(default='')
    cik12 = models.TextField(default='')

    ilk13 = models.TextField(default='')
    ogr13 = models.TextField(default='')
    cik13 = models.TextField(default='')

    ilk14 = models.TextField(default='')
    ogr14 = models.TextField(default='')
    cik14 = models.TextField(default='')

    ilk15 = models.TextField(default='')
    ogr15 = models.TextField(default='')
    cik15 = models.TextField(default='')

    ilk16 = models.TextField(default='')
    ogr16 = models.TextField(default='')
    cik16 = models.TextField(default='')

    ilk17 = models.TextField(default='')
    ogr17 = models.TextField(default='')
    cik17 = models.TextField(default='')

    ilk18 = models.TextField(default='')
    ogr18 = models.TextField(default='')
    cik18 = models.TextField(default='')

    ilk19 = models.TextField(default='')
    ogr19 = models.TextField(default='')
    cik19 = models.TextField(default='')

    ilk20 = models.TextField(default='')
    ogr20 = models.TextField(default='')
    cik20 = models.TextField(default='')

    def __str__(self):
        return self.gun_id

    class Meta:

        db_table = 'saat'
