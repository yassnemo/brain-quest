from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.submit_answer, name='submit_answer'),
    path('quiz/<int:quiz_id>/complete/', views.quiz_complete, name='quiz_complete'),
]