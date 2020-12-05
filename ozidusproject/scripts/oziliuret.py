from django.db import models
from ozildata.models import ZilData


def uret():
    gziller = ZilData.objects.all.filter(active=True)
    for i in range(len(gziller)):
        for x, y in gziller[i].items():
            print(f"{x}, {y}")
