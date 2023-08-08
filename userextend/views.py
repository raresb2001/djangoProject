from datetime import datetime
from random import random, randint

from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from student.models import Student
from userextend.forms import UserForm
from userextend.models import History


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)  # oprim salvarea datelor pentru ca urmeaza sa le modificam
            new_user.first_name = new_user.first_name.upper()
            new_user.last_name = new_user.last_name.upper()
            # atribui valoarea new_user.first_name.upper() campului first_name al obiectului new_user
            # new_user.username = new_user.first_name[0] + new_user.last_name + str(randint(0,5))
            new_user.username = f'{new_user.first_name[0].lower()}{new_user.last_name.lower().replace(" ", "")}_{randint(100000, 999999)}'

            subject = 'Cont nou in aplicatie!'
            message = f"Felicitari. Ai un cont nou in aplicatie. Username este: {new_user.username}"
            send_mail(subject, message, DEFAULT_FROM_EMAIL, [new_user.email])

            new_user.save()

            # Istoric
            message = (f"first_name: {new_user.first_name}, last_name {new_user.last_name}",
                       f"email: {new_user.email}, username: {new_user.username}")

            user = new_user.id
            created_at = datetime.now()
            History.objects.create(message=message, user_id=user, created_at=created_at)


        return redirect('login')
