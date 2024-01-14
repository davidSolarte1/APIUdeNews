from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    img   = models.ImageField(upload_to='news/', blank=True, null=True)
    date  = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news')