from .models import Show, Comment, Article
from django import forms


class TvshowForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = ['image', 'title', 'description', 'category', 'status', 'episodes_no', 'series_no',
                  'aired_from', 'aired_to']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['image', 'title', 'text']
