from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('reservations', views.user_reservation, name='reservations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)