from django.urls import path
from typerush import views

app_name = 'typerush'

urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('game/', views.game_view,name='game'),
    path('update_leaderboard/', views.update_leaderboard, name='update_leaderboard'),
    path('select-mode/', views.selecting_mode, name='selecting_mode'),
]