from django import forms
from rango.models import Page,Category
from django.contrib.auth.models import User
from rango.models import UserProfile
from typerush.models import Player

class UserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    country = forms.Select()
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = Player
        fields = ('firstname','lastname','country','profile_picture',)

class EditUserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)
class EditPlayerProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField()
    class Meta:
        model = Player
        fields = ('profile_picture',)

