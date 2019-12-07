from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.shortcuts import render, redirect

# Create your views here.
from library.forms import AuthorForm
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
        Author.objects.get(pk=self.kwargs['author_pk'])
        return self.request.user.is_superuser


class AuthorCreateView(CreateView):
    template_name = 'author/create.html'
    model = Author
    form_class = AuthorForm

    def form_valid(self, form):
        data = form.cleaned_data
        author = Author.objects.create(name=data['name'],
                                       birth_date=data['birth_date'],
                                       death_date=data['death_date'],
                                       biography=data['biography'],
                                       image=data['image'],
                                       )
        self.object = author
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('library:author_detail', kwargs={'author_pk': self.object.pk})


