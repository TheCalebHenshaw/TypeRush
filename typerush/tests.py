from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from typerush.models import Player, Leaderboard, Mode, Game
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from typerush.models import Mode, Game, Player






class PlayerModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.player = Player.objects.create(user=self.user, firstname='John', surname='Doe', country='USA')

    def test_player_str(self):
        self.assertEqual(str(self.player), 'testuser')

    def test_player_slug(self):
        self.assertEqual(self.player.slug, 'testuser')

    def test_leaderboard_str(self):
        leaderboard = Leaderboard.objects.create(title='Test Leaderboard')
        self.assertEqual(str(leaderboard), 'Test Leaderboard')

    def test_mode_str(self):
        leaderboard = Leaderboard.objects.create(title='Test Leaderboard')
        mode = Mode.objects.create(difficulty='Easy', leaderboard=leaderboard)
        self.assertEqual(str(mode), 'Easy')

class GameModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.player = Player.objects.create(user=self.user, firstname='John', surname='Doe', country='USA')
        self.leaderboard = Leaderboard.objects.create(title='Test Leaderboard')
        self.mode = Mode.objects.create(difficulty='Easy', leaderboard=self.leaderboard)
        self.game = Game.objects.create(mode=self.mode, user=self.player, score=100)

    def test_game_str(self):
        self.assertEqual(str(self.game), 'testuser: Easy score: 100')





class RegistrationTestCase(TestCase):
    def test_valid_registration(self):
        response = self.client.post(reverse('typerush:register'), {
            'username': 'newuser',
            'password': 'newpassword123',
            'firstname': 'New',
            'surname': 'User',
            'country': 'CountryName',  

        })
        self.assertEqual(response.status_code, 200)  
        self.assertTrue(User.objects.filter(username='newuser').exists())
    
    def test_invalid_registration(self):
        response = self.client.post(reverse('typerush:register'), {
            'username': 'existinguser',
            'password': 'newpassword123',
          
        }, follow=True)  

   
        self.assertEqual(response.status_code, 200)  

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_login_success(self):
        response = self.client.post(reverse('typerush:user_login'), {'username': 'testuser', 'password': 'testpassword123'})
        self.assertRedirects(response, reverse('typerush:home'))

    def test_login_failure(self):
        response = self.client.post(reverse('typerush:user_login'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "Invalid login")  

class LogoutTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_logout(self):
        response = self.client.get(reverse('typerush:user_logout'))
        self.assertRedirects(response, reverse('typerush:home'))  
        self.assertNotIn('_auth_user_id', self.client.session)