# Generated by Django 5.1.6 on 2025-03-01 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza', '0016_rename_body1_news_body_remove_news_body2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlar',
            name='nomi',
            field=models.CharField(help_text='title of the news', max_length=250, verbose_name='xabar'),
        ),
    ]
