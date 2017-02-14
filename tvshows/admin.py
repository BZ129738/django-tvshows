from django.contrib import admin
from models import Show,Category, Article
# Register your models here.

# Admin panel superuser:
# U : admin
# P : zaq12wsx

def make_published(modeladmin, request, queryset):
    queryset.update(accepted='True')
make_published.short_description = "Approve selected TV Shows"

class ShowAdmin(admin.ModelAdmin):
    fields = ['accepted','image', 'title','slug','description', 'category' ,'status','episodes_no','series_no', 'aired_from', 'aired_to']
    list_display = ['accepted', 'title', 'get_category' ,'status','episodes_no','series_no', 'aired_from', 'aired_to']
    list_filter = ['status', 'category', 'accepted']
    list_editable = ['title', 'status','episodes_no','series_no']
    prepopulated_fields = {'slug': ('title',)}
    actions = [make_published]

admin.site.register(Show, ShowAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','tvshow','image','text']
    list_display = ['id','title']

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()

admin.site.register(Article, ArticleAdmin)