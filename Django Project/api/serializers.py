from rest_framework import serializers

from store.models import Category, Product


# class CategoryListSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     saxeli = serializers.CharField(source='name')
#     total_products = serializers.IntegerField()

# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
#     quantity = serializers.IntegerField()
#     is_available = serializers.BooleanField()
#     description = serializers.CharField(allow_blank=True, allow_null=True)
#     created_at = serializers.DateTimeField()
#     updated_at = serializers.DateTimeField()
#     image = serializers.ImageField(allow_null=True)
#     category_id = serializers.IntegerField(source='category.id', allow_null=True)

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer(read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        exclude = ('is_available', )

    def get_total_price(self, obj):
        return obj.price * obj.quantity

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('is_available', )

























