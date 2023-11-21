# imagefilter/urls.py
from .views import filter_image
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('filter/', filter_image, name='filter_image'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)