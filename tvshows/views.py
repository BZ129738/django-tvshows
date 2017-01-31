from django.shortcuts import render, get_object_or_404
from tvshows.models import Show,Category



def tvshow_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    tvshows = Show.objects.filter(accepted=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tvshows = tvshows.filter(category=category)
    return render(request, 'tvshows.html', {'category': category,
                                                      'categories': categories,
                                                      'tvshows': tvshows,})


def tvshow_details(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug, accepted=True)
    return render(request,
                  'detail.html',
                  {'tvshows': tvshows,})
