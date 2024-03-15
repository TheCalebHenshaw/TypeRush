from django import forms
from rango.models import Page,Category
from django.contrib.auth.models import User
from rango.models import UserProfile
from typerush.models import Player

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('firstname','surname','country','profile_picture',)

class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username','password',)
class EditPlayerProfileForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('profile_picture')

