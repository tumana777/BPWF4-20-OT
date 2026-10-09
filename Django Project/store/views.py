from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse

from store.models import Product
from store.forms import ProductForm, ProductUpdateForm


# def index(request):
#     return HttpResponse("<h1>Hello, Django!</h1>")

# def about(request):
#     return HttpResponse("<h1>About Page</h1>")

def products_json(request):
    products = Product.objects.all()
    return JsonResponse(list(products.values()), safe=False)

def index(request):
    # print(request.user)
    # print(request.method)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product_list(request):
    all_products = Product.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'product_list.html', context={'products': all_products})

def product_detail(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk, is_available=True)

    return render(request, 'product_detail.html', context={'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        # print(request.POST)

        if form.is_valid():
            form.save()

            return redirect('store:product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', context={'form': form})

def update_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = ProductUpdateForm(request.POST, instance=product)

        if form.is_valid():
            form.save()

            return redirect('store:product_detail', product_pk=product.pk)
    else:
        form = ProductUpdateForm(instance=product)

    return render(request, 'update_product.html', context={'form': form, 'product': product})

def delete_product(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        product.delete()

    return redirect('store:product_list')



















