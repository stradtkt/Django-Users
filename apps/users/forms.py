from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Your Password"}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your First Name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Last Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Your Email"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Your Username"}))
    image = forms.ImageField(widget=forms.ImageField())
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Your Password"}))
    confirm_pass = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Your Password Confirm"}))