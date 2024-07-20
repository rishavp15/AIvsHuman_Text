from django.db import models

# Create your models here.
class TextUpload(models.Model):
    text = models.CharField(max_length=1000)
    