from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from models import customer_registeration_model


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ('username','first_name','last_name','password1','password2','email')


class CustomerForm(forms.ModelForm):

	class Meta:
		model = customer_registeration_model
		exclude = ("user",)