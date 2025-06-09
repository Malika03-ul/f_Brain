from django.urls import path
from .views import convert_ip

urlpatterns = [
    path('convert/', convert_ip, name='convert_ip'),
]