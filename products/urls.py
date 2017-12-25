from django.urls import path
from . import views


app_name = 'products'
urlpatterns = [


    path('add/', views.add, name='shopping-cart-add'),
    path('remove/', views.remove, name='shopping-cart-remove'),
    path(r'show/', views.show, name='shopping-cart-show'),
    ]
