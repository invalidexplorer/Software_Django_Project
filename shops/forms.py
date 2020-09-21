from django import forms

from .models import ProductReport

class ProductReportForm(forms.ModelForm):

    class Meta:
        model = ProductReport
        fields = ['reason']