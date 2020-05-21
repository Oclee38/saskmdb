from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('addlink/', views.addlink, name='add_link'),
    path('addcat/', views.addcategory, name='add_cat'),
    path('<str:cat_name>/', views.details, name='details'),
]
