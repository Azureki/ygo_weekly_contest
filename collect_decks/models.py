from django.db import models


class FileModel(models.Model):
    file = models.FileField(upload_to='decks/')
    name = models.CharField(max_length=30)
    
