from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    path('edit_product/', views.edit_product, name='edit_product'),

    path('add_list/', views.add_list, name='add_list'),
    path('delete_list/<int:pk>/', views.delete_list, name='delete_list'),
    path('edit_list/', views.edit_list, name='edit_list'),
    path('add_prod_in_list/', views.add_prod_in_list, name='add_prod_in_list'),

    
    path('show_list/<int:pk>/', views.show_list, name='show_list'), 
    path('showRecipt/<int:pk>/', views.show_recipt, name='show_recipt'), 

    path('add_recipt/', views.add_recipt, name='add_recipt'),
    path('delete_recipt/<int:pk>/', views.delete_recipt, name='delete_recipt'),
    path('edit_recipt/', views.edit_recipt, name='edit_recipt'),
    path('add_prod_in_recipt/', views.add_prod_in_recipt, name='add_prod_in_recipt'),
]
