from cProfile import label
from django import forms
from django.core import validators
from django.core.exceptions  import ValidationError
from first_app.models import UserProfileInfo,User_name
from django.contrib.auth.models import User


def check_with_z(value):
    if not value.lower().startswith('z'):
        raise forms.ValidationError('Not starts with z')

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data.get('email')
        print(email)
        vmail = all_clean_data.get('verify_email')
        print(vmail)
        if email != vmail:
            print("Warning: Email Mismatch")
            raise forms.ValidationError('MAKE SURE EMAILS MATCH!')

class Userf(forms.ModelForm):
    class Meta():
        model = User_name
        fields = '__all__'
        labels = {'email': 'Enter your email address','first_name': 'Enter your first name','last_name': 'Enter your last name'}


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ['username', 'email', 'password']

class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ['profile_site', 'profile_pic']





