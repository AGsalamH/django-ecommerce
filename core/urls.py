
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', lambda req: render(req, 'base.html')),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
