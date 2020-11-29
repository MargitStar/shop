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

    path('series/list/', views.SAdminSeriesList.as_view(), name='s_admin_series_list'),
    path('series/create/', views.SAdminSeriesCreate.as_view(), name='s_admin_series_create'),
    path('series/view/<int:pk>/', views.SAdminSeriesView.as_view(), name='s_admin_series_view'),
    path('series/update/<int:pk>/', views.SAdminSeriesUpdate.as_view(), name='s_admin_series_update'),
    path('series/delete/<int:pk>/', views.SAdminSeriesDelete.as_view(), name='s_admin_series_delete'),

    path('author/list/', views.SAdminAuthorList.as_view(), name='s_admin_author_list'),
    path('author/create/', views.SAdminAuthorCreate.as_view(), name='s_admin_author_create'),
    path('author/view/<int:pk>/', views.SAdminAuthorView.as_view(), name='s_admin_author_view'),
    path('author/delete/<int:pk>/', views.SAdminAuthorDelete.as_view(), name='s_admin_author_delete'),
    path('author/update/<int:pk>/', views.SAdminAuthorUpdate.as_view(), name='s_admin_author_update'),

    path('publishing_house/list/', views.SAdminPublishingHouseList.as_view(), name='s_admin_publishing_house_list'),
    path('publishing_house/create/', views.SAdminPublishingHouseCreate.as_view(),
         name='s_admin_publishing_house_create'),
    path('publishing_house/view/<int:pk>/', views.SAdminPublishingHouseView.as_view(),
         name='s_admin_publishing_house_view'),
    path('publishing_house/update/<int:pk>/', views.SAdminPublishingHouseUpdate.as_view(),
         name='s_admin_publishing_house_update'),
    path('publishing_house/delete/<int:pk>/', views.SAdminPublishingHouseDelete.as_view(),
         name='s_admin_publishing_house_delete'),
]
