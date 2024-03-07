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
    user3 = User.objects.create_user(username='user3',password='password3')
    user4 = User.objects.create_user(username='user4',password='password4')
    user5 = User.objects.create_user(username='user5',password='password5')
    user6 = User.objects.create_user(username='user6',password='password6')
    user7 = User.objects.create_user(username='user7',password='password7')
    user8 = User.objects.create_user(username='user8',password='password8')
    # Populate Player model
    player1 = Player.objects.create(user=user1, firstname='John', surname='Doe', country='USA', total_races=10, average_speed=50)
    player2 = Player.objects.create(user=user2, firstname='Jane', surname='Smith', country='Canada', total_races=8, average_speed=45)

    # Populate Leaderboard model
    easyleaderboard = Leaderboard.objects.create(title='Easy Leaderboard')
    mediumleaderboard = Leaderboard.objects.create(title='Medium Leaderboard')
    hardleaderboard = Leaderboard.objects.create(title='Hard Leaderboard')

    easyleaderboard.players.add(player1, player2)

    # Populate Mode model
    easyMode = Mode.objects.create(difficulty='Easy', races_played=20, highscore=50, leaderboard=easyleaderboard)
    mediumMode = Mode.objects.create(difficulty='Medium',races_played=17,highscore=33,leaderboard=mediumleaderboard)
    hardMode = Mode.objects.create(difficulty='Hard', races_played=15,highscore=22,leaderboard=hardleaderboard)
    # Populate Game model
    game1 = Game.objects.create(mode=mode, userID=player1, score=80)
    game2 = Game.objects.create(mode=mode, userID=player2, score=75)

    print("Database populated successfully.")







#Main Method Execution
if __name__ == '__main__':
    print("Starting TypeRush Population Script...")
    populate()
