from django.db import models


# Create your models here.

class DersZamanlama(models.Model):
    gun_id = models.PositiveSmallIntegerField(verbose_name='id', primary_key=True, auto_created=False)

    ilk1 = models.TextField(default=None)
    ogr1 = models.TextField(default=None)
    cik1 = models.TextField(default=None)

    ilk2 = models.TextField(default=None)
    ogr2 = models.TextField(default=None)
    cik2 = models.TextField(default=None)

    ilk3 = models.TextField(default=None)
    ogr3 = models.TextField(default=None)
    cik3 = models.TextField(default=None)

    ilk4 = models.TextField(default=None)
    ogr4 = models.TextField(default=None)
    cik4 = models.TextField(default=None)

    ilk5 = models.TextField(default=None)
    ogr5 = models.TextField(default=None)
    cik5 = models.TextField(default=None)

    ilk6 = models.TextField(default=None)
    ogr6 = models.TextField(default=None)
    cik6 = models.TextField(default=None)

    ilk7 = models.TextField(default=None)
    ogr7 = models.TextField(default=None)
    cik7 = models.TextField(default=None)

    ilk8 = models.TextField(default=None)
    ogr8 = models.TextField(default=None)
    cik8 = models.TextField(default=None)

    ilk9 = models.TextField(default=None)
    ogr9 = models.TextField(default=None)
    cik9 = models.TextField(default=None)

    ilk10 = models.TextField(default=None)
    ogr10 = models.TextField(default=None)
    cik10 = models.TextField(default=None)

    ilk11 = models.TextField(default=None)
    ogr11 = models.TextField(default=None)
    cik11 = models.TextField(default=None)

    ilk12 = models.TextField(default=None)
    ogr12 = models.TextField(default=None)
    cik12 = models.TextField(default=None)

    ilk13 = models.TextField(default=None)
    ogr13 = models.TextField(default=None)
    cik13 = models.TextField(default=None)

    ilk14 = models.TextField(default=None)
    ogr14 = models.TextField(default=None)
    cik14 = models.TextField(default=None)

    ilk15 = models.TextField(default=None)
    ogr15 = models.TextField(default=None)
    cik15 = models.TextField(default=None)

    ilk16 = models.TextField(default=None)
    ogr16 = models.TextField(default=None)
    cik16 = models.TextField(default=None)

    ilk17 = models.TextField(default=None)
    ogr17 = models.TextField(default=None)
    cik17 = models.TextField(default=None)

    ilk18 = models.TextField(default=None)
    ogr18 = models.TextField(default=None)
    cik18 = models.TextField(default=None)

    ilk19 = models.TextField(default=None)
    ogr19 = models.TextField(default=None)
    cik19 = models.TextField(default=None)

    ilk20 = models.TextField(default=None)
    ogr20 = models.TextField(default=None)
    cik20 = models.TextField(default=None)

    def __str__(self):
        return self.gun_id

    class Meta:
        db_table = 'saat'
