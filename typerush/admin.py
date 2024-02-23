from django.contrib import admin
from typerush.models import Player, Leaderboard, Mode, Game


# Register your models here.
admin.site.register(Player)
admin.site.register(Leaderboard)
admin.site.register(Mode)
admin.site.register(Game)