from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.shortcuts import render, redirect

# Create your views here.
from library.forms import AuthorForm
from library.models import Author


class AuthorUpdateView(UserPassesTestMixin, UpdateView):
    template_name = 'author/update.html'
    model = Author
    pk_url_kwarg = 'author_pk'
    form_class = AuthorForm
    context_object_name = 'author'


    def get_success_url(self):
        return reverse('library:author_detail', kwargs={'author_pk': self.object.pk})

    def test_func(self):
        return self.request.user.is_superuser


class AuthorIndexView(ListView):
    template_name = 'author/list.html'
    context_object_name = 'authors'
    # paginate_by = 10
    # paginate_orphans = 1
    model = Author
    ordering = ['name']

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class AuthorDetailView(DetailView):
    template_name = 'author/detail.html'
    pk_url_kwarg = 'author_pk'
    model = Author
    context_object_name = 'author'


class AuthorDeleteView(UserPassesTestMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('library:index')
    template_name = 'author/delete.html'
    pk_url_kwarg = 'author_pk'

    def test_func(self):
        Author.objects.get(pk=self.kwargs['author_pk'])
        return self.request.user.is_superuser


class AuthorCreateView(UserPassesTestMixin, CreateView):
    template_name = 'author/create.html'
    model = Author
    form_class = AuthorForm
    context_object_name = 'author'


    def test_func(self):
        return self.request.user.is_superuser

    def form_valid(self, form):
        data = form.cleaned_data
        author = Author.objects.create(name=data['name'],
                                       birth_date=data['birth_date'],
                                       death_date=data['death_date'],
                                       biography=data['biography'],
                                       image=data['image'],
                                       )
        author.save()
        self.object = author
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('library:author_detail', kwargs={'author_pk': self.object.pk})
