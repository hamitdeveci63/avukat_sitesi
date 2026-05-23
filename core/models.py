from django.db import models

class Hizmet(models.Model):
    baslik = models.CharField(max_length=200)
    aciklama = models.TextField()

    def __str__(self):
        return self.baslik

class Iletisim(models.Model):
    telefon = models.CharField(max_length=20, default="0")
    adres = models.TextField()

    def __str__(self):
        return "İletişim Bilgileri"

class Hakkimizda(models.Model):
    metin = models.TextField()

    def __str__(self):
        return "Hakkımızda Metni"