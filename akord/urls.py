from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from akord.views import *

urlpatterns = [
    url(r'^repertuar/', ListaPiosenek.as_view()),
    url(r'^zdjecia/', lista_zdjec),
    url(r'^video/', lista_video),
]

