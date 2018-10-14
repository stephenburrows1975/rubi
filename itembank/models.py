from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CEFRLevel(models.Model):
    cefr_level = models.CharField(max_length=2)
    descripion = models.CharField(max_length=1000)
    def __str__(self):
        return self.cefr_level

class SkillSystem(models.Model):
    name = models.CharField(max_length=20)
    skill = models.BooleanField(default=False)
    system = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class MultipleChoiceItem(models.Model):
    OPTION_ANSWER = (
        ('1', 'Option 1'),
        ('2', 'Option 2'),
        ('3', 'Option 3')
    )
    rubric = models.CharField(max_length=250)
    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    answer = models.CharField(max_length=1, choices=OPTION_ANSWER)
    level = models.ForeignKey(CEFRLevel, on_delete=models.CASCADE)
    language = models.ForeignKey(SkillSystem, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.rubric

class ShortTextItem(models.Model):
    rubric = models.CharField(max_length=400)
    word_limit = models.IntegerField(
        default=10,
        validators=[MaxValueValidator(250), MinValueValidator(10)])
    level = models.ForeignKey(CEFRLevel, on_delete=models.CASCADE)
    language = models.ForeignKey(SkillSystem, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.rubric


class LongTextItem(models.Model):
    rubric = models.CharField(max_length=400)
    word_limit = models.IntegerField(
        default=250,
        validators=[MaxValueValidator(2500), MinValueValidator(10)])
    level = models.ForeignKey(CEFRLevel, on_delete=models.CASCADE)
    language = models.ForeignKey(SkillSystem, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.rubric