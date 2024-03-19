from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError('Username "%s" is already in use.' % username)
        except User.DoesNotExist:
            return username

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
    # Assuming 'country' is a model choice field. You'll need to define the choices correctly.
    country = forms.Select()
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = Player
        fields = ('firstname', 'surname', 'country', 'profile_picture',)

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        custom_ids = {
            'firstname': 'firstname',
            'surname': 'surname',
            'country': 'country',
            'profile_picture': 'profile_picture',
        }
        for field_name, custom_id in custom_ids.items():
            self.fields[field_name].widget.attrs['id'] = custom_id



class EditUserForm(forms.ModelForm):
    username = forms.CharField(required=True)
    # Declare the password field using forms.PasswordInput, ensuring it doesn't pre-fill
    password = forms.CharField(widget=forms.PasswordInput(), required=False, label="New password")

    class Meta:
        model = User
        fields = ('username',)  # Do not include the 'password' field here

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        # Remove the 'password' field from being rendered with initial data
        self.fields['password'].initial = None

    def save(self, commit=True):
        user = super().save(commit=False)
        # Set the password only if it's provided
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user