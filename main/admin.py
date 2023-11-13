from django.contrib import admin
from .models import Category, Test, Question, CheckQuestion, CheckTest
# Register your models here.

class InlineQuestion(admin.TabularInline):
    model = Question

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    model = Test
    list_display = ["title", "author", "category", "maximum_attemps", "start_date", "end_date"]
    inlines = [InlineQuestion]
    search_fields  = ["title", "category__name"]
    list_filter = ["start_date"]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ["test","question", "true_answer"]

admin.site.register([Category, CheckTest, CheckQuestion])
