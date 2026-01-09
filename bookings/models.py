from django.db import models

# Create your models here.

class TableBooking(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  date = models.DateField()
  time = models.TimeField()
  persons = models.PositiveIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
    