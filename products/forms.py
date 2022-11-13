from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('name', 'price',)
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.FloatField(min_value=0),
        }
    