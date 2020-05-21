from django.shortcuts import (render, get_object_or_404, redirect)
from datetime import datetime


from .models import Categorie, Article
# Create your views here.


def index(request):
    """ Index View - Main page
    TODO: Change this to new view for List of Categories
    """
    Categories = Categorie.objects.all()
    context = {'Categories': Categories}
    return render(request, 'index.html', context)


def details(request, cat_name):
    """
    Datails page
    Arguments:
        Category name as cat_name
    Return:
        Renders the links.html file with all links with this category
    """
    category = get_object_or_404(Categorie, cat_name=cat_name)
    links = Article.objects.filter(category=category.pk)

    if not links:
        # return redirect('main:index')
        tags = ''
    else:
        for link in links:
            tags = link.tags.all()

    context = {'category': category, 'links': links, 'tags': tags}
    return render(request, 'links.html', context)


def addlink(request):
    """
    User can create new link - TODO must be logged in user
    return:
        GET: Shows the form to add new Article
        POST: Saves new Article to DB and redirect to home page
    """
    if request.method == 'POST':
        cat = Categorie.objects.get(cat_name=request.POST['category'])
        time = datetime.now()
        url = request.POST['Link']
        Article = Article(url_link=url, category=cat, data_added=time)
        Article.save()
        return redirect('main:index')

    categories = Categorie.objects.all()
    context = {'categories': categories, }
    return render(request, 'addlink.html', context)


def addcategory(request):
    if request.method == 'POST':
        cat_name = request.POST['name']
        cat_desc = request.POST['description']
        cat = Categorie(cat_name=cat_name, cat_description=cat_desc)
        cat.save()
        return redirect('main:index')
    return render(request, 'addcat.html')
