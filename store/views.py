from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def products_all(request):
    products = Product.products.all()
    return render(request, 'store/product/all.html', {'products': products})


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'store/product/product_detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.products.filter(category=category)
    return render(request, 'store/category/products_all.html', {'products': products, 'category': category})
