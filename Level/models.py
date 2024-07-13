from django.db import models

# Create your models here.



class Level(models.Model):    
    level_name = models.CharField(max_length=100)    
    description = models.CharField(max_length=500)    
    image = models.ImageField(upload_to='images/', blank = True, null = True)    
    def __str__(self):        
        return self.level_name