from django.db import models

# Create your models here.
class Album(models.Model):
  name = models.CharField(max_length=200)
  artist = models.CharField(max_length=200)
  date_released = models.DateField(null=True, blank=True)

  def __str__(self):
    return f'{self.name}'