from django.db import models

# Create your models here.
class category(models.Model):
    image = models.ImageField(upload_to='media/banner_img')
    name = models.CharField(max_length=100)
    Link = models.CharField(max_length=200, null=True, default = '')

    def __str__(self):
        return self.name

class special_offer(models.Model):
    image = models.ImageField(upload_to='media/specialOffer_img')
    name = models.CharField(max_length=100)
    Link = models.CharField(max_length=200, null=True, default = '')

    def __str__(self):
        return self.name


class carousal(models.Model):
    image = models.ImageField(upload_to='media/carousal_img') 
    Link = models.CharField(max_length=200, null=True, default = '')

class add1(models.Model):
    image = models.ImageField(upload_to='media/add_img') 
    Link = models.CharField(max_length=200, null=True, default = '')

class add2(models.Model):
    image = models.ImageField(upload_to='media/add_img') 
    Link = models.CharField(max_length=200, null=True, default = '')
