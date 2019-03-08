from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=250, widget=forms.PasswordInput)
