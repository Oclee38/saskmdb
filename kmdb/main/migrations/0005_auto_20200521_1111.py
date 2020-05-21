# Generated by Django 3.0.6 on 2020-05-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200521_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(max_length=4069, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='item',
            name='url_link',
            field=models.URLField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
