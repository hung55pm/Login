from django import forms


class RegisterForm(forms.Form):
    phone = forms.CharField(label='User', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')
    name = forms.CharField(label='Name')
    birthday = forms.DateTimeField(label="Birthday")


class Login(forms.Form):
    user = forms.CharField(label='User', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)