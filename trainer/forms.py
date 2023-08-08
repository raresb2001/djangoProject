from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from trainer.models import Trainer


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields = '__all__'  # definim campurile din formualr, pe care le dorim
        fields = ['first_name', 'last_name', 'email', 'course' , 'department','profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your departement'})
        }

class TrainerUpdateForm(forms.ModelForm):
    class Meta:
        model = Trainer
        # fields = '__all__'  # definim campurile din formualr, pe care le dorim
        fields = ['first_name', 'last_name', 'email', 'course' , 'department','profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'course': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'department': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your departement'})
        }
