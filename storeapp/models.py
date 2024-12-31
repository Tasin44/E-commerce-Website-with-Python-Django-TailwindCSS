from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=500)
    slug = models.SlugField(unique=True)#our urls will be make sense

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):#defination of string model so that we've proper human readable representation of our model
        return self.name


class Product(models.Model):
    #every product will have to belong a category lets create a one to many relationship between product and category where there are many categories and the product has to belong to them

    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    #if the category table deleted, the products belongs to this category will also be delated
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True)#we would like to allow blank to be true
    price = models.DecimalField(max_digits=10, decimal_places=2)#decimal_places means number after . like 3.45
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)#getting the time of adding a object or product
    updated = models.DateTimeField(auto_now=True)#the time of updation any product will also be added
    image = models.ImageField(upload_to='products', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('storeapp:product_detail', kwargs={'id':self.id, 'slug':self.slug})#kwargs is a dictionary
    #reverse will help us to generate a urls pattern based on the arguments we provide