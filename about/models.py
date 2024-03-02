from django.db import models

# Create your models here.

class About (models.Model):
    title = models.CharField()
    content = models.TextField()
    publiched_on = models.DateTimeField(auto_now_add=True)
