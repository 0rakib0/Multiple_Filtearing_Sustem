from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from ecommerce import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.product_category_page, name='product_category_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)