# Generated by Django 2.1.11 on 2019-12-25 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_bookshelf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshelf',
            name='book',
        ),
        migrations.RemoveField(
            model_name='bookshelf',
            name='user',
        ),
        migrations.DeleteModel(
            name='Bookshelf',
        ),
    ]
