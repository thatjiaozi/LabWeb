from django.urls import include, path
from django.contrib import admin

urlpatterns = [
            path('local_system/', include('local_system.urls')),
            path('cloud_system/', include('cloud_system.urls')),
            path('admin/', admin.site.urls),
                ]
