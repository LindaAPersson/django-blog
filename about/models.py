from django.db import models

# Create your models here.

class About (models.Model):
    title = models.CharField()
    content = models.TextField()
    published_on = models.DateTimeField(auto_now_add=True)
