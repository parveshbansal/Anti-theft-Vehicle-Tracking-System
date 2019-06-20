from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class SignUpForm(forms.ModelForm):
	class Meta:
		model=User   #mean of this line based on db table user create this form
		fields=['username','password','email','first_name','last_name']
class MyForm(forms.Form):
	pass
