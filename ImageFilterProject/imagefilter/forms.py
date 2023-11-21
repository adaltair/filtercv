# imagefilter/forms.py
from django import forms

class FilterForm(forms.Form):
    FILTER_CHOICES = [
        ('filter1', 'Blur'),
        ('filter2', 'Contour'),
        ('filter3', 'Sharpen'),
    ]
    filter_option = forms.ChoiceField(choices=FILTER_CHOICES, widget=forms.RadioSelect)
