from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse

from store.models import Product


# def index(request):
#     return HttpResponse("<h1>Hello, Django!</h1>")

# def about(request):
#     return HttpResponse("<h1>About Page</h1>")

def products_json(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product_list(request):
    all_products = Product.objects.filter(is_available=True)
    return render(request, 'product_list.html', context={'products': all_products})

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk, is_available=True)

    return render(request, 'product_detail.html', context={'product': product})