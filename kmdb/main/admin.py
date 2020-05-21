from django.contrib import admin
from .models import Categorie, Article, Tag
# Register your models here.


class ArticelAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'approved']}),
        ('URL and Dates', {'fields': ['url_link',
                                      'data_added'], 'classes': ['collapse']}),
        ('Content', {'fields': ['text'], 'classes': ['collapse']}),
        ('Metadata', {'fields': ['category', 'tags'], 'classes': ['collapse']})
    ]
    list_display = ('name', 'approved', 'category')
    list_filter = ['category', 'approved']


admin.site.register(Categorie)
admin.site.register(Article, ArticelAdmin)
admin.site.register(Tag)
