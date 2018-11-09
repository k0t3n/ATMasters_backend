from django.conf.urls import url

from src.apps.swagger.views import schema_view

urlpatterns = [
    url(r'^$', schema_view)
]
