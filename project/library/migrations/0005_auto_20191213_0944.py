# Generated by Django 2.1.11 on 2019-12-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='book_files', verbose_name='Текст книги'),
        ),
    ]
