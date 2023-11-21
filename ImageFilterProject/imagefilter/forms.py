from django import forms

class FilterForm(forms.Form):
    FILTER_CHOICES = [
        ('gray', 'Grayscale'),
        ('blur', 'Blur'),
        ('edge', 'Edge'),
        ('sharpen', 'Sharpen'),
        ('emboss', 'Emboss'),
    ]
    filter_option = forms.ChoiceField(choices=FILTER_CHOICES, widget=forms.RadioSelect)
