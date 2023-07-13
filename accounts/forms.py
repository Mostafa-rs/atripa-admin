from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm password')

    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        cd = super().clean()
        passwd1 = cd.get('password1')
        passwd2 = cd.get('password2')

        if passwd1 and passwd2 and passwd1 != passwd2:
            raise ValidationError('Passwords must match')
        elif len(passwd2) < 8:
            raise ValidationError('Password must be at least 8 characters')
        elif not any(i.isalpha() for i in passwd2):
            raise ValidationError('Password must contain at least 1 letter')
        elif not any(i.isupper() for i in passwd2):
            raise ValidationError('Password mus contain at least 1 UpperCase')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=
                                         'You can change your password using <a href="../password/">this link</a>')

    class Meta:
        model = User
        fields = '__all__'

