from django.shortcuts import render
from akord.models import *
from django.views.generic import ListView, TemplateView



class ListaPiosenek(ListView):
    model = Piosenka

def lista_video(request):
    video = Wideo.objects.all()
    return render(request, 'akord/video.html',{'videos':video})

def lista_zdjec(request):
    zdjecia = Zdjecie.objects.all()
    profiloweD = ProfiloweD.objects.first()
    profiloweL = ProfiloweL.objects.first()
    video = Wideo.objects.all()
    return render(request, 'akord/main.html',{'zdjecia':zdjecia, "profiloweD":profiloweD, "profiloweL":profiloweL, 'videos':video})

