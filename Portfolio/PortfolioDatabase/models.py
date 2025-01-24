from django.db import models

# Create your models here.

class Hobby(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()

    def __str__(self):
        return self.name