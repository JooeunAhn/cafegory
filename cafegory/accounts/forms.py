from django import forms
from .models import Comment_to_us

class Comment_to_us_Form(forms.ModelForm):
    class Meta:
        model = Comment_to_us
        fields = ("message",)
