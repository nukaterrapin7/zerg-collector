from django.db import models
from django.urls import reverse

ABSORBTIONS = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

# Create your models here.

class Zerg(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    minerals = models.IntegerField()
    vespene = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'zerg_id': self.id})

class Essence(models.Model):
    date = models.DateField('absorbtion date')
    amount = models.CharField(
        max_length=1,
        choices=ABSORBTIONS,
        default=ABSORBTIONS[0][0]
    )

    zerg = models.ForeignKey(Zerg, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_absorbtion_display()} on {self.date}"