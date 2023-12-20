from django.db import models
from author.models import author
# Create your models here.

class profile(models.Model):
  name = models.CharField("Name", max_length=100)
  about = models.TextField("About")
  author = models.OneToOneField(author, on_delete=models.CASCADE,default=None)
  # bio = models.TextField("Bio")
  # phone_no = models.CharField("Phone Number")
  def __str__(self):
    return self.name