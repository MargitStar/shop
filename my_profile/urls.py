from django.urls import path
from . import views

app_name = 'profile'
urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile_view'),
    path('<int:pk>/update/', views.UpdateProfileView.as_view(), name='profile_update'),
]
