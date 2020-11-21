from django.urls import path
from . import views

app_name = 'cart'
urlpatterns = [
    path('add/', views.AddBookToCart.as_view(), name='cart_update'),
    path('delete/<int:pk>', views.BookInCartDelete.as_view(), name='book_in_cart_delete'),
    path('', views.CartView.as_view(), name='cart_view')
]
