from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/', views.AddBookToCart.as_view(), name='cart_update'),
    path('', views.CartView.as_view(), name='cart_view')
]
