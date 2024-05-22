from django.shortcuts import render, get_object_or_404
from .models import Order
from products.models import Product

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def home_view(request):
    products = Product.objects.all()
    return render(request,'home/index.html', {'products': products})

def index(request):
    return render(request, 'index.html')


