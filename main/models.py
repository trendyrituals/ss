from django.db import models

# Create your models here.
class Profile(models.Model):
	user_code = models.CharField(blank=False,max_length=200)
	user_name = models.CharField(blank=False,max_length=200)
	ref_user = models.CharField(blank=False,max_length=200)
	ref_user_code = models.CharField(blank=False,max_length=200)


	def __str__(self):
		return self.user_name



class Enquiry(models.Model):
	fullname = models.CharField(blank=False,max_length=100)
	email = models.EmailField(blank=False)
	phone = models.CharField(blank=False,max_length=10)
	msg = models.TextField(blank=False)


	def __str__(self):
		return self.fullname