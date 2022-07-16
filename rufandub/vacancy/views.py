from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404

from vacancy.models import Vacancy, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

def index(request):
    posts = Vacancy.objects.filter(is_published=True)

    context = {
        'posts': posts,
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

def show_post(request, post_slug):
    post = get_object_or_404(Vacancy, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'selected_category': post.category_id,
    }

    return render(request, 'vacancy/post.html', context=context)

def show_category(request, category_slug):
    posts = Vacancy.objects.filter(category__slug=category_slug)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'selected_category': category_slug,
    }

    return render(request, 'vacancy/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')