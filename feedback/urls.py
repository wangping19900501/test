from django.conf.urls import url
from django.urls import path
from feedback import views

urlpatterns = [
    path('list', views.list, name='list'),
	path('create', views.create, name='create'),
	path('edit/<int:id>/', views.edit, name='edit'),
]
