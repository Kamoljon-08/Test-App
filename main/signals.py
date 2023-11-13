from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from .models import CheckTest, CheckQuestion


# pre_save()
# save()
# post_save()

@receiver(pre_save, sender=CheckTest)
def calculate_test(sender, instance, *args, **kwargs):
    questions = CheckQuestion.objects.filter(checktest=instance)

    number_of_question = questions.count()
    number_of_true_answers = questions.filter(is_true=True).count()
    try:
        percetage = number_of_true_answers / number_of_question * 100
    except:
        percetage = 0
    
    instance.true_answers = number_of_true_answers
    instance.percentage = percetage
    if instance.test.pass_percentage < percetage:
        instance.is_passed = True


@receiver(pre_save, sender=CheckQuestion)
def checkquestion(sender, instance, *args, **kwargs):
    if instance.given_answer == instance.true_answer:
        instance.is_true = True
    else:
        instance.is_true = False