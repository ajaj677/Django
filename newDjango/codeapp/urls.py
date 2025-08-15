from threading import local
from django.urls import path
from . import views

# localhost:8000/code_arena
urlpatterns = [
    path('', views.code_arena, name='code_arena'),
]