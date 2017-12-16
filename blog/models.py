from django.db import models
from django.contrib.auth.models import User

from mysite.fulltext import SearchManager

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    slug = models.SlugField()



    def __str__(self):
        return '%s' % self.name


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField()
    image = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = SearchManager(['title','body'])


    def __str__(self):
        return '%s' % self.title


    def __unicode__(self):
        return '%s' % self.title





