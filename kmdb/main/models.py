from django.db import models

# Create your models here.


class Category(models.Model):
    cat_name = models.CharField('Category Name', max_length=256)
    cat_description = models.TextField('Category Description')

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=250)

    def __str__(self):
        return self.tag_name


class Item(models.Model):
    url_link = models.URLField('URL')
    data_added = models.DateTimeField('Added on')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.TextField('Content')
    tags = models.ManyToManyField(Tag, related_name='items')

    def __str__(self):
        return self.url_link
