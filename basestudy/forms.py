from . models import shop
from django import forms
class updateForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','img','desc','price']