from django.urls import path
from ..discussion import consumers


websocket_urlpatterns = [
    path('ws/discussion/<int:discussion_id>/', consumers.ChatConsumer.as_asgi()),
]