from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from store.models import Product, Category
from rest_framework.response import Response
from api.serializers import CategoryListSerializer, ProductSerializer, ProductListSerializer, ProductCreateSerializer
from django.db.models import Count



# @api_view(['GET'])
# def product_list(request):
#     products = Product.objects.values()
#     return Response(products)

# @api_view(['GET'])
# def category_list(request):
#     categories = Category.objects.annotate(total_products=Count('products'))
#     serializer = CategoryListSerializer(categories, many=True)
#     return Response(serializer.data)
#
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def product_list(request):
#     products = Product.objects.select_related('category').filter(is_available=True).order_by('-created_at')
#     serializer = ProductListSerializer(products, many=True, context={'request': request})
#     return Response(serializer.data)

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.annotate(total_products=Count('products'))
    serializer_class = CategoryListSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.select_related('category').filter(is_available=True).order_by('-created_at')
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.select_related('category').filter(is_available=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = 'product_pk'

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]






















