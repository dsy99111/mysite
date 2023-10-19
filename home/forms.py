from django import forms
class SignupForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    mobile=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

