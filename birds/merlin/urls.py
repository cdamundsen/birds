from django.urls import path
from . import views

app_name='merlin'

urlpatterns = [
    path('', views.birds_list, name='birds_list'),
    path('locations/', views.locations, name='locations'),
    path('orders/', views.orders, name='orders'),
    path('<slug:bird_slug>/', views.bird, name='bird'),
]