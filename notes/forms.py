from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'text']
        labels = {
            'title': 'Note Title',
            'text': 'Write your thouhts here',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control my-5'}
                ),
            'text': forms.Textarea(attrs={
                'class': 'form-control mb5',
            })
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'Django' not in title:
            raise ValidationError("Title must contain 'Django'.")
        return title