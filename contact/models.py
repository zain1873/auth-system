from django.db import models

# Create your models here.

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=50, default="No Subject")
  message = models.TextField()

  def __str__(self):
    return self.name