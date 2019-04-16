
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PlayerForm
from .models import Player


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
