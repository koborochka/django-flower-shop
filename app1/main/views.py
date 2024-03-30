from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Floral - Главная',
        'content': "Комнатные растения и цветы"
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Floral - О нас',
        'content': "О нас",
        'text_on_page': "Челеееееееееееееееен"
    }

    return render(request, 'main/about.html', context)