from django.contrib import admin
from .models import Quiz, Question, UserScore

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'quiz', 'answer')
    list_filter = ('quiz',)

@admin.register(UserScore)
class UserScoreAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'quiz', 'score', 'completed_at')
    list_filter = ('quiz',)