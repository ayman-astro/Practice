from django.db import models
from musician.models import Musician


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=50)
    release_date = models.DateField(null=True, blank=True)
    CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    rating = models.IntegerField(choices=CHOICES)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.name}"
