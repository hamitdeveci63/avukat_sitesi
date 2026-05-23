from django.contrib import admin
from django.urls import path
from core.views import anasayfa  # core klasöründen anasayfayı çağırıyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', anasayfa),  # Ana adres '' (boş) olduğu için burası ana sayfa olur
]