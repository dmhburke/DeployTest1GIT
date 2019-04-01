from django import forms
from django.forms import ModelForm
from catalog.models import PlayerName, PlayerScore

class PlayerScoreForm(ModelForm):
   
    playerscore1 = forms.IntegerField(label='', required=False)
    playerscore2 = forms.IntegerField(label='', required=False)
    playerscore3 = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(PlayerScoreForm, self).__init__(*args, **kwargs)
        self.fields['playerscore1'].widget.attrs={'id': 'player1', 'class':'scoreInputField'}
        self.fields['playerscore2'].widget.attrs={'id': 'player2', 'class':'scoreInputField'}
        self.fields['playerscore3'].widget.attrs={'id': 'player3', 'class':'scoreInputField'}

    class Meta:
        model = PlayerScore
        fields = ('playerscore1', 'playerscore2', 'playerscore3',)
