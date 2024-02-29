from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    # includes username and password
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    country = models.CharField(max_length = 128)
    profile_picture = models.ImageField(upload_to='profile_images', blank=True)
    total_races = models.IntegerField(default=0) 
    average_speed = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.user.username

class Leaderboard(models.Model):
    title = models.CharField(max_length = 128)
    players = models.ManyToManyField(Player)
    
    def __str__(self):
        return self.title


class Mode(models.Model):
    difficulty = models.CharField(max_length = 18)
    races_played= models.IntegerField(default=0)
    highscore = models.IntegerField(default=0)

    # associated leaderboard
    leaderboard = models.ForeignKey(Leaderboard, on_delete=models.CASCADE)

    def __str__(self):
        return self.difficulty

# stores all game instances, filter by mode to display on leaderboard, 
# get top 10 scores after sorting by descending order
class Game(models.Model):
    mode = models.ForeignKey(Mode, on_delete = models.CASCADE)
    userID = models.OneToOneField(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return (self.userID + ": " + self.difficulty + " score: " + self.current_score)
    

    



