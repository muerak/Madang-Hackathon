from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'SaleList'

urlpatterns = [
    path('whole/', views.whole, name='whole'),
    path('whole_product/', views.product_list, name='product_list'),  # 상품 상세 페이지
    path('whole_product/<str:category>/', views.category_filter, name='category_filter'),
    path('logo_click/', views.logo_click, name='logo_click'),# 카테고리별 필터링 페이지
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)