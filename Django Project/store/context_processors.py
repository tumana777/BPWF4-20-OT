from store.models import Product

def products(request):
    return {
        'site_name': 'My Store',
        'product_list': Product.objects.all()
    }