from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads')
    desc = models.TextField()
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    profile = models.ImageField(upload_to='uploads')
    def __str__(self):
        return self.name