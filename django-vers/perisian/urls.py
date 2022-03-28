from django.urls import path
from perisian import views

urlpatterns = [
    path('', views.perisian, name='Perisian'),
]