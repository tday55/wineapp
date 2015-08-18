from django.db import models

# Create your models here.

class Wine(models.Model):
    def __str__(self):              # __unicode__ on Python 2
        return self.vineyard + ' ' + self.varietal + ' ' + self.vintage
    vineyard = models.CharField(max_length=200)
    varietal = models.CharField(max_length=200)
    vintage = models.CharField(max_length=10)
    acquisition_date = models.DateTimeField('date acquired')

class Tasting(models.Model):
    def __str__(self):
        return self.wine
    wine = models.ForeignKey(Wine)
    rating = models.IntegerField(default=0) 