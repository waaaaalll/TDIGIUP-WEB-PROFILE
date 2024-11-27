from django.db import models

# Create your models here.
class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='project/images')

    def __str__(self):
        return self.title