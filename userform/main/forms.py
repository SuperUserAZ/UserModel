from .models import userData
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput

class userDataForm(ModelForm):
    class Meta:
        model = userData
        fields = ['user_name', 'user_last_name', 'user_email', 'user_password']
        widgets = {
            'user_name': TextInput(attrs={
                'class': 'signup-form__input',
                'placeholder': 'Name'
            }),
            'user_last_name': TextInput(attrs={
                'class': 'signup-form__input',
                'placeholder': 'Last Name'
            }),
            'user_email': EmailInput(attrs={
                'class': 'signup-form__input',
                'placeholder': 'Email'
            }),
            'user_password': PasswordInput(attrs={
                'class': 'signup-form__input',
                'placeholder': 'Password'
            }),
        }
