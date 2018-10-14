from django import forms
from .models import MultipleChoiceItem, ShortTextItem, LongTextItem

class MultipleChoiceItemForm(forms.ModelForm):
    class Meta:
        model = MultipleChoiceItem
        exclude = ['pub_date']
        verbose_name = "Multiple Choice Item"
        widgets = {
            'rubric': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
        }

class ShortTextItemForm(forms.ModelForm):
    class Meta:
        model = ShortTextItem
        fields = '__all__'
        verbose_name = "Short Response Item"

class LongTextItemForm(forms.ModelForm):
    class Meta:
        model = LongTextItem
        fields = '__all__'
        verbose_name = "Long Response Item"