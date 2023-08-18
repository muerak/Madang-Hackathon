from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reservation'

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('logo_click/', views.logo_click, name='logo_click'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
