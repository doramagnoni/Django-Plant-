from django.db import models
from django.conf import settings

# Create your models here.
class Plant(models. Model):
    common_name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField()
    light_needs = models.CharField(max_length=50)
    water_needs = models.CharField(max_length=50)
    fertilization_notes = models.TextField(blank=True)  
    image = models.ImageField(upload_to='plant_images/', blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 