from django import template
from vacancy.models import *


register = template.Library()

@register.simple_tag()
def get_categories(filter=None):
    if filter is None:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('vacancy/list_categories.html')
def show_categories(sort=None, selected_category=0):
    if sort is None:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {"categories": categories, "selected_category": selected_category}
