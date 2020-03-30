from django.db import models

# Create your models here.
class Doggarden(models.Model):
    name = models.CharField(max_length=50)
    size = models.FloatField()
    street = models.CharField(max_length=50)
    slug = models.SlugField()
    thumb = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.name + ' - ' + self.street