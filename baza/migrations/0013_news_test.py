# Generated by Django 5.1.6 on 2025-02-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0012_remove_news_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='test',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
