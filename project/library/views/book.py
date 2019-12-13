from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from library.forms import BookForm
from library.models import Book, Author


class BookDetailView(DetailView):
    template_name = 'book/detail.html'
    pk_url_kwarg = 'book_pk'
    model = Book


class BookCreateView(UserPassesTestMixin, CreateView):
    template_name = 'book/create.html'
    model = Book
    form_class = BookForm
    context_object_name = 'book'

    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        data = form.cleaned_data
        form.instance.author = self.get_author()
        book = Book.objects.create(name=data['name'],
                                   created_at=data['created_at'],
                                   file=data['file'],
                                   cover=data['cover'],
                                   description=data['description'],
                                   author=form.instance.author
                                   )
        book.save()
        self.object = book
        return redirect(self.get_success_url())

    # def form_valid(self, form):
    #     form.instance.article = self.get_article()
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def get_author(self):
        return Author.objects.get(pk=self.kwargs.get('author_pk'))

    def get_context_data(self, **kwargs):
        kwargs['author'] = self.get_author()
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'book_pk': self.object.pk})
