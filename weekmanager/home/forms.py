from django import forms

class ActivityForm(forms.Form):
    title = forms.CharField(label='title', max_length=255)
    category = forms.IntegerField(label='category')
    date = forms.IntegerField(label='date')
    fr0m = forms.TimeField()
    to = forms.TimeField()