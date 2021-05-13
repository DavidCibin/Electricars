from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


from django.forms import ModelForm
from .models import Booking


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2',)



class BookingForm(ModelForm):
  class Meta:
    model = Booking
    fields = ['insurance', 'start_date', 'end_date', 'total']
    widgets = {
        'start_date': forms.TextInput(attrs={'readonly': 'readonly','class':'pudate'}),
        'end_date': forms.TextInput(attrs={'readonly': 'readonly','class':'dodate'}),
        'total': forms.TextInput(attrs={'readonly': 'readonly'}),
    }

class ProfileForm(ModelForm):
  class Meta:
    model = Profile
    fields = ['phone', 'address1', 'city', 'state', 'zipcode']    

