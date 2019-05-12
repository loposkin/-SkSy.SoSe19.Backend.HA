from django import forms
from .validators.validate_deadline import validate_deadline


class TodoForm(forms.Form):
    text = forms.CharField(label='Task text', max_length=160, widget=forms.Textarea)
    percent = forms.FloatField(label='percent', max_value=100, min_value=0)
    date = forms.DateField(validators=[validate_deadline], error_messages={'invalid': 'Enter a valid value'})


