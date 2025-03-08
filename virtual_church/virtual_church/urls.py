from django.contrib import admin
from django.urls import path, include
from home.views import index, about, live_event, resources
from django.conf import settings  # Import settings module
from django.conf.urls.static import static  # Import static helper function
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', index, name='index'),
    path('about', views.about, name = 'about'),
    path('live_event/', views.live_event, name = 'live_event'),
    path('resources/', views.resources, name = 'resources'),
]

# Serve static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
