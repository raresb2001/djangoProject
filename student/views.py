from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.forms import StudentForm, StudentUpdateForm
from student.models import Student
from userextend.models import History


# Create your views here.

# CreateView -> este o clasa generica in Django utilizata pentru a crea un obiect intr-o baza de date folosinf un formular
# PermissionRequiredMixin -> functionalitate dez. de Django pentru a verifica daca userul
# logat are dreptul sa acceseze actiunea respectiva
#Daca userul NU are dreptul sa acceseze actiunea ii va afisa in interfata un template 403 (HTTP STATUS)

class StudentCreateView(LoginRequiredMixin,PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'  # calea catre fisierul html unde va fi generat formularul pentru a scrie codul html
    model = Student  # formularul din html se va genera pe baza modelului(clasa din models.py)
    form_class = StudentForm
    success_url = reverse_lazy('list-students')  # dupa ce vom accesa butonul de save, utilizatorul va fi redirectionat pe pagina mentionat
    success_message = 'Felicitari. Studentul cu numele {f_name} {l_name} a adaugat cu success'
    permission_required = 'student.add_student'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(f_name=self.object.first_name, l_name = self.object.last_name)


    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save()
            message = f'Creat student nou {new_student.first_name} {new_student.last_name}'
            user = self.request.user.id
            created_at = datetime.now()
            History.objects.create(message=message, user_id=user, created_at=created_at)

        return redirect('list-students')


# ListView -> este o clasa generica in Django utilizate pentru a afisa datele dintr-o tabela

class StudentListView(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students' # numele variabilei de context (Student.objects.all())
    permission_required = 'student.view_list_of_students'

    # metoda get_queryset este o metofa folosita in clase de baza pentru a obtine si returna setul de obiecte(python)
    # care va fi folosit pentru afisare

    def get_queryset(self):
        return Student.objects.filter(active=True)

# SuccessMessageMixin este o clasa care furnizeaza functionalitatea unui mesaj dupa o actiune
# ce a fost realizata cu success.


# UpdateView este o clasa de baza in Django folosiita pentru a afisa o forma pre-populata cu datele unui obiect
# Ii permite utilizatorului sa editeze datele si sa le salveze in baza date


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-students')
    permission_required = 'student.change_student'


# DeleteView este o clasa utilizata pentru a afisa o pagina de confirmare
# si pentru a sterge un obiect existent din baza de date

class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete-student.html'
    model = Student
    success_url = reverse_lazy('list-students')
    permission_required = 'student.delete_student'

# DetailView este o clasa in Django pentru a afisa detaliile unui singur obiect dintr-un model
class StudentDetailView(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


@login_required()
@permission_required('student.delete_student')
def delete_modal_student(request, pk):
    Student.objects.filter(id=pk).delete() #Query
    return redirect('list-students')
