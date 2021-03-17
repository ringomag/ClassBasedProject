from django.forms import ModelForm
from .models import Lik
from django import forms

class LikForm(ModelForm):
    class Meta:
        model = Lik
        fields = [
            'firstname',
            'lastname',
        ]
        widgets = {
            'firstname': forms.TextInput(attrs={'class':'blue_letters', 'placeholder': 'Firstname'}),
            'lastname': forms.TextInput(attrs={'class':'red_letters', 'placeholder': 'Lastname'}),
        }
        #Labele nece da rade odavde....
        # labels = {
        #     'firstname': "Enter your name",
        #     'lastname': "Enter your lastname",
        # }
