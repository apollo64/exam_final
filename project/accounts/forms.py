from django import forms

from accounts.models import Account


class UserForm(forms.ModelForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите логин'
        })
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите email'
        })
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )

    def clean(self):
        email = self.cleaned_data.get('email')

        if Account.objects.filter(email=email).exists():
            raise ("Данный Email уже существует")
        return self.cleaned_data

    class Meta:
        model = Account
        fields = ['username', 'email', 'password']
