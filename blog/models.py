from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    slug = models.SlugField(max_length=145,unique=True)


    def __str__(self):
        return '%s' % self.name


class Entry(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=145,unique=True)
    image = models.ImageField(null=True,blank=True,upload_to='static/images/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.title


    def __unicode__(self):
        return '%s' % self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Entry.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super().save()

