from django.urls import path

from .consumers import WSConsumer
ws_urlpatterns = [
    path('ws/notifiation/',  WSConsumer.as_asgi()),
]