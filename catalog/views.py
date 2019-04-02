from django.shortcuts import render, redirect, get_object_or_404
from catalog.models import *
from catalog.forms import PlayerScoreForm
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Sum, Count
from catalog.definitions import *

# Create your views here.

def Homepage (request):
    """View function for home page of site."""

    #Define views here
    
    
    context = {
    
    }

    #Render the HTML template homepage.html with the data in the context var
    return render(request, 'homePage.html', context=context)

def Formpage (request):
    """View function for form inputs and data display"""
    
    #VALIDATE PLAYER SETUP
    player_model = PlayerName.objects.all()
    active_players = PlayerName.objects.all().count()

    def player_setup():
        try:
            player1 = PlayerName.objects.get(number=1)
        except:
            player1 = 'None'

        try:
            player2 = PlayerName.objects.get(number=2)
        except:
            player2 = 'None'

        try:
            player3 = PlayerName.objects.get(number=3)
        except:
            player3 = 'None'

        return (player1, player2, player3)
    
    player1, player2, player3 = player_setup()

    #SCORE FORM INPUT
    if request.method =='POST':
        form = PlayerScoreForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('formpage')
    else:
        form = PlayerScoreForm()

    #VALIDATE SCORE MODELS
    def playerscore_setup():
        try:
            playerscore1 = list(PlayerScore.objects.aggregate(Sum('playerscore1')).values())[0]
        except:
            playerscore1 = 0
        try:        
            playerscore2 = list(PlayerScore.objects.aggregate(Sum('playerscore2')).values())[0]
        except:
            playerscore2 = 0
        try:
            playerscore3 = list(PlayerScore.objects.aggregate(Sum('playerscore3')).values())[0]
        except:
            playerscore3 = 0

        return (playerscore1, playerscore2, playerscore3)

    playerscore1, playerscore2, playerscore3 = playerscore_setup()

     #VALIDATE STABLEFORD MODELS
    def playerstableford_setup():
        try:
            playerstableford1 = list(PlayerStableford.objects.aggregate(Sum('playerstableford1')).values())[0]
        except:
            playerstableford1 = 0
        try:
            playerstableford2 = list(PlayerStableford.objects.aggregate(Sum('playerstableford2')).values())[0]
        except:
            playerstableford2 = 0
        try:
            playerstableford3 = list(PlayerStableford.objects.aggregate(Sum('playerstableford2')).values())[0]
        except:
            playerstableford3 = 0

        return (playerstableford1, playerstableford2, playerstableford3)

    playerstableford1, playerstableford2, playerstableford3 = playerstableford_setup()
    
    context = {
        'player_model': player_model,
        'player1': player1,
        'player2': player2,
        'player3': player3,
        'active_players': active_players,
        'playerscore1': playerscore1,
        'playerscore2': playerscore2,
        'playerstableford1': playerstableford1,
        'playerstableford2': playerstableford2,
        'form': form,
        }

    #Render the HTML template **pagename**.html with the data in the context variable
    return render(request, 'formPage.html', context=context)
