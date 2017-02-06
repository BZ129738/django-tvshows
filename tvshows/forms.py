from django import forms

from .models import  Show, Category, Comment


class TvshowForm(forms.ModelForm):

    class Meta:
        model = Show
        fields = ['image', 'title','description', 'category', 'status', 'episodes_no', 'series_no',
                  'aired_from', 'aired_to']