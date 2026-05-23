from django.shortcuts import render
from .models import Hizmet, Iletisim, Hakkimizda

def anasayfa(request):
    hizmetler = Hizmet.objects.all()
    iletisim = Iletisim.objects.first()
    hakkimizda = Hakkimizda.objects.first()
    
    return render(request, 'index.html', {
        'hizmetler': hizmetler, 
        'iletisim': iletisim, 
        'hakkimizda': hakkimizda
    })