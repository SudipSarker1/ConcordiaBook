# textbooks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.textbook_list, name='textbook_list'),  # /textbooks/
]
