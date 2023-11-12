from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator


class Movie(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    
    def __str__(self):
        return self.title
    

class Rating(models.Model):
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    
    def __str__(self):
        return str(self.stars)
    class Meta:
        unique_together = (('user','movie'),)
        index_together  = (('user','movie'),)
        
    
 