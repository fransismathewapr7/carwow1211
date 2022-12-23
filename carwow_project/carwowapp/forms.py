from django import forms
from .models import Cars

class Carsform(forms.ModelForm):
    class Meta:
        model=Cars
        fields=['name','desc','price','img']