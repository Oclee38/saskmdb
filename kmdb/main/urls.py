from django.urls import path

from main import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('addarticle/', views.addarticle, name='newarticle'),
    path('addcat/', views.addcategory, name='add_cat'),
    path('login/', views.login_engine, name='login'),
    path('logout/', views.logout_engine, name='logout'),
    path('<str:cat_name>/', views.details, name='details'),

]
