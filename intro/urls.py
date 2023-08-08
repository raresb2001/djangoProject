from django.urls import path

from intro import views

urlpatterns = [
    path('hello/', views.index, name="get_hello"),
    path('show_name/', views.name, name="show-name"),
    path('list-cars/', views.cars, name='list_cars'),
    path('list-movies/', views.movies, name='list_movies'),
]


# path('prefix', functia/clasa, name='nume-url')
# Prefix UNIC
# in variabila NAME = ..., va fi UNIC