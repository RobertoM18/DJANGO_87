from django.db import models
import datetime
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image= CloudinaryField('images')
    date = models.DateField(datetime.date.today)
    

# Create your models here.
