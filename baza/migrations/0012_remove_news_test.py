# Generated by Django 5.1.6 on 2025-02-25 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0011_remove_news_update_time_news_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='test',
        ),
    ]
