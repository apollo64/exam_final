from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView

from library.models import Book


class BookDetailView(DetailView):
    template_name = 'book/detail.html'
    pk_url_kwarg = 'book_pk'
    model = Book

