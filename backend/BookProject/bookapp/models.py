from django.db import models


def upload_image(instance,filename):
    return "uploads/{title}/{filename}".format(title=instance.title,filename = filename)




    


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10,blank=True)
    isbn_13 = models.CharField(max_length=13,blank=True)
    
    def __str__(self):
        return self.isbn_10



class Book(models.Model):
    title        = models.CharField(max_length = 36,blank = False,unique = True)
    description  = models.TextField(max_length = 256,blank = True)
    price        = models.DecimalField(default = 0,max_digits=6,decimal_places=2) 
    published    = models.DateField()
    is_published = models.BooleanField(default=False) 
    cover        = models.ImageField(upload_to=upload_image,null=True,blank=True)
    number       = models.OneToOneField(BookNumber,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name = "character")
    
    def __str__(self):
        return self.name
    

class Author(models.Model):
    ''' One author might have multiple book
        One book might have  multiple author
    '''
    name    = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books   = models.ManyToManyField(Book,related_name='author')