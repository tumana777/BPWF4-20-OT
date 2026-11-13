from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CategoryListAPIView, ProductListAPIView,
    ProductRetrieveAPIView, ProductCreateAPIView,
    ProductUpdateAPIView, ProductDeleteAPIView,
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView,
    ProductViewSet
)

router = routers.DefaultRouter()

router.register('products', ProductViewSet)

app_name = 'api'

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    # path('products/', ProductListAPIView.as_view(), name='product_list'),
    # path('products/<int:product_pk>/', ProductRetrieveAPIView.as_view(), name='product_detail'),
    # path('products/create/', ProductCreateAPIView.as_view(), name='product_create'),
    # path('products/<int:product_pk>/update/', ProductUpdateAPIView.as_view(), name='product_update'),
    # path('products/<int:product_pk>/delete/', ProductDeleteAPIView.as_view(), name='product_delete'),
    # path('products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    # path('products/<int:product_pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]