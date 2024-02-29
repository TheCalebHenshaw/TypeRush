from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Mode, Game
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import UserForm, UserProfileForm



# Create your views here.
def home(request):
    return render(request, 'typerush/home.html', {})
from .models import Player

def leaderboard(request):
    modes = Mode.objects.all()
    top_games_by_mode = {}
    for mode in modes:
        top_games = Game.objects.filter(mode=mode).order_by('-score')[:10]
        top_games_by_mode[mode] = top_games
    return render(request, 'typerush/leaderboard.html', {'top_games_by_mode': top_games_by_mode})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect(reverse('typrush:home'))
            else:
                return HttpResponse("Your typerush account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'typerush/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('typerush:home'))

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'typerusj/register.html' ,
                  context= {'user_form' : user_form,
                            'profile_form' : profile_form,
                            'registered' : registered })

