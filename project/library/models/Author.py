from django.db import models


class Author(models.Model):
    name = models.CharField(
        verbose_name='ФИО',
        max_length=100,
        null=False,
        blank=False,
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        null=True,
        blank=True,
        default=None
    )
    death_date = models.DateField(
        verbose_name='Дата смерти',
        null=True,
        blank=True,
        default=None
    )
    biography = models.TextField(
        verbose_name='Биография',
        max_length=3000,
        null=True,
        blank=True,
        default=None
    )

    image = models.ImageField(
        verbose_name='Фотография',
        upload_to='author_pics',
        null=True,
        blank=True,
        default=None
    )

    status = models.BooleanField(
        verbose_name='Статус',
        max_length=100,
        null=False,
        blank=False,
        default=True,
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'Автор \'{self.name} \''
