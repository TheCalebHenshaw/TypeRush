import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'typerush_project.settings')

import django
django.setup()
from typerush.models import Player,Mode,Leaderboard,Game
from django.contrib.auth.models import User



def populate():
 # Create users
    user1 = User.objects.create_user(username='user1', password='password1')
    user2 = User.objects.create_user(username='user2', password='password2')
    #user3 = User.objects.create_user(username=)
    # Populate Player model
    player1 = Player.objects.create(user=user1, firstname='John', surname='Doe', country='USA', total_races=10, average_speed=50, rank=1)
    player2 = Player.objects.create(user=user2, firstname='Jane', surname='Smith', country='Canada', total_races=8, average_speed=45, rank=2)

    # Populate Leaderboard model
    leaderboard = Leaderboard.objects.create(title='Main Leaderboard')
    leaderboard.players.add(player1, player2)

    # Populate Mode model
    mode = Mode.objects.create(difficulty='Easy', races_played=20, highscore=100, leaderboard=leaderboard)

    # Populate Game model
    game1 = Game.objects.create(mode=mode, userID=player1, score=80)
    game2 = Game.objects.create(mode=mode, userID=player2, score=75)

    print("Database populated successfully.")







#Main Method Execution
if __name__ == '__main__':
    print("Starting TypeRush Population Script...")
    populate()
