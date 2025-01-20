from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create sample quiz
        quiz = Quiz.objects.create(
            title="Python Basics",
            description="Test your Python knowledge"
        )
        
        # Create sample questions
        Question.objects.create(
            quiz=quiz,
            question_text="What is Python?",
            answer="A programming language"
        )