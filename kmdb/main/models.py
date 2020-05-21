from django.db import models

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


class Item(models.Model):
    url_link = models.URLField('URL', unique=True)
    data_added = models.DateTimeField('Added on')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    text = models.TextField('Content', max_length=4069)
    tags = models.ManyToManyField(Tag, related_name='items')

    def __str__(self):
        return self.url_link
