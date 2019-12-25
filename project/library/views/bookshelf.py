from django.views.generic import ListView

from library.models import Bookshelf


class BookshelfListView(ListView):
    model = Bookshelf
    template_name = 'bookshelf/list.html'
