from django import forms
from .models import Video

class ViedoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

