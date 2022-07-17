from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *



class VacancyHome(DataMixin, ListView):
    model = Vacancy
    template_name = 'vacancy/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")

        return dict(list(context.items()) + list(c_def.items()))

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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'vacancy/add_page.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление статьи")

        return dict(list(context.items()) + list(c_def.items()))


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


class ShowPost(DataMixin, DetailView):
    model = Vacancy
    template_name = 'vacancy/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])

        return dict(list(context.items()) + list(c_def.items()))


class VacancyCategory(DataMixin, ListView):
    model = Vacancy
    template_name = 'vacancy/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Vacancy.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        c_def = self.get_user_context(title='Категория — ' + str(context['posts'][0].category),
                                      selected_category=context['posts'][0].category_id)

        return dict(list(context.items()) + list(c_def.items()))

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