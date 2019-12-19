from django.contrib import admin
from django.urls import path

from accounts.views import UserDetailView, login_view, register_view, logout_view

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:user_pk>/', UserDetailView.as_view(), name='user_detail'),
    path('login', login_view, name='login'),
    path('new_user', register_view, name='create'),
    path('logout', logout_view, name='logout')
]
