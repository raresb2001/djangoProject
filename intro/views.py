from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required()
def index(request):
    return HttpResponse('<h1>Hello World</h1>')

@login_required()
def name(request):
    return HttpResponse('Anita')

@login_required()
def cars(request):
    context = {
        'cars': [
            {
                'brand': 'Dacia',
                'model': 'Duster',
                'year': 2023
            },
            {
                'brand': 'Audi',
                'model': 'A1',
                'year': 2022
            },
            {
                'brand': 'Toyota',
                'model': 'RAV4',
                'year': 2021
            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)

@login_required()
def movies(request):
    context = {
        'movies': [
            {
                'name': 'Avatar The Way of Water',
                'type': 'Action',
                'year': 2022,
                'rating': 10
            },
            {
                'name': 'Oppenheimer',
                'type': 'Drama',
                'year': 2023,
                'rating': 10
            },
            {
                'name': 'Black Panther',
                'type': 'Action',
                'year': 2018,
                'rating': 10
            }
        ]
    }
    return render(request, 'intro/list_of_movies.html', context)
