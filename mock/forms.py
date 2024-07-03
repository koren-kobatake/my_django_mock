# mock/forms.py

from django import forms

class LoginForm(forms.Form):
    userId = forms.CharField(label='User ID', max_length=100)
    cic = forms.CharField(label='CIC', max_length=100)
