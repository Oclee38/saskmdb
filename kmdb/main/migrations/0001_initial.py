# Generated by Django 3.0.6 on 2020-05-21 15:02

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=256, unique=True, verbose_name='Category Name')),
                ('cat_description', models.TextField(verbose_name='Category Description')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('url_link', models.URLField(unique=True, verbose_name='URL')),
                ('data_added', models.DateTimeField(verbose_name='Added on')),
                ('text', tinymce.models.HTMLField(max_length=4069, verbose_name='Content')),
                ('approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Categorie')),
                ('tags', models.ManyToManyField(related_name='items', to='main.Tag')),
            ],
        ),
    ]
