from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Floral - Главная',
        'content': "Комнатные растения и цветы",
        'categories': categories
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Floral - О нас',
        'content': "О нас",
        'text_on_page': "Челеееееееееееееееен"
    }

    return render(request, 'main/about.html', context)