from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kanban'),
    path('kanban/<int:kanban_id>', views.kanban_detail, name='detail'),
]
