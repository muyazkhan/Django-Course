from django.db import models
from categories.models import category
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
  title = models.CharField("Title", max_length=50)
  content = models.TextField("content")
  category = models.ManyToManyField(category) # Ekta post e multiple category thakte  pare & 
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  def __str__(self):
    return self.title