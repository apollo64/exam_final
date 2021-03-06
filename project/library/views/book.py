from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from library.forms import BookForm
from library.models import Book, Author



class BookIndexView(ListView):
    template_name = 'book/list.html'
    context_object_name = 'books'
    # paginate_by = 10
    # paginate_orphans = 1
    model = Book
    ordering = ['name']

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

class BookUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'book/update.html'
    model = Book
    pk_url_kwarg = 'book_pk'
    form_class = BookForm
    context_object_name = 'book'


    def get_success_url(self):
        return reverse('library:book_detail', kwargs={'book_pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser


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


class BookDeleteView(UserPassesTestMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('library:index')  # правильно было бы поставить возврат на автора книги
    template_name = 'book/delete.html'
    pk_url_kwarg = 'book_pk'

    def test_func(self):
        return self.request.user.is_superuser



# def booktobookshelf(book, self.request.user):
#     user = self.user
#
#     if book in
#     user.bookshelf.book.add(data['book'])
#     tags = data['tags'].split(',')
#     db_tags = Tag.objects.all()
#     for tag in tags:
#         if tag not in db_tags:
#             article.tags.add(Tag.objects.create(tag=tag.strip()))
#         else:
#             article.tags.add(Tag.objects.filter(tag__iexact=tag.strip()))
#     return article
