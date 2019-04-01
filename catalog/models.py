from django.db import models
from django.urls import reverse

# Create your models here

class PlayerName(models.Model):
    """Record player details"""
    number = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    HC = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='playerimages', blank=True, null=True)

    def __str__(self):
        return self.name

class PlayerScore(models.Model):
    """Record player scores"""
    playerscore1 = models.IntegerField(blank=True, null=True)
    playerscore2 = models.IntegerField(blank=True, null=True)
    playerscore3 = models.IntegerField(blank=True, null=True)
    
