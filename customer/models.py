# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class customer_registeration_model(models.Model):

	user = models.OneToOneField(User)
	age = models.IntegerField(default=18)
	contact1 = models.IntegerField()
	contact2 = models.IntegerField()
	loaction = models.CharField(max_length=25)
	zip_code = models.IntegerField()
	created_on = models.DateTimeField(auto_now=True)


class MyWalletModal(models.Model):

	username = models.ForeignKey(User)
	user_location = models.CharField(max_length=25,null=True,blank=True)
	user_contact_no1 = models.IntegerField(null=True,blank=True)
	user_contact_no2 = models.IntegerField(null=True,blank=True)
	user_zip_code = models.IntegerField(null=True,blank=True)

	product_name = models.CharField(max_length=50,null=True,blank=True)
	size = models.IntegerField(null=True,blank=True)
	amount = models.IntegerField(null=True,blank=True,default=0)
	status = models.BooleanField(default=False,blank=True)
	price =  models.IntegerField(null=True,blank=True,default=0)

	total =  models.IntegerField(null=True,blank=True,default=0)
	created_on = models.DateTimeField(auto_now=True)
	
class MessageModal(models.Model):

	user_name = models.CharField(max_length=25,null=True,blank=True)
	user_email = models.EmailField(null=True,blank=True)
	user_message = models.TextField(null=True,blank=True)

	created_on = models.DateTimeField(auto_now=True)





