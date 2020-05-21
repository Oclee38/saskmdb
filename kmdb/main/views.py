from django.shortcuts import (render, get_object_or_404, redirect)
from datetime import datetime


from .models import Category, Item
# Create your views here.


def index(request):
    Categories = Category.objects.all()
    context = {'Categories': Categories}
    return render(request, 'index.html', context)


def details(request, cat_name):
    category = get_object_or_404(Category, cat_name=cat_name)
    links = Item.objects.filter(category=category.pk)

    for link in links:
        tags = link.tags.all()
    context = {'category': category, 'links': links, 'tags': tags}
    return render(request, 'links.html', context)


def addlink(request):
    if request.method == 'POST':
        cat = Category.objects.get(cat_name=request.POST['category'])
        time = datetime.now()
        url = request.POST['Link']
        item = Item(url_link=url, category=cat, data_added=time)
        item.save()
        return redirect('main:index')

    categories = Category.objects.all()
    context = {'categories': categories, }
    return render(request, 'addlink.html', context)


def addcategory(request):
    if request.method == 'POST':
        cat_name = request.POST['name']
        cat_desc = request.POST['description']
        cat = Category(cat_name=cat_name, cat_description=cat_desc)
        cat.save()
        return redirect('main:index')
    return render(request, 'addcat.html')
