from django.http import HttpResponse
from django.shortcuts import render

from vacancy.models import Vacancy

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']

def index(request):
    posts = Vacancy.objects.all()

    return render(request, 'vacancy/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'vacancy/about.html', {'menu': menu, 'title': 'О сайте'})

def categories(request, category_id):
    return HttpResponse(f"<h1>Категории</h1><p>Номер категории: {category_id}</p>")