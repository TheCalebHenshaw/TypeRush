from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Mode, Game, Player, GameResult
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from .forms import UserForm, UserProfileForm,EditProfileForm,EditUserForm
from .models import Game
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def home(request):
    user_instance = request.user
    return render(request, 'typerush/home.html', {'user_instance': user_instance})

def get_games(mode):

    try:
        top_games = Game.objects.filter(mode=mode).order_by('-score')[:10]
        return top_games
    except Exception as e:
        print(f"Error fetching games: {e}")
        return Game.objects.none()
    

def leaderboard(request):
    mode = 1 # default
    top_games = get_games(mode)
    
    try:
        user_instance = Player.objects.get(user=request.user)
    except:
        user_instance = None
    
    return render(request, 'typerush/leaderboard.html', {'top_games': top_games, 'mode':mode, 'user_instance': user_instance})

@csrf_exempt
def update_leaderboard(request):
    mode = request.POST.get('mode')
    request.session['mode'] = mode

    top_games = get_games(mode)
    print(top_games)
    # Prepare the data to be returned in JSON format
    leaderboard_data = []
    for game in top_games:
        leaderboard_data.append({
            'user': game.user.user.username,
            'score': game.score,
            'profile_picture': game.user.profile_picture.name
            })
    # print(leaderboard_data)
    # Return the leaderboard data as JSON response
    return JsonResponse({'top_games': leaderboard_data})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('typerush:home'))  # Redirect to home page after successful login
            else:
                return HttpResponse("Your TypeRush account is disabled.")
        else:
            error = "Invalid login details supplied."
            return render(request, 'typerush/login.html', {'error_message': error})
    else:
        return render(request, 'typerush/login.html')

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
            profile.country = request.POST.get('country')

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'typerush/register.html' ,
                  context= {'user_form' : user_form,
                            'profile_form' : profile_form,
                            'registered' : registered })

@login_required
def user_logout(request):
    logout(request)
    return redirect('typerush:home')

@login_required
def profile(request):
    player = Player.objects.get(user=request.user)
    return render(request, 'typerush/profile.html', {'player' : player})

@login_required
def edit_profile(request):
    user = request.user
    player = request.user.player

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=player)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('typerush:user_login'))
    else:
        user_form = EditUserForm(instance=user)
        profile_form = UserProfileForm(instance=player)
        user_form.fields['password'].initial = None

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'player':player,
    }
    return render(request, 'typerush/edit_profile.html', context)



@login_required(login_url='/typerush/login/')
# will add the correct context dictionary when i have better idea of how game is implemented
def game_view(request):
    return render(request, 'typerush/game.html')


@csrf_exempt
def get_json_data(request):
    mode = request.POST.get('mode')
    json_file_path = f'static/data/{mode}.json'

    try:
        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
        return JsonResponse(json_data)
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=500)

    
def selecting_mode(request):
    return render(request,'typerush/selecting_mode.html')

@csrf_exempt
def save_game_results(request):
    if request.method == 'POST':
        correct = request.POST.get('correct', 0)
        wrong = request.POST.get('wrong', 0)

        GameResult.objects.create(correct = correct , wrong = wrong)

        return JsonResponse({'status' : 'success'})
    
    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'}, status=405)

def page_not_found_view(request):
    return render(request, 'typerush/404.html', {})