from django.urls import path
from s_admin import views

app_name = 's_admin'

urlpatterns = [
    path('order/list/', views.SAdminOrderList.as_view(), name='s_admin_order_list')
]
