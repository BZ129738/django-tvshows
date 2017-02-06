from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from tvshows.models import Show, Category
from .forms import TvshowForm
from django.utils import timezone


def tvshow_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    tvshows = Show.objects.filter(accepted=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tvshows = tvshows.filter(category=category)
    return render(request, 'tvshows.html', {'category': category,
                                            'categories': categories,
                                            'tvshows': tvshows, })


def tvshow_details(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug, accepted=True)
    return render(request,
                  'detail.html',
                  {'tvshows': tvshows, })


@login_required
def new_tvshow(request):
    if request.method == "POST":
        form = TvshowForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.updated = timezone.now();
            post.accepted = False;
            slug = str(post.title) + '-' + str(post.aired_from.strftime("%Y"));
            post.slug = slug.replace(" ", "-")
            post.save()
            form.save_m2m()
            return redirect('tvshow_list')
    else:
        form = TvshowForm()
    return render(request, 'edit.html', {'form': form})


@login_required
def tvshow_update(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug)
    form = TvshowForm(request.POST or None, instance=tvshows)
    if form.is_valid():
        form.save()
        return redirect('tvshow_list')

    return render(request, 'edit.html', {'form': form})


@login_required
def tvshow_delete(request, id, slug):
    tvshow = get_object_or_404(Show, id=id, slug=slug)
    if request.method == 'POST':
        tvshow.delete()
        return redirect('tvshow_list')

    return render(request, 'delete_confirm.html', {'object': tvshow})
