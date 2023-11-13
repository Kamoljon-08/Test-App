from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
# from datetime import datetime
# Create your models here.


class Category(models.Model):
    name =  models.CharField(max_length=60, verbose_name="nomi")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
class Test(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="avtor")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="kategoriya")
    title = models.CharField(max_length=250, verbose_name="sarlavha")
    maximum_attemps = models.PositiveIntegerField(verbose_name="maksimum harakatlar soni")
    pass_percentage = models.PositiveIntegerField(default=60)
    start_date = models.DateTimeField(default=timezone.now, verbose_name="boshlanish sanasi")
    end_date = models.DateTimeField(default=(timezone.now()+timezone.timedelta(days=2)), verbose_name="tugash sanasi")

    #questions = > Barcha shu test aloqador bo'lgan question bor

    def __str__(self):
        return str(self.title)
    
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Testlar"
    
#test.questions.all()
class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=400, verbose_name="savol")
    answer_a = models.CharField(max_length=250, verbose_name="a javob")
    answer_b = models.CharField(max_length=250, verbose_name="b javob")
    answer_c = models.CharField(max_length=250, verbose_name="c javob")
    answer_d = models.CharField(max_length=250, verbose_name="d javob")
    true_answer = models.CharField(max_length=250, verbose_name="to'g'ri javob")

    def __str__(self):
        return str(f"Question of {self.test.title}: {self.question}")
    
    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class CheckTest(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="checktests")
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    true_answers = models.PositiveIntegerField(default=0)
    percentage = models.PositiveBigIntegerField(default=0)
    is_passed = models.BooleanField(default=False)

    def __str__(self):
        return f"Ishlangan: {str(self.test.title)}"

class CheckQuestion(models.Model):
    checktest = models.ForeignKey(CheckTest, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    given_answer = models.CharField(max_length=2)
    true_answer = models.CharField(max_length=2)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return str(self.is_true)