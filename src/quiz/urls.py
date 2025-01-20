from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
]