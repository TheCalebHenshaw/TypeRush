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

class EditProfileForm(forms.ModelForm):
    firstname = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    country = forms.Select()
    profile_picture = forms.ImageField(required=False)
    class Meta:
        model = Player
        fields = ('firstname','surname','country','profile_picture',)
    
    def __init__(self,*args,**kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        custom_ids = {
            'firstname' : 'firstname',
            'surname' : 'surname',
            'country' : 'country',
            'profile_picture' : 'profile_picture',
        }
        for field_name, custom_id in custom_ids.items():
            self.fields[field_name].widget.attrs['id'] = custom_id


class EditUserForm(forms.ModelForm):
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

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data["password"]
        user.set_password(password)
        if commit:
            user.save()
        return user