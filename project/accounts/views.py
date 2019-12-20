from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from accounts.forms import UserForm
from accounts.models import Account


class UserDetailView(DetailView):
    template_name = 'detail.html'
    pk_url_kwarg = 'user_pk'
    model = User
    context_object_name = 'user'


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('library:index')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['username'] = username
    else:
        context = {'next': request.GET.get('next')}
    return render(request, 'login.html', context=context)


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            user.save()

            login(request, user)
            return redirect('library:index')
    else:
        form = UserForm()
    return render(request, 'create.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('library:index')

class UserListView(ListView):
    template_name = 'list.html'
    context_object_name = 'users'
    model = Account
    ordering = ['pk']

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
