from django.db import models
from accounts.models import Account


class Bookshelf(models.Model):
    user = models.OneToOneField(Account,
                            on_delete=models.CASCADE,
                            verbose_name='Пользователь',
                            related_name='user_bookshelfs',
                            null=False,
                            blank=False
                            )
    book = models.ManyToManyField('library.Book',
                                  verbose_name='Книга',
                                  related_name='book_bookshelfs',
                                  blank=True,
                                  default=None
                                  )
    class Meta:
        verbose_name = 'Книжная полка'
        verbose_name_plural = 'Книжные полки'

    def __str__(self):
        return f'Полка пользователя \'{self.user.username} \''

