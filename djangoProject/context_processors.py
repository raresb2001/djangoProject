from trainer.models import Trainer


def get_all_trainers(request):
    return { 'trainers' : Trainer.objects.filter(active=True) }

# Step1: Am adaugat un fisier nou.py numit context_processors in folderul djangoProject
# Step2: In fisierul context_processors.py am adaugat o functie noua get_all_trainers
# Step3: In fisierul settings.py, am adaugat in lista context_processors(Templates) -> calea catre functie
# Step4: Am adaugat in fisierul navbar.html codul pentru a adauga lista cu trainerii.

