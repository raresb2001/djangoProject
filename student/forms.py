from django import forms
from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student

#formularul de create
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  # definim campurile din formualr, pe care le dorim
        fields = ['first_name', 'last_name', 'age', 'email', 'description', 'start_date', 'end_date', 'gender', 'trainer','profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        # unicitatea pe adresa de email
        get_email = cleaned_data['email']  # cleaned_data.get('email')
        check_emails = Student.objects.filter(email=get_email)
        if check_emails:
            msg = "Exista un student cu aceasta adresa de mail"
            self._errors['email'] = self.error_class([msg])

        # validare pe campul start_date (daca start_date este mai mare decat end_date sa genereze of eroare)
        if cleaned_data['start_date'] > cleaned_data['end_date']:
            msg = "Start date este mai mare decat end date"
            self._errors["start_date"] = self.error_class([msg])

        return cleaned_data



    # Metoda clean() este o metoda specifica in Django pentru a valida si curata datele introduse in formular inainte
    # de a fi salvate

    # Atunci cand se apeleaza metoda clean() Django va executa validarile implicite pentru fiecare camp al formularului.
# Class Meta intr-un fisier forms.py intr-un Django este folosita
# pentru a defini metadele asociate cu un formular

# Aceste metadate includ informatii despre modelul alocat formularului,
#campurile care trebuie sa aparat in formular si vor exista
#alte optiuni specifice

# update form
class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  # definim campurile din formualr, pe care le dorim
        fields = ['first_name', 'last_name', 'age', 'email', 'description', 'start_date', 'end_date', 'gender', 'trainer','profile']

        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your last name'}),
            'age': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your age'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter your email'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class': 'form-select'}),
        }

