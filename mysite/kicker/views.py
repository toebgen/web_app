
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import GameForm, PlayerForm
from .models import Game, Player


def index(request):
    latest_player_list =  Player.objects.order_by('-join_date')[:50]
    context = {'latest_player_list': latest_player_list}
    output = ', '.join([p.name for p in latest_player_list])
    return render(request, 'kicker/index.html', context)


def player(request, player_id):
    player = get_object_or_404(Player, pk=player_id)
    return render(request, 'kicker/player.html', {'player': player})


def add_player(request):
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding)
        form = PlayerForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            player = form.save(commit=False)
            player.name = form.cleaned_data['name']
            player.join_date = timezone.now()
            player.save()

            # redirect to a new URL
            return render(request, 'kicker/player.html', {'player': player})

    else:
        # If this is a GET (or any other method) create the default form
        form = PlayerForm()
    
    # context = {
    #     'form': form,
    #     'player': player,
    # }

    return render(request, 'kicker/add_player.html', {'form': form})


def game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'kicker/game.html', {'game': game})


def add_game(request):
    if request.method == "POST":
        # Create a form instance and populate it with data from the request (binding)
        form = GameForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            game = form.save(commit=False)
            game.home_player_1 = form.cleaned_data['home_player_1']
            game.home_player_2 = form.cleaned_data['home_player_2']
            game.guest_player_1 = form.cleaned_data['guest_player_1']
            game.guest_player_2 = form.cleaned_data['guest_player_2']
            game.date = timezone.now()
            game.save()

            # redirect to a new URL
            return render(request, 'kicker/game.html', {'game': game})

    else:
        # If this is a GET (or any other method) create the default form
        form = GameForm()
    
    return render(request, 'kicker/add_game.html', {'form': form})
