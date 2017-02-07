from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Show(models.Model):
    accepted = models.BooleanField(default=False)
    title = models.CharField(max_length=250, db_index=True)
    description = models.TextField(blank=True,null=True)
    category = models.ManyToManyField('tvshows.Category', related_name='shows')
    slug = models.SlugField(max_length=250, db_index=True,unique=True)
    image = models.ImageField(upload_to='cover/%Y/%m/%d', blank=True)
    AIR_STATUS = (
        (1, 'current show'),
        (2, 'ended / cancelled'),
        (3, 'on hiatus'),
    )
    status = models.IntegerField(default=1, choices=AIR_STATUS)
    episodes_no = models.IntegerField(default=1)
    series_no = models.IntegerField(default=1)
    aired_from = models.DateField(default=timezone.now)
    aired_to = models.DateField(blank=True,null=True)
    updated = models.DateField(auto_now=True)

    def get_category(self):
        return "\n, ".join([c.name for c in self.category.all()])

    def accept(self):
        self.accepted = True
        self.save()

    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('tvshows:tvshow_details', args=[self.id,self.slug])


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tvshows:list_by_category', args=[self.slug])


class Comment(models.Model):
    accepted = models.BooleanField(default=False)
    tvshow_id = models.ForeignKey('tvshows.Show', related_name='comments')
    author = models.ForeignKey(User)
    text = RichTextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def accept(self):
        self.accepted = True
        self.save()
