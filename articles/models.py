from django.db import models
from django.db.models import ImageField

# Create your models here.
class Article(models.Model):
  title = models.CharField(max_length=100, unique=True)
  author = models.CharField(max_length=100, unique=True)
  pub_date = models.DateTimeField('Date Published')
  category = models.CharField(max_length=100)
  hero_image = models.ImageField('Hero Image', upload_to='images/')
  additional_image = models.ImageField('Additional Image', upload_to='images/')
  body = models.TextField()

  def __str__(self):
    return self.title