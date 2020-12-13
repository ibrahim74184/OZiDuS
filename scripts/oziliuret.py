import os, sys

proj_path = "/Users/Samsung/Desktop/PythonProjeler/OZiDuS"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ozidusproject.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from ozilanons.models import ZilData


class Zuret:
    def uret():
        gziller = ZilData.objects.all()
        gunler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
        for x in gziller:
            sd = gunler[int(x.zilgun)]
            print(sd)
