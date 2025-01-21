from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Answer

def index(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/index.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if 'questions' not in request.session:
        questions = [q.id for q in quiz.get_random_questions()]
        request.session['questions'] = questions
        request.session['current_question'] = 0
        request.session['score'] = 0
    
    current_q_index = request.session['current_question']
    if current_q_index >= len(request.session['questions']):
        return redirect('quiz:quiz_complete', quiz_id=quiz_id)
    
    question = Question.objects.get(pk=request.session['questions'][current_q_index])
    answers = Answer.objects.filter(question=question)
    
    return render(request, 'quiz/quiz.html', {
        'quiz': quiz,
        'question': question,
        'answers': answers,
        'progress': f"Question {current_q_index + 1} of {len(request.session['questions'])}"
    })

def submit_answer(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        answer_id = request.POST.get('answer')
        if answer_id:
            answer = Answer.objects.get(pk=answer_id)
            if answer.is_correct:
                request.session['score'] = request.session.get('score', 0) + 1
        
        request.session['current_question'] = request.session.get('current_question', 0) + 1
        return redirect('quiz:quiz_detail', quiz_id=quiz_id)

def quiz_complete(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    score = request.session.get('score', 0)
    total = len(request.session.get('questions', []))
    
    # Clear session data
    if 'questions' in request.session:
        del request.session['questions']
        del request.session['current_question']
        del request.session['score']
    
    return render(request, 'quiz/results.html', {
        'quiz': quiz,
        'score': score,
        'total': total
    })