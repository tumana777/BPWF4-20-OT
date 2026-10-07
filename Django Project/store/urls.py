from django.urls import path
from store.views import index, about, products_json, product_list, product_detail

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products.json', products_json, name='products_json'),
    path('products/', product_list, name='product_list'),
    path('products/<int:product_pk>/', product_detail, name='product_detail'),
]