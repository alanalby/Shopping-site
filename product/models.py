# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categories(models.Model):
	category_title =models.CharField(max_length=25)
	category_discrption = models.TextField(null=True,blank=True)
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.category_title




class SubCategories(models.Model):
	category = models.ForeignKey(Categories)
	sub_category_title = models.CharField(max_length=25)
	sub_category_disc = models.TextField(null=True,blank=True)
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.sub_category_title





class ProductModel(models.Model):

	product_code = models.CharField(max_length = 300 ,blank=True , null=True)
	product_name = models.CharField(max_length=25,primary_key=True)
	product_description = models.TextField(null=True,blank=True)
	pdt_category = models.ForeignKey(Categories)
	pdt_sub_category = models.ForeignKey(SubCategories)
	pdt_image = models.ImageField(upload_to="image/" , null=True, blank=True)
	price = models.IntegerField()
	tax = models.IntegerField()
	discount = models.IntegerField()
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.product_name

class Size(models.Model):

	size = models.CharField(max_length=10)
	created_on = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.size

class Stock(models.Model):

	stock_name = models.ForeignKey(ProductModel)
	size = models.ForeignKey(Size)
	stock = models.IntegerField(default=0)
	created_on = models.DateTimeField(auto_now=True)

	
 
# class Order(models.Model):



 

