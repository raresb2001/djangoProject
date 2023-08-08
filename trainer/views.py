from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.models import Student
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


# Create your views here.

class TrainerCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name = 'trainer/create_trainer.html'  # calea catre fisierul html unde va fi generat formularul
    model = Trainer  # formularul din html se va genera pe baza modelului(clasa din models.py)
    form_class = TrainerForm
    success_url = reverse_lazy('list-trainers')  # dupa ce dom accesa butonul de save, utilizatorul va fi redirectionat pe pagina mentionat
    success_message = 'Felicitari. Trainerul cu numele {t_name} {s_name} a fost creat cu success'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(t_name=self.object.first_name, s_name=self.object.last_name)


class TrainerListView(LoginRequiredMixin,ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'all_trainers'  # numele variabilei de context (Student.objects.all())

    def get_queryset(self):
        return Trainer.objects.filter(active=True)

class TrainerUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'trainer/update_trainer.html'
    model = Trainer
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list-trainers')


class TrainerDeleteView(LoginRequiredMixin,DeleteView):
    template_name = 'trainer/delete-trainer.html'
    model = Trainer
    success_url = reverse_lazy('list-trainers')

class TrainerDetailView(LoginRequiredMixin,DetailView):
    template_name = 'trainer/details_trainer.html'
    model = Trainer

@login_required()
def delete_modal_trainer(request, pk):
    Trainer.objects.filter(id=pk).delete() #Query
    return redirect('list-trainers')

def get_students_trainer(request, pk):
    get_students = Student.objects.filter(trainer_id=pk)

    return render(request, 'student/list_of_students.html', {'all_students': get_students})
