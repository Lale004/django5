from django.shortcuts import render
from .models import Product
from django.db.models import F, FloatField, ExpressionWrapper
def home(request):
    return render(request,'home.html',{})

def product_list(request):
    products = Product.objects.annotate(
        total_price=ExpressionWrapper(F('price') - F('discount_price'), output_field=FloatField())
    )
    context = {'products': products}
    return render (request,'products.html',context)


def product(request,id):
    product = Product.objects.get(id=id)
    if product.discount_price is not None:
        product.total_price = product.price - product.discount_price
    else:
        product.total_price =product.price
    context={'product':product}
    return render (request,'product.html',context)

def product_create(request):
    return render(request,'product_create.html',{})

