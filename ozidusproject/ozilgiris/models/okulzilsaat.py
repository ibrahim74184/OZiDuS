from django.db import models


# Create your models here.

class DersZamanlama(models.Model):
    gun_id = models.PositiveSmallIntegerField(verbose_name='id', primary_key=True)

    ilk1 = models.TextField()
    ogr1 = models.TextField()
    cik1 = models.TextField()

    ilk2 = models.TextField()
    ogr2 = models.TextField()
    cik2 = models.TextField()

    ilk3 = models.TextField()
    ogr3 = models.TextField()
    cik3 = models.TextField()

    ilk4 = models.TextField()
    ogr4 = models.TextField()
    cik4 = models.TextField()

    ilk5 = models.TextField()
    ogr5 = models.TextField()
    cik5 = models.TextField()

    ilk6 = models.TextField()
    ogr6 = models.TextField()
    cik6 = models.TextField()

    ilk7 = models.TextField()
    ogr7 = models.TextField()
    cik7 = models.TextField()

    ilk8 = models.TextField()
    ogr8 = models.TextField()
    cik8 = models.TextField()

    ilk9 = models.TextField()
    ogr9 = models.TextField()
    cik9 = models.TextField()

    ilk10 = models.TextField()
    ogr10 = models.TextField()
    cik10 = models.TextField()

    ilk11 = models.TextField()
    ogr11 = models.TextField()
    cik11 = models.TextField()

    ilk12 = models.TextField()
    ogr12 = models.TextField()
    cik12 = models.TextField()

    ilk13 = models.TextField()
    ogr13 = models.TextField()
    cik13 = models.TextField()

    ilk14 = models.TextField()
    ogr14 = models.TextField()
    cik14 = models.TextField()

    ilk15 = models.TextField()
    ogr15 = models.TextField()
    cik15 = models.TextField()

    ilk16 = models.TextField()
    ogr16 = models.TextField()
    cik16 = models.TextField()

    ilk17 = models.TextField()
    ogr17 = models.TextField()
    cik17 = models.TextField()

    ilk18 = models.TextField()
    ogr18 = models.TextField()
    cik18 = models.TextField()

    ilk19 = models.TextField()
    ogr19 = models.TextField()
    cik19 = models.TextField()

    ilk20 = models.TextField()
    ogr20 = models.TextField()
    cik20 = models.TextField()

    def __str__(self):
        return self.gun_id

    class Meta:
        managed = True
        db_table = 'saat'
