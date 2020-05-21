from django.contrib import admin
from .models import Categorie, Item, Tag
# Register your models here.

admin.site.register(Categorie)
admin.site.register(Item)
admin.site.register(Tag)
