from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from models import ProductModel,Stock
from django.forms.widgets import Textarea,TextInput,NumberInput,Select

class ProductForm(forms.ModelForm):

	class Meta:
		model = ProductModel
		fields = ('product_code','product_name','product_description',
			'pdt_category','pdt_sub_category','price','tax','discount','pdt_image')
		
		widgets = {
		'product_name':TextInput(attrs={'class':'form-control','style':'width=80%' }),
		'product_code':TextInput(attrs={'class':'form-control','style':'width=80%'}),
		'product_description':Textarea(attrs={'class':'form-control','style':'width=80%'}),
		'pdt_category':Select(attrs={'class':'form-control','style':'width=80%', "id":"product_category_change"} ),
		'pdt_sub_category':Select(attrs={'class':'form-control','style':'width=80%', "id":"product_subcategory_change"} ),
		'price':NumberInput(attrs={'class':'form-control','style':'width=80%'}),
		'tax':NumberInput(attrs={'class':'form-control','style':'width=80%'}),
		'discount':NumberInput(attrs={'class':'form-control','style':'width=80%'}),
		# 'pdt_image':ImageThumbnailFileInput(attrs={'class':'form-control','style':'width=80%'}),
		}


class ProductStockForm(forms.ModelForm):

	class Meta:
		model = Stock
		fields = ('stock_name','size','stock',)
