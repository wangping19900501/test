from django.conf.urls import url
from django.urls import path
from home import views

urlpatterns = [
	path('join/', views.signup, name='join'),
	path('login/', views.signin, name='login'),
]
