from django.urls import path
from .views import home,login_view,contact_us,about
urlpatterns = [
	path('about/',about,name='about'),
	path('contact/',contact_us,name='contact'),
	path('login/',login_view,name='login_url'),
    path('',home,name='home_url'),
]
