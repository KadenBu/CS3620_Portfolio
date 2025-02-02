from django.db import models

# Create your models here.

class Hobby(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()
    image = models.CharField(max_length = 500, default = "https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png")

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length = 200)
    desc = models.TextField()
    image = models.CharField(max_length = 500, default = "https://www.contentviewspro.com/wp-content/uploads/2017/07/default_image.png")

    def __str__(self):
        return self.name