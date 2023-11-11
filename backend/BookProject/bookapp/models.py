from django.db import models


def upload_image(instance,filename):
    return "uploads/{title}/{filename}".format(title=instance.title,filename = filename)


class Book(models.Model):
    title        = models.CharField(max_length = 36,blank = False,unique = True)
    description  = models.TextField(max_length = 256,blank = True)
    price        = models.DecimalField(default = 0,max_digits=6,decimal_places=2) 
    published    = models.DateField()
    is_published = models.BooleanField(default=False) 
    cover        = models.ImageField(upload_to=upload_image,null=True,blank=True)
    
