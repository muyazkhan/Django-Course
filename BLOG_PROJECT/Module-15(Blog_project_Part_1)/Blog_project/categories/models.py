from django.db import models

# Create your models here.
class category(models.Model):
  name = models.CharField("Name", max_length=100)
  # bio = models.TextField("Bio")
  # phone_no = models.CharField("Phone Number")
  def __str__(self):
    return self.name