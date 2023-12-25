from django.db import models
from categories.models import category
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
  title = models.CharField("Title", max_length=50)
  content = models.TextField("content")
  category = models.ManyToManyField(category) # Ekta post e multiple category thakte  pare & 
  author = models.ForeignKey(User,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='posts/media/',blank=True,null=True)
  def __str__(self):
    return self.title
  


  

class Comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"
        