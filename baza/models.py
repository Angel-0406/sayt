from django.db import models
from django.template.context_processors import request
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.Published)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori", help_text="Ma'lumot yo'nalishlari")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Yo'nalishlar"


class News(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PD', 'Published'

    title = models.CharField(max_length=250, help_text="Title of the news", verbose_name="xabar")
    slug = models.SlugField(max_length=250, help_text="o'zi to'ldiriladi", verbose_name="url shakli")
    body = models.TextField(verbose_name="Asosiy qismi", max_length=1000, default="")
    image = models.ImageField(upload_to="news/images")
    categoriy = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)

    class Meta:
        ordering = ['-publish_time']
        verbose_name_plural = "Yangiliklar"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


class Contact(models.Model):
    name = models.CharField(max_length=250, verbose_name="kontakt")
    email = models.EmailField(verbose_name="email", max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.name



