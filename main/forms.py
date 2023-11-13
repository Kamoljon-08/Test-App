from django.forms import ModelForm
from .models import Test, Question

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ["title", "category", "maximum_attemps", "start_date", "end_date"]


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["question", "answer_a", "answer_b", "answer_c", "answer_d", "true_answer"]