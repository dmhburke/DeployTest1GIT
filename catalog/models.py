from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

class PlayerStableford(models.Model):
    """Convert score to stableford"""
    playerstableford1 = models.IntegerField(blank=True, null=True)
    playerstableford2 = models.IntegerField(blank=True, null=True)
    playerstableford3 = models.IntegerField(blank=True, null=True)


#STABLEFORD CONVERSION
par = 4
index = 17
player1HC = 21
player2HC = 16
stblford_two = 2

def stableford_conversion(par, index, HC, score):
        
    if HC >= index + 18:
        stblford_add = 2
    elif HC >= index:
        stblford_add = 1
    else:
        stblford_add = 0
    
    if score is None:
        score = 0        

    score_diff = par - score
    stableford_conversion = max(stblford_add + stblford_two + score_diff,0)

    return stableford_conversion

@receiver(pre_save, sender=PlayerScore)
def my_callback(sender, instance, **kwargs):

    convertedscore1 = stableford_conversion(par, index, player1HC, instance.playerscore1)
    convertedscore2 = stableford_conversion(par, index, player2HC, instance.playerscore2)
    
    stableford_scores = PlayerStableford(
        playerstableford1=convertedscore1,
        playerstableford2=convertedscore2,
        )
    stableford_scores.save()


