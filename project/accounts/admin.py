from django.contrib import admin

# Register your models here.
from .models import Account
from .models import Bookshelf

admin.site.register(Account)
admin.site.register(Bookshelf)
