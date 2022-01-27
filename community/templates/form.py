from django import forms
from ..models import Board

class Boardupdate(forms.ModelForm):
    class Meta:
        model = Board
        fields=['contents','file']