from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Journal(models.Model):
    title = models.CharField(max_length = 120)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    publish_date = models.DateTimeField()
    reviewed  = models.BooleanField(default = False)
    def __str__(self):
        return self.title

