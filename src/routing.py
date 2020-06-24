# chat/routing.py
from django.urls import re_path

from src.websocket import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer),

]
