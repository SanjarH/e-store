from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()    

    class Meta:
        ordering = ('name',)
        

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    #description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['created_at']