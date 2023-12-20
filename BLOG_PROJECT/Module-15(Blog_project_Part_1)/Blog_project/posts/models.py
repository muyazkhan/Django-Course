from django.db import models
from categories.models import category
from author.models import author

# Create your models here.
class post(models.Model):
  title = models.CharField("Title", max_length=50)
  content = models.TextField("content")
  category = models.ManyToManyField(category) # Ekta post e multiple category thakte  pare & 
  author = models.ForeignKey(author,on_delete=models.CASCADE)
  def __str__(self):
    return self.title