from django.contrib.auth.models import User
from django.db import models

from trainer.models import Trainer


# Create your models here.


class Student(models.Model):

    gender_options = (
        ('male', 'Male'),
        ('female', 'Female')
    )

    #('valoarea salvata in tabela,' 'valoarea afisata in interfata')

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to='student_profiles/', null=True, blank=True)
    # file = models.FileField(upload_to='student_files', null=True)

    created_at = models.DateTimeField(auto_now_add=True) #salveaza data si ora cand a fost creat un student , nu se mai modifica data si ora never.
    updated_at = models.DateTimeField(auto_now=True) #salveaza data si ora cand se realizeaza modificari pe sudentul respectiv


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#Putem sterge tabela pe baza unei migrari(prima data comentam si  dupa facem migrations)- NU FACEM CU DROP DATABASE



