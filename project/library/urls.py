from django.contrib import admin
from django.urls import path
from library.views import AuthorIndexView, AuthorDetailView, AuthorDeleteView

app_name = 'library'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AuthorIndexView.as_view(), name='index'),
    path('author/<int:author_pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('author/<int:author_pk>/delete', AuthorDeleteView.as_view(), name='author_delete')
]

