from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(label='Task text', max_length=160, widget=forms.Textarea)
    percent = forms.FloatField(label='percent', max_value=100, min_value=0)
    date = forms.DateField()


