import json
from django.http import response
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from store.models import Product
from .basket import Basket


def basket_summary(request):
    # basket = Basket(request)
    return render(request, 'store/basket/summary.html')

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        productqty = int(request.POST.get('productqty'))
        basket.add(product=product, productqty=productqty)
        basket_qty = basket.__len__()
        response = JsonResponse({'basket_qty': basket_qty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        basket.delete(product=product)
        basket_qty_updated = basket.__len__()
        basket_total_updated = basket.get_total_price()
        response = JsonResponse({'basket_qty_updated': basket_qty_updated, 'basket_total_updated': basket_total_updated})
        return response

def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == "post":
        product_id = int(request.POST.get('productid'))
        product = get_object_or_404(Product, id=product_id)
        productqty = int(request.POST.get('productqty'))
        basket.update(product=product, productqty=productqty)
        basket_qty_updated = basket.__len__()
        basket_total_updated = basket.get_total_price()
        response = JsonResponse({'basket_qty_updated': basket_qty_updated, 'basket_total_updated': basket_total_updated})
        return response