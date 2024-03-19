from django import forms
from django.contrib.auth.models import User
from typerush.models import Player

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # Dictionary mapping field names to custom IDs
        custom_ids = {
            'username': 'username',
            'password': 'password',
        }
        # Assign custom IDs to form fields
        for field_name, custom_id in custom_ids.items():
            self.fields[field_name].widget.attrs['id'] = custom_id

    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'password',)

class UserProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        # Dictionary mapping field names to custom IDs
        custom_ids = {
            'firstname': 'firstname',
            'surname': 'surname',
            'country': 'country',
            'profile_picture': 'profile_picture',
        }
        # Assign custom IDs to form fields
        for field_name, custom_id in custom_ids.items():
            self.fields[field_name].widget.attrs['id'] = custom_id
    
    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    country = forms.Select()
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = Player
        fields = ('firstname','surname','country','profile_picture',)

class EditUserForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username','password',)
class EditPlayerProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField()
    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    country = forms.Select()
    class Meta:
        model = Player
        fields = ('firstname','surname','country','profile_picture',)

