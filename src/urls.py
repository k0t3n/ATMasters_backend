from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/swagger', include('src.apps.swagger.urls')),
    path('api/', include('src.apps.withdrawal_point.urls')),
]
