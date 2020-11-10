from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/kanban/<int:kanban_id>', consumers.KanbanConsumer.as_asgi()),
]

