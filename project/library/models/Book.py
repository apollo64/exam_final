from django.db import models


class Book(models.Model):
    name = models.CharField(
        verbose_name='Название книги',
        max_length=100,
        null=False,
        blank=False,
    )
    author = models.ForeignKey(
        'pawnshop.Author',
        related_name='books',
        verbose_name='Автор',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        default=None
    )
    created_at = models.DateField(
        verbose_name='Год издания',
        null=False,
        blank=False,
    )
    file = models.FileField(
        verbose_name='Текст книги',
        null=True,
        blank=True,
        upload_to='author_pics',
        default=None
    )
    cover = models.ImageField(
        verbose_name='Картинка обложки',
        upload_to='cover_pics',
        null=True,
        blank=True,
        default=None
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        null=True,
        blank=True,
        default=None
    )

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return f'Название книги \'{self.name} \''

