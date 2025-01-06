from django import forms

class UsersForm(forms.Form):
    num1 = forms.CharField(max_length=100)
    num2=forms.CharField(max_length=200)
