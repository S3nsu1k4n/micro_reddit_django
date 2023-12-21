from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  """Represents a post of a user

  Parameters
  ---------
  title : CharField
  body : TextField
  poster : ForeignKey(User)
  created_at : DateTime
  updated_at : DateTime
  """
  title = models.CharField(max_length=100, help_text='Title of the post', unique=True)
  body = models.TextField(max_length=1000)
  poster = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title + f'({self.id})'

  def get_absolute_url(self):
    return reverse('post-detail')


class Comment(models.Model):
  """ Represents a comment of a user

  Parameters
  ---------
  title : CharField
  body : TextField
  commenter : ForeignKey(User)
  post : ForeignKey(Post)
  created_at : DateTime
  updated_at : DateTime
  """
  title = models.CharField(max_length=100, help_text='Title of the comment', unique=True)
  body = models.TextField(max_length=1000)
  commenter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('comment-detail')