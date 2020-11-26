from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, get_user_model, AuthenticationForm, UsernameField
from . models import UserDetails
from django.core.validators import RegexValidator



class CustomAuthForm(AuthenticationForm):
      username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
#-------------------------------------------------------------------------------

class UserRegisterForm(UserCreationForm):
    chars = RegexValidator(r'^[a-öA-Ö]*$', 'Only characters please')
    first_name = forms.CharField(max_length=30, validators=[chars])
    last_name = forms.CharField(max_length=30, validators=[chars])
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2', )

#-------------------------------------------------------------------------------

class EmailChangeForm(forms.ModelForm):
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ['email']
#-------------------------------------------------------------------------------

class DetailsChangeForm(forms.ModelForm):

    class Meta:
        model = UserDetails
        fields = ['phone', 'address', 'city', 'zip_code', 'country']
