from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=50, unique=True)

  def __str__(self):
    return self.name
    
class Movie(models.Model):
  name = models.CharField(max_length=50)
  year = models.IntegerField()
  rating = models.IntegerField()
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name