from django.test import TestCase
from django.test import TestCase
from django.contrib.auth.models import User
from typerush.models import Player, Leaderboard, Mode, Game
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from typerush.models import Mode, Game, Player

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.player = Player.objects.create(user=self.user, firstname='John', surname='Doe', country='USA')
        self.mode = Mode.objects.create(difficulty='Easy')
        self.game = Game.objects.create(mode=self.mode, user=self.player, score=100)

    def test_home_view(self):
        response = self.client.get(reverse('typerush:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/home.html')

    def test_leaderboard_view(self):
        response = self.client.get(reverse('typerush:leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/leaderboard.html')

    def test_update_leaderboard_view(self):
        response = self.client.post(reverse('typerush:update_leaderboard'), {'mode': self.mode.pk})
        self.assertEqual(response.status_code, 200)
        leaderboard_data = response.json().get('top_games')
        self.assertEqual(len(leaderboard_data), 1)
        self.assertEqual(leaderboard_data[0]['user'], 'testuser')
        self.assertEqual(leaderboard_data[0]['score'], 100)

    def test_login_view(self):
        response = self.client.post(reverse('typerush:login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('typerush:home')))

    def test_register_view(self):
        response = self.client.get(reverse('typerush:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/register.html')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('typerush:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('typerush:home')))

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('typerush:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/profile.html')

    def test_edit_profile_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('typerush:edit_profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/editprofile.html')

    def test_game_view(self):
        response = self.client.get(reverse('typerush:game_view'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'typerush/game.html')







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



