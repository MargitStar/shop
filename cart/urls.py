from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.AddBookToCart.as_view(), name='cart_view'),
    path('add/', views.AddBookToCart.as_view(), name='add_to_cart'),
]
