# textbooks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 1) /textbooks/ – no course code, shows all textbooks
    path('', views.textbook_list, name='textbook_list'),

    # 2) /textbooks/<course_code>/ – filtered by course code
    path('<str:course_code>/', views.textbook_list, name='textbook_list_with_code'),
]
