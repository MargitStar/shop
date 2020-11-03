"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello_world.views import hello_world
from django.conf import settings
from django.conf.urls.static import static
from references import views
from books.views import BookListView, BookView, create_book, delete_book, update_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListView.as_view()),
    path('book/<int:pk>/', BookView.as_view()),
    path('book/create', create_book),
    path('book/<int:pk_obj>/update', update_book),
    path('book/<int:pk_obj>/delete', delete_book),
    path('genre/', views.GenreListView.as_view()),
    path('genre/<int:pk>/', views.GenreView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorView.as_view()),
    path('publishing_house/', views.PublishingHouseListView.as_view()),
    path('publishing_house/<int:pk>/', views.PublishingHouseView.as_view()),
    path('series/', views.SeriesListView.as_view()),
    path('series/<int:pk>/', views.SeriesView.as_view()),
    path('genre/create/', views.create_genre),
    path('author/create', views.create_author),
    path('series/create', views.create_series),
    path('publishing_house/create', views.create_publishing_house),
    path('genre/<int:pk_obj>/update', views.update_genre),
    path('author/<int:pk_obj>/update', views.update_author),
    path('series/<int:pk_obj>/update', views.update_series),
    path('publishing_house/<int:pk_obj>/update', views.update_publishing_house),
    path('genre/<int:pk_obj>/delete', views.delete_genre),
    path('author/<int:pk_obj>/delete', views.delete_author),
    path('series/<int:pk_obj>/delete', views.delete_series),
    path('publishing_house/<int:pk_obj>/delete', views.delete_publishing_house),
    path('', hello_world)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
