from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class ShopkeeperForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	re_password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'username',
			'email',
			'password',
			're_password'
		]