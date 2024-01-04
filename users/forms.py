from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        first_name = forms.CharField(label="First Name", required=True)
        last_name = forms.CharField(label="Last Name", required=True)
        phone_number = forms.CharField(label="Phone Number", required=True)
        email = forms.EmailField(label="Email address", required=True)

        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "phone_number", "password1", "password2")

