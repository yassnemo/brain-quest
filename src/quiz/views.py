from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        score = 0
        questions = Question.objects.filter(quiz=quiz)
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.answer:
                score += 1
        return render(request, 'quiz/results.html', {
            'quiz': quiz,
            'score': score,
            'total': questions.count()
        })
    return redirect('quiz:quiz_detail', quiz_id=quiz_id)