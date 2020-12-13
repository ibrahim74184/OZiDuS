import os, sys

proj_path = "User/Samsung/Desktop/PythonProjeler/OZiDuS"
# This is so Django knows where to find stuff.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ozilanons.settings")
sys.path.append(proj_path)

# This is so my local_settings.py gets loaded.
os.chdir(proj_path)

# This is so models get loaded.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from ozildata.models import ZilData


def uret():
    gziller = ZilData.objects.all.filter(active=True)
    for i in range(len(gziller)):
        for x, y in gziller[i].items():
            print(f"{x}, {y}")

uret()