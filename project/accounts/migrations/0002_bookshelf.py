# Generated by Django 2.1.11 on 2019-12-20 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20191213_1317'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookshelf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(blank=True, default=None, related_name='book_bookshelfs', to='library.Book', verbose_name='Книга')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_bookshelfs', to='accounts.Account', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Книжная полка',
                'verbose_name_plural': 'Книжные полки',
            },
        ),
    ]
