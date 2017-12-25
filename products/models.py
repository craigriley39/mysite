from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class Product(models.Model):

    product_name = models.CharField(max_length=64)
    product_id = models.CharField(max_length=32)
    price = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Product.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                next_id = 1


            self.product_id = 'PRD' + str(next_id).zfill(6)

            super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.product_name

    def __str__(self):
        return '%s' % self.product_name