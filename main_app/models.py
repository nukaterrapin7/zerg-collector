from django.db import models
from django.urls import reverse

ABSORBTIONS = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)

RACES = (
    ('T', 'Terran'),
    ('P', 'Protoss'),
    ('Z', 'Zerg'),
)

# Create your models here.

class Enemy(models.Model):
    name = models.CharField(max_length=50)
    race = models.CharField(max_length=1,
        choices=RACES,
        default=RACES[0][0]
        )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('enemies_detail', kwargs={'pk': self.id})


class Zerg(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    minerals = models.IntegerField()
    vespene = models.IntegerField()
    enemies = models.ManyToManyField(Enemy)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'zerg_id': self.id})

class Essence(models.Model):
    date = models.DateField('Absorbtion Date')
    absorbtions = models.CharField(
        max_length=1,
        choices=ABSORBTIONS,
        default=ABSORBTIONS[0][0]
    )

    zerg = models.ForeignKey(Zerg, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_absorbtions_display()} on {self.date}"

    class Meta:
        ordering = ['-date']