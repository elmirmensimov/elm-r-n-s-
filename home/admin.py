from django.contrib import admin
from .models import Product
from .models import Order

admin.site.register(Order)

admin.site.register(Product)
