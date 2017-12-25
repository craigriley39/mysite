from django.urls import path
from . import views



app_name = 'order'
urlpatterns = [
    path('customer', views.customer_list, name='customer_list'),
    path('order', views.order_list, name='order_list'),
    path('product', views.product_list, name='product_list'),
]