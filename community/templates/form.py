from django import forms
from ..models import Board

class Boardupdate(forms.ModelForm):
    class Meta:
        model = Board
        fields=['contents','file']

class DocumentForm(forms.ModelForm):
    upload = forms.FileField(label='첨부 파일', required=False, 
          widget=forms.FileInput(attrs={'class': 'form'}))
    
    class Meta:
        model = Board
        exclude = ['attached']