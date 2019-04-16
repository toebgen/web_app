from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Player


def index(request):
    latest_player_list =  Player.objects.order_by('-join_date')[:5]
    context = {'latest_player_list': latest_player_list}
    output = ', '.join([p.name for p in latest_player_list])
    return render(request, 'kicker/index.html', context)


def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'kicker/player.html', {'player': player})
