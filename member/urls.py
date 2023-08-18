from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'member'

urlpatterns = [
    path('', views.login, name='login'),
    path('main/<str:phone_last_four>/', views.main, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)