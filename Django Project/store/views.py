from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy

from store.models import Product
from store.forms import ProductForm, ProductUpdateForm

from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


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
    all_products = Product.objects.filter(is_available=True).select_related('category').order_by('-created_at')
    return render(request, 'product_list.html', context={'products': all_products, 'count': all_products.count()})

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


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    queryset = Product.objects.filter(is_available=True).select_related('category').order_by('-created_at')
    # ordering = ['-created_at']
    context_object_name = 'products'

    # def get_queryset(self):
    #     return Product.objects.filter(is_available=True).select_related('category').order_by('-created_at')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['count'] = self.queryset.count()

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'product_pk'
    queryset = Product.objects.filter(is_available=True)

    # def get_object(self, queryset = None):
    #     return get_object_or_404(Product, pk=self.kwargs['product_pk'], is_available=True)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('store:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = ProductUpdateForm
    pk_url_kwarg = 'product_pk'
    queryset = Product.objects.filter(is_available=True)

    def get_success_url(self):
        return reverse_lazy('store:product_detail', kwargs={'product_pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'product_pk'
    queryset = Product.objects.filter(is_available=True)
    success_url = reverse_lazy('store:product_list')





