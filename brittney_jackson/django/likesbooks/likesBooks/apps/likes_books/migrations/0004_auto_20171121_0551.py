# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-21 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0003_book_liked_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='liked_books',
        ),
        migrations.AddField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(related_name='liked_books', to='likes_books.User'),
        ),
    ]
