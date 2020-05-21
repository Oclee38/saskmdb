from django.shortcuts import (
    render, get_object_or_404, redirect)
from datetime import datetime
from .models import Categorie, Article, Tag
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    """ Index View - Main page
    TODO: Change this to new view for List of Categories
    """
    Categories = Categorie.objects.all()
    context = {'Categories': Categories}
    return render(request, 'index.html', context)


@login_required
def details(request, cat_name):
    """
    Datails page
    Arguments:
        Category name as cat_name
    Return:
        Renders the links.html file with all links with this category
    """
    category = get_object_or_404(Categorie, cat_name=cat_name)
    links = Article.objects.filter(category=category.pk, approved=True)

    if not links:
        # return redirect('main:index')
        tags = ''
    else:
        for link in links:
            tags = link.tags.all()

    context = {'category': category, 'links': links, 'tags': tags}
    return render(request, 'links.html', context)


@login_required(login_url='main:index')
def addarticle(request):
    error_message = ''
    """
    User can create new link - TODO must be logged in user
    return:
        GET: Shows the form to add new Article
        POST: Saves new Article to DB and redirect to home page
    """
    if request.method == 'POST':
        if not validate_article(request):
            try:
                save_article(request)
                return redirect('main:index')
            except IntegrityError:
                error_message = "URL is already added,You can request admin to add your contents via email"

        else:
            error_message = validate_article(request)

    categories = Categorie.objects.all()
    tags = Tag.objects.all()

    context = {'categories': categories,
               'tags': tags, 'error_message': error_message}
    return render(request, 'addarticle.html', context)


@login_required(login_url='main:index')
def validate_article(request):
    if request.POST['name'] == "":
        return "Name cannot be empty"
    elif request.POST['Link'] == "":
        return "URL cannot be empty"
    elif request.POST['category'] == "":
        return "Category cannot be empty"
    elif request.POST['content'] == "":
        return "Content cannot be empty"
    elif request.POST['tags'] == "":
        return "Tags cannot be empty"
    else:
        return False


@login_required(login_url='main:index')
def save_article(request):
    name = request.POST['name']
    cat = Categorie.objects.get(cat_name=request.POST['category'])
    time = datetime.now()
    url = request.POST['Link']
    content = request.POST['content']
    Articles = Article(url_link=url, category=cat,
                       data_added=time, name=name, text=content)
    Articles.save()


@login_required(login_url='main:index')
def addcategory(request):
    if request.method == 'POST':
        cat_name = request.POST['name']
        cat_desc = request.POST['description']
        cat = Categorie(cat_name=cat_name, cat_description=cat_desc)
        cat.save()
        return redirect('main:index')
    return render(request, 'addcat.html')


def login_engine(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('main:index')


@login_required(login_url='main:index')
def logout_engine(request):
    logout(request)
    return redirect('main:index')
