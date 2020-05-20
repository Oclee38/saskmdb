from django.shortcuts import render, get_object_or_404

from .models import Category, Item
# Create your views here.


def index(request):
    Categories = Category.objects.all()
    # template = loader.get_template('index.html')
    context = {'Categories': Categories}
    return render(request, 'index.html', context)


def details(request, cat_name):
    category = get_object_or_404(Category, cat_name=cat_name)
    links = Item.objects.get(category=category.pk)
    context = {'category': category, 'links': links}
    return render(request, 'links.html', context)
