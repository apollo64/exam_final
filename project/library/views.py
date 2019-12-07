from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.shortcuts import render

# Create your views here.
from library.models import Author


class AuthorIndexView(ListView):
    template_name = 'author/list.html'
    context_object_name = 'authors'
    paginate_by = 10
    paginate_orphans = 1
    # search_value = None
    model = Author
    ordering = ['name']

    def get_context_data(self, **kwargs):
        # Loan.expire_loans()
        return super().get_context_data(**kwargs)

class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    pk_url_kwarg = 'author_pk'
    model = Author



class AuthorDeleteView(UserPassesTestMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('library:index')
    template_name = 'author/delete.html'
    pk_url_kwarg = 'author_pk'


    def test_func(self):
        author = Author.objects.get(pk=self.kwargs['author_pk'])
        return author.id == self.request.user.is_superuser


