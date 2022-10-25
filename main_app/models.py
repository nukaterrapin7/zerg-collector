from django.db import models
from django.urls import reverse

# Create your models here.

class Zerg(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    minerals = models.IntegerField()
    vespene = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absollute_url(self):
        return reverse('detail', kwargs={'zerg_id': self.id})