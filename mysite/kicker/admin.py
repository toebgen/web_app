from django.contrib import admin

from .models import Game, Player


class PlayerAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class GameAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
