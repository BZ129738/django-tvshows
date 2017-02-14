from tvshows.models import Show, Category, Comment, Article

def get_cats(request):
    categories = Category.objects.all()
    return {
        'cats': categories
    }