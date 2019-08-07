# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json
import urllib
import urllib2
from django.shortcuts import render,render_to_response,redirect
from django.views.generic import TemplateView,FormView,View
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
import json
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.conf import settings

# Create your views here.

from django.contrib.auth.models import User
from form import UserForm,CustomerForm
from models import customer_registeration_model,MyWalletModal,MessageModal
from product.forms import ProductForm
from product.models import ProductModel,Stock,Categories

class HomeView(TemplateView):
	template_name = "index.html"
	def get(self,request):
		dict1={}
		usr=ProductModel.objects.all()

		dict1["test"]=usr
		return render(request,'index.html',dict1)

class MyOrderView(TemplateView):
	template_name = "myorder.html"
	def get(self,request):
		dict1 = {}
		user = request.user
		wallet_obj = MyWalletModal.objects.filter(username=user,status=True)
		# wallet_obj.product_name = regid
		dict1['test']=wallet_obj

		return render(request,'myorder.html',dict1)

class AdminHome(View):
	template_name = "admin_index.html"
	# form_class = ProductForm

	def get(self,request):
		# form = self.form_class()
		# pro_code = random()
		wallet_obj = MyWalletModal.objects.all()
		context = {
			'test': wallet_obj,
		}
		return render(request, self.template_name, context)

class RegisterationView(FormView):

	template_name = "signup.html"
	form_class = UserForm

	def get(self,request,*args,**kwargs):

		print("&&&11")

		form_class = self.get_form_class()
		form1 = self.get_form(form_class)
		form2 = CustomerForm()
		print("&&&22")

		return self.render_to_response(self.get_context_data(f1=form1,f2=form2))

	def post(self,request,*args,**kwargs):

		print("&&&")
		form_class = self.get_form_class()
		form1 = self.get_form(form_class)
		form2 = CustomerForm(self.request.POST)
		print(form1,form2)

		recaptcha_response = request.POST.get('g-recaptcha-response')
		print(recaptcha_response)
		# data = {
  #               'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
  #               'response': recaptcha_response
  #           }
		# r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
		# result = r.json()

		# if result['success']:

		# 	if(form1.is_valid() and form2.is_valid()):
		# 		return self.form_valid(form1,form2)
		# 	else:
		# 		return self.form_invalid(form1,form2)

		# else:
		# 	return self.form_invalid(form1,form2)

		if(form1.is_valid() and form2.is_valid()):
			return self.form_valid(form1,form2)
		else:
			return self.form_invalid(form1,form2)


	def form_valid(self,form1,form2):
		self.object = form1.save()
		self.object.staff = True 
		p = form2.save(commit=False)
		p.user = self.object
		p.save()

		return super(RegisterationView,self).form_valid(form2)

	def form_invalid(self,form1,form2):

		return self.render_to_response(self.get_context_data(f1=form1,f2=form2))

	def get_success_url(self,**kwargs):

		return reverse_lazy("customer_regiseraion")

class ChangePasswordView(View):

	def post(self,request):
		print("Hello_this")
		old = request.POST.get('old_password')
		new = request.POST.get('new_password')
		print(old, new)

		userobj = User.objects.get(username=request.user)
		
		if userobj.check_password(old):
			userobj.set_password(new)
			userobj.save()
			response="Success"

		else :
			print("Error")
			response="failed"

		return HttpResponse(json.dumps(response),content_type='json')

def login(request):
    form =AuthenticationForm()
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return redirect("/adminhome/")# or your url name
        if request.user.is_staff:
            return redirect("/home/")# or your url name


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect("/adminhome/")# or your url name
            if request.user.is_staff:
                return redirect("/home/")# or your url name

        else:
            messages.error(request, 'Error wrong username/password')
    context = {}
    context['form']=form

    return render(request, 'registration/login.html', context)


class MyProductView1(View):
	def get(self,request):
		dict1={}

		category = Categories.objects.filter(category_title="Bottomwear")
		for x in category:
			print(x)

		usr=ProductModel.objects.filter(pdt_category=x)
		dict1["test"]=usr
		print(dict1)
		return render(request,'product.html',dict1)

class MyProductView2(View):
	def get(self,request):
		dict1={}
		category = Categories.objects.filter(category_title="Topwear")
		for x in category:
			print(x)

		usr=ProductModel.objects.filter(pdt_category=x)
		dict1["test"]=usr
		return render(request,'product.html',dict1)

class MyProductView3(View):
	def get(self,request):
		dict1={}
		category = Categories.objects.filter(category_title="Frocks")
		for x in category:
			print(x)

		usr=ProductModel.objects.filter(pdt_category=x)
		dict1["test"]=usr
		return render(request,'product.html',dict1)

class MyProductView4(View):
	def get(self,request):
		dict1={}
		category = Categories.objects.filter(category_title="Kids Accessories")
		for x in category:
			print(x)

		usr=ProductModel.objects.filter(pdt_category=x)
		dict1["test"]=usr
		return render(request,'product.html',dict1)

class MyWalletVew(View):
	def get(self,request):
		dict1 = {}
		user = request.user
		wallet_obj = MyWalletModal.objects.filter(username=user,status=False)
		# wallet_obj.product_name = regid
		dict1['test']=wallet_obj

		return render(request,'mywallet.html',dict1)


class AddToCartView(View):
	def get(self,request,pdt_name):
		# pdt_name = request.POST.get('product_name')
		dict1={}
		print("pdt_name")
		user = request.user
		usr=ProductModel.objects.all()
		pdt_obj=ProductModel.objects.get(product_name=pdt_name)
		pdt_price = pdt_obj.price


		dict1["test"]=usr
		if MyWalletModal.objects.filter(username=user,product_name=pdt_name,status=False):
			wallet_obj = MyWalletModal.objects.get(username=user,product_name=pdt_name,status=False)
			wallet_obj.amount = wallet_obj.amount + 1
			wallet_obj.save()
			wallet_obj.price = pdt_price
			amount = wallet_obj.amount
			pdt_total = amount * pdt_price
			wallet_obj.total = pdt_total

			return render(request,'index.html',dict1)


		wallet_obj = MyWalletModal.objects.create(username=user)
		wallet_obj.product_name = pdt_name
		wallet_obj.amount = 1

		wallet_obj.price = pdt_price
		wallet_obj.total = pdt_price


		wallet_obj.save()
		response="success"

		usr=ProductModel.objects.all()

		dict1["test"]=usr
 

		return render(request,'index.html',dict1)


		# return HttpResponse(json.dumps(response),content_type='json')


class ItemView(View):
	print("hello")


	def get(self,request,regid):
		dict1={}
		print("hello")
		usr=ProductModel.objects.get(product_name=regid)
		stocks_obj = Stock.objects.filter(stock_name=regid)
	
		dict1["test"]=usr
		dict1["stocks"]=stocks_obj
		return render(request,'single.html',dict1)

class DeleteView(ItemView):
	def post(self,request,pdt_name):
		stocks_obj = Stock.objects.filter(stock_name=pdt_name)
		
		stocks_obj.save()

		return ItemView.get(self,request,pdt_name)



	

class BuyView(View):
	print("buy")
	def post(self,request):
		print("buy2")
		dict1={}
		quantity = request.POST.get('pdt_qantity')
		size_pdt = request.POST.get('pdt_size')
		name = request.POST.get('pdt_name')
		pwd = request.POST.get('pwd')
		print(type(size_pdt))
		print("buy3")
		
		# amount = requ3st.GET['amount_required']
		# size = request.GET['size']
		userobj2 = User.objects.get(username=request.user)

		userobj = customer_registeration_model.objects.get(user=request.user)
		user = request.user
		user_loc = userobj.loaction
		user_con1 = userobj.contact1
		user_con2 = userobj.contact2
		user_zip = userobj.zip_code

		if quantity==0:
			response="Enter a quantity"
			return HttpResponse(json.dumps(response),content_type='json')


		
		if userobj2.check_password(pwd):
			print("buy4")
			# if MyWalletModal.objects.filter(username=user,product_name=name,status=False):
			# 	wallet_obj = MyWalletModal.objects.filter(username=user,product_name=name,status=False)
			# else:
			# 	wallet_obj = MyWalletModal.objects.create(username=user)
			
			# wallet_obj = MyWalletModal.objects.filter(username=user,product_name=name,status=False)

			wallet_obj = MyWalletModal.objects.create(username=user)


			wallet_obj.user_location = user_loc
			wallet_obj.user_contact_no1 = user_con1
			wallet_obj.user_contact_no2 = user_con2
			wallet_obj.user_zip_code = user_zip

			pdt_obj=ProductModel.objects.get(product_name=name)
			pdt_price = pdt_obj.price
			pdt_total = pdt_price * int(quantity)

			wallet_obj.product_name = name
			wallet_obj.size = int(size_pdt)
			wallet_obj.amount = int(quantity)
			wallet_obj.status = True

			wallet_obj.price = pdt_price
			wallet_obj.total = pdt_total


			wallet_obj.save()
			# MyWalletModal.username = user name
			# MyWalletModal.product_namint(e = product.product_name
			# MyWalletModal.size = size
			# MyWalletModal.amount = amount
			# MyWalletModal.status = False
			
			response="Success"

		else :
			print("Error")
			response="Invalid Password"


		

		# print("hjv",quantity,size,name)


		return HttpResponse(json.dumps(response),content_type='json')


		# return render(request,'buy.html',dict1)

class MessageView(View):
	def post(self,request,*args, **kwargs):
		name = request.POST.get('usr_name')
		email = request.POST.get('usr_email')
		message = request.POST.get('usr_message')
		print("ghg")

		message_obj = MessageModal.objects.create(user_name=name,user_email=email,user_message=message)
		message_obj.save()

		response="success"
		return HttpResponse(json.dumps(response),content_type='json')

class ContactView(TemplateView):
	template_name="contact.html"