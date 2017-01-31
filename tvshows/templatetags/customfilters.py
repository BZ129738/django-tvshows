from django import template
from tvshows.models import Show, Category

register = template.Library()


@register.filter(name='get_count_of_category')
def get_count_of_category(value):
    tvshows = Show.objects.filter(accepted=True)
    count = tvshows.filter(category = value).count()
    return str(count)

@register.filter(name='get_year')
def get_year(value):
    return str(value.year)