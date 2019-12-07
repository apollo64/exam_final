from django.contrib import admin
from django.urls import path
from library.views import AuthorIndexView

app_name = 'library'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', AuthorIndexView.as_view(), name='index'),

]

