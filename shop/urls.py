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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from books.views import BookListView, BookView, CreateBook, DeleteBookView, UpdateBook

from references import views
from home_screen.views import TopBooksListView
from my_auth.views import MyLogInView, MyLogOutView, MyPasswordChangeDoneView, MyPasswordChangeView, SignUpView
from cart import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', BookListView.as_view()),
    path('signin/', MyLogInView.as_view(), name="login"),
    path('logout/', MyLogOutView.as_view(), name='logout'),
    path('password_change/', MyPasswordChangeView.as_view(),
         name='password_change'),
    path('password_change_done/', MyPasswordChangeDoneView.as_view(),
         name='password_change_done'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('profile/', include('my_profile.urls', namespace='profile')),
    path('order/', include('order.urls', namespace='order')),
    path('s_admin/', include('s_admin.urls', namespace='s_admin')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('book/<int:pk>/', BookView.as_view()),
    path('book/create', CreateBook.as_view()),
    path('book/<int:pk>/update', UpdateBook.as_view()),
    path('book/<int:pk>/delete', DeleteBookView.as_view()),
    path('genre/', views.GenreListView.as_view()),
    path('genre/<int:pk>/', views.GenreView.as_view()),
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>/', views.AuthorView.as_view()),
    path('publishing_house/', views.PublishingHouseListView.as_view()),
    path('publishing_house/<int:pk>/', views.PublishingHouseView.as_view()),
    path('series/', views.SeriesListView.as_view()),
    path('series/<int:pk>/', views.SeriesView.as_view()),
    path('genre/create/', views.CreateGenre.as_view()),
    path('author/create', views.CreateAuthor.as_view()),
    path('series/create', views.CreateSeries.as_view()),
    path('publishing_house/create', views.CreatePublishingHouse.as_view()),
    path('genre/<int:pk>/update', views.UpdateGenre.as_view()),
    path('author/<int:pk>/update', views.UpdateAuthor.as_view()),
    path('series/<int:pk>/update', views.UpdateSeries.as_view()),
    path('publishing_house/<int:pk>/update', views.UpdatePublishingHouse.as_view()),
    path('genre/<int:pk>/delete', views.DeleteGenreView.as_view()),
    path('author/<int:pk>/delete', views.DeleteAuthorView.as_view()),
    path('series/<int:pk>/delete', views.DeleteSeriesView.as_view()),
    path('publishing_house/<int:pk>/delete', views.DeletePublishingHouseView.as_view()),
    path('', TopBooksListView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
