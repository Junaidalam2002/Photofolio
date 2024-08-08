from django.db import models

class Photographs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='items/')  # Assumes you have an 'items' folder in your media directory
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
