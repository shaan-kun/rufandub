from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render

from vacancy.models import Vacancy, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Vacancy.objects.all()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories,
        'menu': menu,
        'title': 'Главная страница',
        'selected_category': 0,
    }

    return render(request, 'vacancy/index.html', context=context)

def about(request):
    return render(request, 'vacancy/about.html', {'menu': menu, 'title': 'О сайте'})

def add_page(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def show_category(request, category_id):
    posts = Vacancy.objects.filter(category_id=category_id)
    categories = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'categories': categories,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'selected_category': category_id,
    }

    return render(request, 'vacancy/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')