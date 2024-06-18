from django import forms 
from django.forms import ModelForm
from .models import Product


class ProductForms(ModelForm):
    class Meta:
        model = Product
        fields =('name', 'color', 'price', 'qty', 'tax', 'total')
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'color':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'qty':forms.TextInput(attrs={'class':'form-control'}),
            'tax':forms.TextInput(attrs={'class':'form-control'}),
            'total':forms.TextInput(attrs={'class':'form-control'}),
        }
        labels={
            'name':'Enter your product name',
            'color':'Enter color',
            'price':'Enter price',
            'qty':'Enter quantity',
            'tax':'Enter tax',
            'total':'Enter total',
        }

    