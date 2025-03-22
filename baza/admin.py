from django.contrib import admin
from .models import Category, News, Contact
from import_export.admin import ImportExportModelAdmin
admin.site.register(Contact)

@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    list_display =('title','slug','publish_time','status')
    list_filter = ('publish_time','status','create')
    date_hierarchy = 'publish_time'
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    ordering = ('publish_time','status')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


