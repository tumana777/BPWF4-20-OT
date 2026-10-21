from django.urls import path
from store.views import (
    index, about, products_json, product_list, product_detail,
    add_product, update_product, delete_product, ProductListView,
    ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

app_name = 'store'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('products.json', products_json, name='products_json'),
    # path('products/', product_list, name='product_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    # path('products/<int:product_pk>/', product_detail, name='product_detail'),
    path('products/<int:product_pk>/', ProductDetailView.as_view(), name='product_detail'),
    # path('add-product/', add_product, name='add_product'),
    path('add-product/', ProductCreateView.as_view(), name='add_product'),
    path('update-product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete-product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),
]