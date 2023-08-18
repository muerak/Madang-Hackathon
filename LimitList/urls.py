from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'LimitList'

urlpatterns = [
    path('limit/', views.limit_product_list, name='limit_product_list'),
    path('reserve/<int:product_id>/', views.reserve_product, name='reserve_product'),
    path('logo_click/', views.logo_click, name='logo_click'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)