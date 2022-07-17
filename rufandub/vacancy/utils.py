from django.db.models import Count

from .models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not  self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        categories = Category.objects.annotate(Count('vacancy'))
        context['categories'] = categories

        if 'selected_category' not in context:
            context['selected_category'] = 0

        return context
