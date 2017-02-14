from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from tvshows.models import Show, Category, Comment, Article
from .forms import TvshowForm, CommentsForm, ArticlesForm
from django.utils import timezone
from django.contrib.auth.decorators import user_passes_test

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


@user_passes_test(lambda u: u.is_superuser)
def tvshow_unaccepted(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    tvshows = Show.objects.filter(accepted=False)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tvshows = tvshows.filter(category=category)
    return render(request, 'tvshows.html', {'category': category,
                                            'categories': categories,
                                            'tvshows': tvshows, })

@login_required
def tvshow_accept(request, id):
    shownota = get_object_or_404(Show, id=id)
    shownota.accept()
    return redirect('tvshow_unaccepted')

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles, })


def tvshow_details(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug, accepted=True)
    if request.method == "POST":
        form = CommentsForm(request.POST)
    else:
        form = CommentsForm()
    return render(request,
                  'detail.html',
                  {'tvshows': tvshows, 'form': form, })


def article_details(request, id):
    print ("test2")
    article = get_object_or_404(Article, id=id)
    return render(request,
                  'article.html',
                  {'article': article, })

@login_required
def new_article(request):
    if request.method == "POST":
        forms = ArticlesForm(request.POST, request.FILES)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.created = timezone.now();
            post.author = request.user;
            post.save()
            return redirect('article_list')
    else:
        forms = ArticlesForm()
    return render(request, 'edit_article.html', {'forms': forms})


@login_required
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')

    return render(request, 'delete_confirm.html', {'object': article})

@login_required
def article_update(request, id):
    article = get_object_or_404(Article, id=id)
    forms = ArticlesForm(request.POST or None, request.FILES or None, instance=article)
    if forms.is_valid():
        forms.save()
        return redirect('article_list')

    return render(request, 'edit_article.html', {'forms': forms})



@login_required
def new_tvshow(request):
    if request.method == "POST":
        forms = TvshowForm(request.POST, request.FILES)
        if forms.is_valid():
            post = forms.save(commit=False)
            post.updated = timezone.now();
            post.accepted = False;
            slug = str(post.title) + '-' + str(post.aired_from.strftime("%Y"));
            post.slug = slug.replace(" ", "-")
            post.save()
            forms.save_m2m()
            return redirect('tvshow_list')
    else:
        forms = TvshowForm()
    return render(request, 'edit.html', {'forms': forms})


@login_required
def tvshow_update(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug)
    forms = TvshowForm(request.POST or None, request.FILES or None, instance=tvshows)
    if forms.is_valid():
        forms.save()
        return redirect('tvshow_list')

    return render(request, 'edit.html', {'forms': forms})


@login_required
def tvshow_delete(request, id, slug):
    tvshow = get_object_or_404(Show, id=id, slug=slug)
    if request.method == 'POST':
        tvshow.delete()
        return redirect('tvshow_list')

    return render(request, 'delete_confirm.html', {'object': tvshow})


@login_required
def tvshow_comment(request, id, slug):
    tvshows = get_object_or_404(Show, id=id, slug=slug)
    if request.method == "POST":
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.tvshow_id = tvshows
            comment.save()
            print("Test1")
            return redirect('tvshow_details', id=tvshows.id, slug=tvshows.slug)
    else:
        print("Test2")
        form = CommentsForm()
    return render(request, 'detail.html', {'tvshows': tvshows}, )


@login_required
def comment_accept(request, id):
    comment = get_object_or_404(Comment, id=id)
    tvshow = comment.tvshow_id
    comment.accept()
    return redirect('tvshow_details', id=tvshow.id, slug=tvshow.slug)


@login_required
def comment_delete(request, id):
    comment = get_object_or_404(Comment, id=id)
    tvshow = comment.tvshow_id
    comment.delete()
    return redirect('tvshow_details', id=tvshow.id, slug=tvshow.slug)

