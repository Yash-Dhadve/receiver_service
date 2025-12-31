from django.urls import path
from .views import receive_ping

urlpatterns = [
    path("api/receive/", receive_ping),
]
