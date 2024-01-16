from django import forms
from mysite.models import Contact, Subscribe

class ContactFrom(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone_number', 'subject', 'message')

class SubscibeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email', )