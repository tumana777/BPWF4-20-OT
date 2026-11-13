from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView,
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)

from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from store.models import Product, Category
from rest_framework.response import Response
from api.serializers import (
    CategoryListSerializer, ProductSerializer,
    ProductListSerializer, ProductCreateSerializer,
    ProductUpdateSerializer
)
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
    queryset = Product.objects.select_related('category')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = 'product_pk'

class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer
    permission_classes = [IsAuthenticated]

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.select_related('category')
    serializer_class = ProductUpdateSerializer
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'product_pk'

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.select_related('category')
    permission_classes = [IsAuthenticated]
    lookup_url_kwarg = 'product_pk'


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').filter(is_available=True).order_by('-created_at')
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProductCreateSerializer
        return ProductListSerializer

class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.select_related('category')
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_url_kwarg = 'product_pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProductSerializer
        return ProductUpdateSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related('category').order_by('-created_at')
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        elif self.action == 'retrieve':
            return ProductSerializer
        elif self.action == 'create':
            return ProductCreateSerializer
        return ProductUpdateSerializer

    # @action(detail=True, methods=['post'])
    # def make_available_true(self, request, pk=None):
    #     product = self.get_object()
    #     product.is_available = True
    #     product.save()
    #     return Response({'message': 'Product is now available'})
    #
    # @action(detail=True, methods=['post'])
    # def make_available_false(self, request, pk=None):
    #     product = self.get_object()
    #     product.is_available = False
    #     product.save()
    #     return Response({'message': 'Product is now not available'})

    @action(detail=True, methods=['post'])
    def change_available(self, request, pk=None):
        product = self.get_object()
        product.is_available = not product.is_available
        product.save()
        return Response(
            {
                'message': f'Product availability changed to {product.is_available}',
                'status': status.HTTP_200_OK
            }
        )

