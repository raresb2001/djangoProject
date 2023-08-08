from django.urls import path

from trainer import views

urlpatterns = [
    path('create_trainer/', views.TrainerCreateView.as_view(), name='create_trainer'),
    path('list_trainers/', views.TrainerListView.as_view(), name='list-trainers'),
    path('update_trainer/<int:pk>', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='delete-trainer'),
    path('details_trainer/<int:pk>/', views.TrainerDetailView.as_view(), name='details-trainer'),
    path('delete_modal_trainer/<int:pk>/', views.delete_modal_trainer, name='delete-modal-trainer'),
    path('get_student/<int:pk>/', views.get_students_trainer, name='get-students'),
]