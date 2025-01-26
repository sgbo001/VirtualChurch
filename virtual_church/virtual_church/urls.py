from django.contrib import admin
from django.urls import path, include
from home.views import index
from django.conf import settings  # Import settings module
from django.conf.urls.static import static  # Import static helper function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', index, name='index'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
