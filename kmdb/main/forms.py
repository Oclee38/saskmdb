from django.forms import ModelForm
from main.models import Article


class AddArticleForm(ModelForm):
    class Meta():
        model = Article
        fields = ['name', 'url_link', 'text']
