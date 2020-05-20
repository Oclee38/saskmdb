from django.urls import path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:cat_name>/', views.details, name='details')
]
