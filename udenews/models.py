from django.db import models
from django.urls import reverse
# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    img   = models.ImageField(upload_to='news/', verbose_name='Imagen', blank=True, null=True)
    date  = models.DateField(blank=True, verbose_name='Fecha', null=True)
    place = models.CharField(max_length=100, verbose_name='Lugar', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('news')