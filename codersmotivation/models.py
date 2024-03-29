# from tkinter import CASCADE
from django.db import models
from cloudinary.models import CloudinaryField
from authentication.models import User

class Category(models.Model):
  category =models.CharField(max_length=20)

  def __str__(self):
      return self.category

class Post(models.Model):
  category = models.ForeignKey(Category,related_name='post_category', on_delete=models.CASCADE)
  title =models.CharField(max_length=20)
  image = CloudinaryField('image')
  video = CloudinaryField('video')
  content =models.TextField()
  time_posted =models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey(User,related_name='post_author', on_delete=models.CASCADE)
  like = models.IntegerField(default=0)

  
  objects = models.Manager()

  def likes_count(self):
       return self.like.all().count()


  def __str__(self):
      return self.title


  
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(User,related_name="commented_by", on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment, self.name)



