from django import forms
from .models import MultipleChoiceItem, ShortTextItem

class MultipleChoiceItemForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceItem
        fields = '__all__'
        verbose_name = "Multiple Choice Item"

class ShortTextItemForm(forms.ModelForm):
    class Meta:
        model = ShortTextItem
        fields = '__all__'
        verbose_name = "Short Text Item"