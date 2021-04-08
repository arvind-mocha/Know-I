from django.db import models

# Create your models here.
class Role(models.Model):
    position = models.CharField(max_length=50)
class Members(models.Model):
    name = models.CharField(max_length=30)
    position = models.ForeignKey(Role, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)
class Events(models.Model):
    e_title = models.CharField(max_length=30)
    e_content = models.TextField()
    e_image =  models.URLField(max_length=200)