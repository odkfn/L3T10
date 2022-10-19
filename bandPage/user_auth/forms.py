from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    '''
    This class creates the SignUpForm.

    The form is used to permit new users to sign up to the website.

    :param str first-name: The users first name
    :param str username: The username selected by the user
    :param str password1: The password selected by the user
    :param str password2: The password selected by the user a second time for verification purposes

    :returns: The title of the post
    :rtype: str
    
    '''
    first_name = forms.CharField(max_length=30, required=True, help_text='Optional.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2', )
