from .models import *
from django.contrib import admin
from embed_video.admin import AdminVideoMixin


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Wideo, MyModelAdmin)
admin.site.register(Zdjecie)
admin.site.register(Piosenka)
admin.site.register(KategoriaPiosenki)
admin.site.register(ProfiloweD)
admin.site.register(ProfiloweL)
