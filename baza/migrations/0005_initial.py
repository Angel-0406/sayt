# Generated by Django 5.1.6 on 2025-02-22 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('baza', '0004_delete_izohlar_delete_news_delete_postlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=100)),
                ('rasmi', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Postlar',
                'db_table': 'postlar',
            },
        ),
    ]
