from django.urls import path 
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path("add/", views.add_to_cart, name="add"),
    path("menu/add/", views.add_to_cart_menu, name="add_menu"),
    path('about/', views.about, name='about'),
    path('message/', views.message, name='message'),
    path('cart/', views.CartView.as_view(), name='cart'),
    path("delete/<int:product_id>/<int:qty>", views.deleteItem, name="delete"),
    path('order/', views.CheckoutView.as_view(), name='checkout'),
    path('complated/', views.complated, name='complated')
]
