from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)


    def __str__(self):
        return '%s' % self.name


class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    #slug = models.SlugField(max_length=145,unique=True)
    image = models.ImageField(null=True,blank=True,upload_to='static/images/')
    category = models.ForeignKey(Category,default='Blog',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.title


    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk' : self.pk})

    # def _get_unique_slug(self):
    #
    #     #slug = slugify(self.title)
    #     unique_slug = self
    #     if Entry.objects.filter(slug=unique_slug).exists():
    #         #raise ValueError('Entry with this title already exists')
    #         print("Slug Exists")
    #         slug = unique_slug
    #     else:
    #         slug = slugify(self.title)
    #
    #     #while Entry.objects.filter(slug=unique_slug).exists():
    #     #    unique_slug = '{}-{}'.format(slug, num)
    #     #    num += 1
    #     return slug

    # def save(self, *args, **kwargs):
    #     print("This is the models idea of what the slug is: ",self)
    #     if not self.slug:
    #         self.slug = self._get_unique_slug()
    #
    #     super().save()

