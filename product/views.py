# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView,FormView,View
from django.shortcuts import render,render_to_response,redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json
import random

from models import SubCategories,ProductModel,Stock,Size
from forms import ProductForm,ProductStockForm
from customer.models import MessageModal
# Create your views here.


class CreateProduct(View):
	template_name = "createproduct.html"
	form_class = ProductForm

	def get(self,request):
		form = self.form_class()
		# pro_code = random()
		context = {
			'f3': form,
		}
		return render(request, self.template_name, context)

	def post(self,request):
		form = self.form_class(self.request.POST,self.request.FILES)
		self.objects = form
		product_name = self.request.POST["product_name"]
		product_code = codegeneration(product_name)

		if form.is_valid():
			form.save()
			context = {
				'form':form,
				'success':"saved successfully"
			}
			print("succes")
			user = ProductModel.objects.get(product_name=product_name)
			user.product_code = product_code
			user.save()
			return redirect("/product/stock/")

		else:
			context = {
				'form':form
			}
			print("error")
			return render(request,self.template_name,context)


def codegeneration(product_name):
	rand = random.randint(1000,10100)
	rand = str(rand)
	code = "kingini_"+ product_name + rand
	print(code)
	return code


class SubCategoryView(View):

	def post(self,request):
		cat_obj = request.POST.get('pdt_category')
		response = {}
		userobj = SubCategories.objects.filter(category=cat_obj)
		for obj in userobj:
			sub_category_objects = obj.sub_category_title
			response[sub_category_objects]=sub_category_objects

		# subcat = [x for x in sub_catego
		
		# print(response)


		return HttpResponse(json.dumps(response),content_type='json')


class ProductStockView(View):
	template_name = "stock.html"
	form_class = ProductStockForm

	def get(self,request):
		form = self.form_class()
		# pro_code = random()
		context = {
			'f4': form,
		}
		return render(request, self.template_name, context)

	def post(self,request):
		form = self.form_class(self.request.POST)
		if form.is_valid():
			form.save()
			context = {
				'form':form,
				'success':"saved successfully"
			}
			return redirect("/product/stock/")
		else:
			context = {
				'form':form
			}
			print("error")
			return render(request,self.template_name,context)


class ProductStockListView(View):
	template_name = "list.html"

	def get(self,request):
		dict1={}
		dict3={}
		usr=ProductModel.objects.all()
		for product in usr:
			dict2 = {}
			dict2.clear()
			dict2 = {'0':0,'16':0,'18':0,'20':0,'22':0,'24':0,'26':0,'28':0,'30':0}
			username = product.product_name
			stocks_obj = Stock.objects.filter(stock_name=username)

			for x in stocks_obj:
				size = x.size.size
				stock = x.stock
				dict2[size]=stock
				print('dict2222222222222',dict2)
			print(dict2)
			dict1[username]=[product,dict2]
			del dict2
		print(dict1)
		
		return render(request,'list.html',{'test':dict1})

class UpdateView(View):
	template_name = 'update.html'

	def get(self,request,pdt_name):
		
		pro_obj=ProductModel.objects.get(product_name=pdt_name)


		stocks_obj = Stock.objects.filter(stock_name=pdt_name)
		
		
		context = {
			'pdt': pro_obj,
			'stk': stocks_obj,
		}
		return render(request,self.template_name,context)

	# def post(self,request):
	# 	stocks_obj = Stock.objects.filter(stock_name=pdt_name)
	# 	for x in stocks_obj:
	# 		print(x)

	# 		x.stock = 0

	# 	context = {}
	# 	return render(request,'update.html',context)

class EditView(View):
	 def post(self,request):
	 	print("postiing")
	 	name = request.POST.get('pdt_name')
	 	pdt_tax = request.POST.get('pdt_tax')
	 	pdt_price = request.POST.get('pdt_price')
	 	pdt_discount = request.POST.get('pdt_discount')

	 	details = request.POST.get('pdt_details')

	 	pro_obj = ProductModel.objects.get(product_name=name)
	 	pro_obj.tax = pdt_tax
	 	pro_obj.price = pdt_price
	 	pro_obj.discount = pdt_discount
	 	pro_obj.product_description = details

	 	pro_obj.save()



		response = "success"
	
		# return ProductStockListView.get()

		return HttpResponse(json.dumps(response),content_type='json')

class ClearView(ProductStockListView):
	def get(self,request,pdt_name):
		stocks_obj = Stock.objects.filter(stock_name=pdt_name)
		for x in stocks_obj:
			print(x)

			x.stock = 0
			x.save()

		context = {}
		return ProductStockListView.get(self,request)
		# return render(request,'admin_index.html',context)

		# return render(request,self.,context)

class InboxView(View):
	def get(self,request):
		mess_obj = MessageModal.objects.all()
		dict1 = {}
		dict1['test']= mess_obj

		return render(request,'message.html',dict1)
