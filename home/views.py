from django.shortcuts import render
from django.views.generic import TemplateView


# TemplateView -> este o clasa de baza generica care poate fi utilizata pentru a afisa o pagina html intr-o aplicatie web


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html' # specificam numele template-ului html utilizat pentru afisare
