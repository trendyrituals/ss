from django import forms
# from django.contrib.auth import get_user_model
from .models import Enquiry


# User = get_user_model()


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)



class EnquiryForm(forms.ModelForm):
	class Meta:
		model = Enquiry
		fields = [
			'fullname',
			'email',
			'phone',
			'msg'
			]


