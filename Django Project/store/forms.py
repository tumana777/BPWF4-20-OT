from django import forms
from store.models import Product

# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(max_digits=10, decimal_places=2)
#     quantity = forms.IntegerField()
#     is_available = forms.BooleanField(required=False)
#     description = forms.CharField(widget=forms.Textarea)
#     category = forms.CharField(max_length=100)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['is_available']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'