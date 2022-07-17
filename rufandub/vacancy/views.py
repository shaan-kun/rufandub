from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

class VacancyHome(ListView):
    model = Vacancy
    template_name = 'vacancy/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['selected_category'] = 0

        return context

    def get_queryset(self):
        return Vacancy.objects.filter(is_published=True)

# def index(request):
#     posts = Vacancy.objects.filter(is_published=True)
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'selected_category': 0,
#     }
#
#     return render(request, 'vacancy/index.html', context=context)

def about(request):
    return render(request, 'vacancy/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'vacancy/add_page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['title'] = 'Добавление статьи'

        return context


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     return render(request, 'vacancy/add_page.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

# def show_post(request, post_slug):
#     post = get_object_or_404(Vacancy, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'selected_category': post.category_id,
#     }
#
#     return render(request, 'vacancy/post.html', context=context)


class ShowPost(DetailView):
    model = Vacancy
    template_name = 'vacancy/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['title'] = context['post']

        return context


class VacancyCategory(ListView):
    model = Vacancy
    template_name = 'vacancy/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['menu'] = menu
        context['title'] = 'Категория — ' + str(context['posts'][0].category)
        context['selected_category'] = context['posts'][0].category_id

        return context

# def show_category(request, category_slug):
#     posts = Vacancy.objects.filter(category__slug=category_slug)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'selected_category': category_slug,
#     }
#
#     return render(request, 'vacancy/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')