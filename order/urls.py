from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('create/<int:pk>', views.CreateOrder.as_view(), name='create_order'),
]
