from django.db import models


# Create your models here.

class DersZamanlama(models.Model):
    gun_id = models.PositiveSmallIntegerField(verbose_name='id', primary_key=True, auto_created=False)

    ilk1 = models.TextField(null=True)
    ogr1 = models.TextField(null=True)
    cik1 = models.TextField(null=True)

    ilk2 = models.TextField(null=True)
    ogr2 = models.TextField(null=True)
    cik2 = models.TextField(null=True)

    ilk3 = models.TextField(null=True)
    ogr3 = models.TextField(null=True)
    cik3 = models.TextField(null=True)

    ilk4 = models.TextField(null=True)
    ogr4 = models.TextField(null=True)
    cik4 = models.TextField(null=True)

    ilk5 = models.TextField(null=True)
    ogr5 = models.TextField(null=True)
    cik5 = models.TextField(null=True)

    ilk6 = models.TextField(null=True)
    ogr6 = models.TextField(null=True)
    cik6 = models.TextField(null=True)

    ilk7 = models.TextField(null=True)
    ogr7 = models.TextField(null=True)
    cik7 = models.TextField(null=True)

    ilk8 = models.TextField(null=True)
    ogr8 = models.TextField(null=True)
    cik8 = models.TextField(null=True)

    ilk9 = models.TextField(null=True)
    ogr9 = models.TextField(null=True)
    cik9 = models.TextField(null=True)

    ilk10 = models.TextField(null=True)
    ogr10 = models.TextField(null=True)
    cik10 = models.TextField(null=True)

    ilk11 = models.TextField(null=True)
    ogr11 = models.TextField(null=True)
    cik11 = models.TextField(null=True)

    ilk12 = models.TextField(null=True)
    ogr12 = models.TextField(null=True)
    cik12 = models.TextField(null=True)

    ilk13 = models.TextField(null=True)
    ogr13 = models.TextField(null=True)
    cik13 = models.TextField(null=True)

    ilk14 = models.TextField(null=True)
    ogr14 = models.TextField(null=True)
    cik14 = models.TextField(null=True)

    ilk15 = models.TextField(null=True)
    ogr15 = models.TextField(null=True)
    cik15 = models.TextField(null=True)

    ilk16 = models.TextField(null=True)
    ogr16 = models.TextField(null=True)
    cik16 = models.TextField(null=True)

    ilk17 = models.TextField(null=True)
    ogr17 = models.TextField(null=True)
    cik17 = models.TextField(null=True)

    ilk18 = models.TextField(null=True)
    ogr18 = models.TextField(null=True)
    cik18 = models.TextField(null=True)

    ilk19 = models.TextField(null=True)
    ogr19 = models.TextField(null=True)
    cik19 = models.TextField(null=True)

    ilk20 = models.TextField(null=True)
    ogr20 = models.TextField(null=True)
    cik20 = models.TextField(null=True)

    def __str__(self):
        return self.gun_id

    class Meta:
        db_table = 'saat'
