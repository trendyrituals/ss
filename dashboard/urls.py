from django.urls import path
from .views import home,logout_view,create_customer,create_shopkeeper,detail_view
urlpatterns = [
	path('logout/',logout_view,name='logout_url'),
	path('detail/',detail_view,name='detail_url'),
	path('customer/',create_customer,name='create_customer'),
	path('shopkeeper/',create_shopkeeper,name='create_shopkeeper'),
    path('',home,name='home_url'),
]
