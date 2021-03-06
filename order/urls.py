from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('create/', views.CreateOrder.as_view(), name='create_order'),
    path('update/<int:pk>/', views.CancelOrder.as_view(), name='update_order'),
]
