from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import UserDetails


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
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
