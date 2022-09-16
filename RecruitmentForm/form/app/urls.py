from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('data/', views.database, name='database'),
]
