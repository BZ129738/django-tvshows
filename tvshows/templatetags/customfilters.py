from django import template
# from django.contrib.auth.models import Group

from tvshows.models import Show

register = template.Library()


@register.filter(name='get_count_of_category')
def get_count_of_category(value):
    tvshows = Show.objects.filter(accepted=True)
    count = tvshows.filter(category = value).count()
    return str(count)

@register.filter(name='get_year')
def get_year(value):
    return str(value.year)

@register.filter(name='get_month_and_year')
def get_month_and_year(value):
    month =str(value.strftime("%B"))
    year = str(value.year)
    return str(month+" "+year)

@register.filter(name='get_accepted_comment')
def get_accepted_comment(value):
    comments = value.filter(accepted=True)
    return comments

@register.filter(name='get_unconfirmed_comment')
def get_unconfirmed_comment(value):
    comments = value.filter(accepted=False)
    return comments


# @register.filter(name='has_group')
# def has_group(user, group_name):
#     group = Group.objects.get(name=group_name)
#     return True if group in user.groups.all() else False