from tkinter import CASCADE
from unicodedata import category
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import User

class Category(models.Model):
  category =models.CharField(max_length=20)

  def __str__(self):
      return self.category

class Post(models.Model):
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  title =models.CharField(max_length=20)
  image = CloudinaryField('image')
  video = CloudinaryField('video')
  content =models.TextField
  time_posted =models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  likes = models.IntegerField(default=0)

  


  def __str__(self):
      return self.category


  
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Likes(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Profile(models.Model):
    name = models.ForeignKey(User, on_delete=models.Cascade)
    avatar = CloudinaryField('image')
    category =models.ForeignKey(Category, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    