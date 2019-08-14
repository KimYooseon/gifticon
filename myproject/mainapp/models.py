from django.db import models

# Create your models here.


class category(models.Model):
    brand = models.CharField(max_length=20)
    item = models.CharField(max_length=20)
    originalprice = models.IntegerField(null=True)
    
    file = models.FileField(null=True)

    def __str__(self):
        return (str(self.brand)+''+str(self.item))


class brand_for_category(models.Model):
    brandname= models.CharField(max_length=20)

    def __str__(self):
        return self.brandname