# formatter/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('format/', views.format_code, name='format_code'),  # API route for formatting code
]
