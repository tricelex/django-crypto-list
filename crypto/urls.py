from django.urls import path
from crypto import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('prices/', views.prices, name='prices'),
]
