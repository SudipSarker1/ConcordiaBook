from django.urls import path
from . import views

urlpatterns = [
    path('<str:course_code>/', views.textbook_list, name='textbook_list'),
        # path('', views.textbook_list, name='textbook_list'),
]
