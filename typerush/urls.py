from django.urls import path
from typerush import views

app_name = 'typerush'

urlpatterns = [
    path('', views.home, name='home'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]