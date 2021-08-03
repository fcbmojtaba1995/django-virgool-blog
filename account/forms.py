from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
    )
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
    )


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your username'})
    )
    email = forms.EmailField(
        max_length=50, required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email(optional)'})
    )
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'})
    )
    confirm_password = forms.CharField(
        label='confirm password', max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.exclude(email__exact='').filter(email=email)
        if user.exists():
            raise forms.ValidationError('This email address already exists')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password must match')


class UserEditProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=50, required=False)

    class Meta:
        model = Profile
        fields = (
            'username', 'first_name', 'last_name', 'email',
            'phone_number', 'bio', 'avatar', 'date_of_birth', 'gender',
        )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'placeholder': 'Select a date'}),
        }

