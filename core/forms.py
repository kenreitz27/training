from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from core.models import Profile

class SignUpForm(UserCreationForm):
  first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
  last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
  email = forms.EmailField(max_length=254, help_text='Valid Email Address Required')
  birth_date = forms.DateField(
    help_text='Required',
    widget=forms.widgets.DateTimeInput(
      attrs={"type": "date"}
    )
  )
  
  
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'birth_date', 'password1', 'password2')
    
class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('first_name', 'last_name', 'email')
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ('birth_date', 'ghin', 'phone')
    
    