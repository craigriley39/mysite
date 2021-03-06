from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify


from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys



class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255)


    def __str__(self):
        return '%s' % self.name



def upload_image_to(instance, filename):
    import os
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s' % (
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),
    )


class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    #slug = models.SlugField(max_length=145,unique=True)
    image = models.ImageField(null=True,blank=True,upload_to=upload_image_to)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.title


    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk' : self.pk})

    def save(self,*args, **kwargs):
        # Opening the uploaded image
        if self.image:


            im = Image.open(self.image)

            output = BytesIO()

            # Resize/modify the image
            im = im.resize((750, 300),Image.NEAREST)

            # after modifications, save it to the output
            im.save(output, format='JPEG', quality=40)
            output.seek(0)

        # change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
                                        sys.getsizeof(output), None)

        super(Entry, self).save(*args, **kwargs)
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

