from django.views.generic import ListView, DetailView
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
