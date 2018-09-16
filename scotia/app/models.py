from django.db import models

# Create your models here.

class Provider(models.Model):
    # provider name
    name = models.CharField(max_length=255, null=False)
    # expiration date
    expiration_date = models.DateField(max_length=255, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.expiration_date)


class Product(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    # product price
    price = models.FloatField(max_length=255, null=False)
    # product ration points/COP
    ratio = models.FloatField(max_length=255, null=False)
    #product points
    points = models.FloatField(max_length=255, null=False)
    # status of product
    active = models.IntegerField(null=False)
    # expiration date
    expiration_date = models.DateField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.price, self.ratio, self.points, self.active, self.expiration_date)

class Customer(models.Model):
    # user name
    name = models.CharField(max_length=255, null=False)
    # user email
    email = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)

class Point(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # numer of points
    quantity = models.FloatField(max_length=255, null=False)
    # expiration date
    expiration_date = models.DateField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.quantity, self.expiration_date)

class Stock(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # number of elements
    quantity = models.FloatField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.quantity)

class Order(models.Model):
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    # quantity on the order
    quantity = models.IntegerField(null=False)
    # order status
    status = models.IntegerField(null=False)

    def __str__(self):
        return "{} - {}".format(self.status)
