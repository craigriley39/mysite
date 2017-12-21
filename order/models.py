from django.db import models

import datetime
# model definition
# order
# shipment
# items
# pricing_line


# an order can have shipments, shipments can have items. Each item has a price (part of the model),
# an order has a shipment, a shipment has an item
# item - item_id, item_description, item_price,item_length,item_width, item_depth
# order has item(s), order_id
#
# customer - customer_id,customer_first_name,customer_last_name
# address - customer_id,
# Create your models here.


from django.db import models

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Customer(models.Model):
    CUSTOMER_STATUS = [
        ('OPEN','OPEN'),
        ('CLOSED','CLOSED'),
        ('HOLD','HOLD'),
    ]
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    customer_id = models.CharField(max_length=32)
    customer_status = models.CharField(max_length=10,choices=CUSTOMER_STATUS,default='OPEN')
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.company_name


    def __unicode__(self):
        return '%s' % self.company_name

    def save(self,*args,**kwargs):

        if not self.pk:
            try:
                last_id = Customer.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Customers yet')
                next_id = 1

            print("Value of the next_id is" , next_id)
            self.customer_id = 'CUS' + str(next_id).zfill(6)



        super(Customer,self).save(*args,**kwargs)




class Contact(models.Model):

    CONTACT_TYPE = [
        ('BILLING','Billing'),
        ('SHIPPING','Shipping'),

    ]
    id = models.AutoField(primary_key=True)
    contact_id = models.CharField(max_length=32)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    primary_email = models.EmailField()
    phone = models.CharField(max_length=32)
    contact_type = models.CharField(max_length=32,choices=CONTACT_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.contact_id

    def __unicode__(self):
        return '%s' % self.contact_id

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Customer.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Customers yet')
                next_id = 1


            self.contact_id = 'CONTACT' + str(next_id).zfill(6)

            super(Contact, self).save(*args, **kwargs)


class Address(models.Model):
    ADDRESS_TYPE = [
        ('SHP','SHIP_TO'),
        ('BILL','BILLING'),
    ]

    id = models.AutoField(primary_key=True)
    address_id = models.CharField(max_length=32)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address_type = models.CharField(max_length=6,choices=ADDRESS_TYPE)
    address_1 = models.CharField(max_length=32)
    address_2 = models.CharField(max_length=32,blank=True,null=True)
    city = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    country = models.CharField(max_length=32)
    zipcode = models.CharField(max_length=32)
    primary = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.address_id


    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Address.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Addresses yet')
                next_id = 1


            self.address_id = 'ADDR' + str(next_id).zfill(6)

            super(Address, self).save(*args, **kwargs)




#### Tax rates by zipcode
#State	ZipCode	TaxegionName
## StateRate	EstimatedCombinedRate	EstimatedCountyRate
# EstimatedCityRate	EstimatedSpecialRate	RiskLevel

class TaxRateByZip(models.Model):
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=12)
    tax_region_name = models.CharField(max_length=120)
    state_rate = models.FloatField(max_length=10)
    est_combined_rate = models.FloatField(max_length=10)
    est_county_rate = models.FloatField(max_length=10)
    est_city_rate = models.FloatField(max_length=10)
    est_special_rate = models.FloatField(max_length=10)


    def __str__(self):
        return '%s' % self.est_combined_rate

# an order contains one or more products
# each prodcut has a category of service

class Order(models.Model):
    ORDER_STATUS = [
        ('OPEN', 'OPEN'),
        ('HOLD','HOLD'),
        ('CLOSED', 'CLOSED')
        ]
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=32)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_status = models.CharField(choices=ORDER_STATUS, max_length=32)
    order_date = models.DateTimeField(default=datetime.datetime.now())
    order_fulfill_date = models.DateTimeField(datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE )


    @property
    def order_duration(self):
        order_duration = self.order_date - self.order_fulfill_date
        return order_duration
    # This model should have a few propertys defined
    # total order amount
    # delta between order_date and order_fulfill_date = order_duration
    # order fufil date
    # combined tax rate, city state taxes , etc

    def __str__(self):
        return '%s' % self.order_id



    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Order.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Orders yet')
                next_id = 1


            self.order_id = 'ORD' + str(next_id).zfill(6)

            super(Order, self).save(*args, **kwargs)






class Category(models.Model):


    TRANSACTION_TYPES = [
        ('SHIPMENT', 'SHIPMENT'),
        ('HOMESALE','HOMESALE'),
        ('SOMETHING', 'Something else'),
    ]
    category_group_id = models.CharField(max_length=32)
    category_group_name = models.CharField(max_length=32)
    transaction_type = models.CharField(max_length=12,choices=TRANSACTION_TYPES)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return '%s' % self.category_group_name


    def __unicode__(self):
        return '%s' % self.category_group_id



    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Category.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Categories yet')
                next_id = 1

            self.product_id = 'CAT' + str(next_id).zfill(6)

            super(Category, self).save(*args, **kwargs)


class Product(models.Model):

    category_group_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=64)
    product_id = models.CharField(max_length=32,primary_key=True)
    cost = models.FloatField()
    sell_for_amount = models.FloatField(max_length=10)
    est_tax_amount = models.FloatField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                last_id = Product.objects.latest('created')
                next_id = last_id.id + 1
            except ObjectDoesNotExist:
                print('No Products yet')
                next_id = 1

            self.product_id = 'PRD' + str(next_id).zfill(6)

            super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' % self.product_name

    def __str__(self):
        return '%s' % self.product_name