from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField() #put email in registration form

	class Meta: #Configuration of new Form created
		model = User #model gona be affected 
		fields = ['username', 'email', 'password1', 'password2'] #fields would be in the form and order
