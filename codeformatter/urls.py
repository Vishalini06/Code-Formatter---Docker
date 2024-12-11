# codeformatter/urls.py
from django.contrib import admin
from django.urls import path, include
from formatter import views  # Import views from the formatter app

urlpatterns = [
    path('admin/', admin.site.urls),   # Admin route
    path('', views.home, name='home'),  # Map the root URL to the 'home' view
    path('api/', include('formatter.urls')),  # API routes
]
