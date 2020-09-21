from django import forms

from .models import Applypdf

class ApplyForm(forms.ModelForm):

    class Meta:
        model = Applypdf
        fields = ['apply']
