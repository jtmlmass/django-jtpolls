from django.contrib import admin
from .models import Question, Choice

#Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

#Question
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_per_page = 25
    fieldsets = [
        ('Information',               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

# Register your models here.
admin.site.register(Question, QuestionAdmin)
