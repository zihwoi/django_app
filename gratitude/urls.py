# gratitude/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gratitude-home'),  # Example route
]
