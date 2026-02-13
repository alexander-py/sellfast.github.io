from django.urls import path
from .views import home, download_checklist

urlpatterns = [
    path("", home, name="home"),
    path("checklist/", download_checklist, name="download_checklist"),
]