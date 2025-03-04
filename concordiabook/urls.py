"""
URL configuration for concordiabook project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('textbooks/', include('textbooks.urls')),
]
