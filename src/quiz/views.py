from django.shortcuts import render, get_object_or_404
from .models import Quiz

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quiz/quiz.html', {'quiz': quiz})

def submit_quiz(request, quiz_id):
    if request.method == 'POST':
        score = 0
        quiz = Quiz.objects.get(id=quiz_id)
        questions = Question.objects.filter(quiz=quiz)
        
        for question in questions:
            user_answer = request.POST.get(str(question.id))
            if user_answer == question.correct_answer:
                score += 1
        
        Score.objects.create(quiz=quiz, score=score)
        return render(request, 'quiz/results.html', {'score': score, 'quiz': quiz})

    return JsonResponse({'error': 'Invalid request'}, status=400)