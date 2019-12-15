from django.contrib import admin
from django.urls import path
from library.views.author import AuthorIndexView, AuthorDetailView, AuthorDeleteView, AuthorCreateView, AuthorUpdateView
from library.views.book import BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, BookIndexView

app_name = 'library'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors', AuthorIndexView.as_view(), name='author_list'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/<int:author_pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:author_pk>/delete', AuthorDeleteView.as_view(), name='author_delete'),
    path('author/<int:author_pk>/update', AuthorUpdateView.as_view(), name='author_update'),

    path('', BookIndexView.as_view(), name='index'),
    path('author/<int:author_pk>/book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/<int:book_pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book/<int:book_pk>/update', BookUpdateView.as_view(), name='book_update'),
    path('book/<int:book_pk>/delete', BookDeleteView.as_view(), name='book_delete'),
]
