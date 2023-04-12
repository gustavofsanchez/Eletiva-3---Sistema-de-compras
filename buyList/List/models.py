from django.db import models
#from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Supermarket(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class HistoricalPrice(models.Model):
    price = models.FloatField()
    timestamp = models.DateTimeField()
    promoTag = models.BooleanField()
    supermarket = models.ForeignKey(Supermarket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name + " - " + self.supermarket.name + " - " + str(self.price)

class List(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class List_product(models.Model):
    product = models.ForeignKey(Product,related_name='prod', on_delete=models.SET_NULL, null=True)
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    product_second_option = models.ForeignKey(Product, related_name='secondOption', on_delete=models.SET_NULL, null=True)
    importance = models.IntegerField()

    def __str__(self):
        return self.product.name  + " - " +  self.list.name

class TagRecipt(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Recipt(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    tagCategory = models.ForeignKey(TagRecipt, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class ProductRecipt(models.Model):
    product = models.ForeignKey(Product,related_name='prod_in_recipe', on_delete=models.SET_NULL, null=True)
    recipt = models.ForeignKey(Recipt, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name  + " - " +  self.recipt.name
