from django.conf.urls import url
from akord.views import *

urlpatterns = [
    url(r'^main/', main),
]

