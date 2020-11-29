from django.urls import path
from s_admin import views

app_name = 's_admin'

urlpatterns = [
    path('order/list/', views.SAdminOrderList.as_view(), name='s_admin_order_list'),
    path('order/update/<int:pk>/', views.SAdminOrderUpdate.as_view(), name='s_admin_order_update'),
    path('order/delete/<int:pk>/', views.SAdminOrderDelete.as_view(), name='s_admin_order_delete'),

    path('genre/list/', views.SAdminGenreList.as_view(), name='s_admin_genre_list'),
    path('genre/create/', views.SAdminGenreCreate.as_view(), name='s_admin_genre_create'),
    path('genre/view/<int:pk>/', views.SAdminGenreView.as_view(), name='s_admin_genre_view'),
    path('genre/update/<int:pk>/', views.SAdminGenreUpdate.as_view(), name='s_admin_genre_update'),
    path('genre/delete/<int:pk>/', views.SAdminGenreDelete.as_view(), name='s_admin_genre_delete'),
]
