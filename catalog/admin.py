from django.contrib import admin
from catalog.models import PlayerName, PlayerScore, PlayerStableford

# Register your models here.
class PlayerNameAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'HC',)
    ordering = ('number',)

# Register the admin class with the associated model
admin.site.register(PlayerName, PlayerNameAdmin)

class PlayerScoreAdmin(admin.ModelAdmin):
    list_display = ('playerscore1', 'playerscore2', 'playerscore3',)

# Register the admin class with the associated model
admin.site.register(PlayerScore, PlayerScoreAdmin)

class PlayerStablefordAdmin(admin.ModelAdmin):
    list_display = ('playerstableford1', 'playerstableford2', 'playerstableford3',)

# Register the admin class with the associated model
admin.site.register(PlayerStableford, PlayerStablefordAdmin)
