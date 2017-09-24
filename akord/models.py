from django.db import models

class Zdjecie(models.Model):
    obraz = models.ImageField(upload_to = 'zdjecia/', null=False)

class Wideo(models.Model):
    url = models.CharField(max_length=1000,null=False, blank=False)

class Piosenka(models.Model):
    tytul = models.CharField(max_length=200)
    kategoria = models.ForeignKey('KategoriaPiosenki', on_delete=models.CASCADE, null=True)

class KategoriaPiosenki(models.Model):
    nazwa_ketegori = models.CharField(max_length=200)

class ProfiloweD(models.Model):
    obraz = models.ImageField(upload_to='zdjecia/')

class ProfiloweL(models.Model):
    obraz = models.ImageField(upload_to='zdjecia/', null=False)