from __future__ import unicode_literals

from django.shortcuts import render,render_to_response, get_object_or_404,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Customer ,Order, Product #,Shipment,Contact,Address,ShipmentItem


# Create your views here.


def customer_list(request):

    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})



def order_list(request):
    orders = Order.objects.all()

    return render(request,'order_list.html', {'orders' : orders})



def product_list(request):
    products = Product.objects.all()

    return render(request,'product_list.html', {'products' : products})