from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import logout, login


urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)