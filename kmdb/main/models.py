from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Categorie(models.Model):
    cat_name = models.CharField('Category Name', max_length=256, unique=True)
    cat_description = models.TextField('Category Description')

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.tag_name


class Article(models.Model):
    name = models.CharField(max_length=80)
    url_link = models.URLField('URL', unique=True)
    data_added = models.DateTimeField('Added on')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    text = RichTextField('Content', max_length=4069)
    tags = models.ManyToManyField(Tag, related_name='items')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
