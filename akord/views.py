from django.shortcuts import render
from akord.models import *


def main(request):
    zdjecia = Zdjecie.objects.all()
    profiloweD = ProfiloweD.objects.first()
    profiloweL = ProfiloweL.objects.first()
    video = Wideo.objects.all()
    piosenki = Piosenka.objects.all()
    kat_piosenki = KategoriaPiosenki.objects.all()
    for v in video:
        v.url = '<button type="button" class="bmd-modalButton btn btn-info btn-lg" data-toggle="modal" data-bmdSrc="{0}" data-bmdWidth="500" data-bmdHeight="281" data-target="#myModal">{1}</button>'.format(v.url,v.tytul)
    return render(request, 'akord/main.html',{'zdjecia':zdjecia, "profiloweD":profiloweD, "profiloweL":profiloweL, 'videos':video, 'piosenki':piosenki, 'kat_piosenki':kat_piosenki})

