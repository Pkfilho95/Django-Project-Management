from django import forms
from django.contrib.auth.models import User

from .functions import password_requirements
from .models import Position

class RegisterUserForm(forms.Form):
    first_name = forms.CharField(max_length=70)
    last_name = forms.CharField(max_length=70)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(min_length=8, max_length=150)
    confirm_password = forms.CharField(min_length=8, max_length=150)
    position = forms.ModelChoiceField(queryset=Position.objects.all())

    def clean(self):
        cleaned_data = super(RegisterUserForm, self).clean()

        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError('User already exists!', code='invalid')
        
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('E-mail already exists!', code='invalid')
        
        if password and confirm_password:

            password_error = password_requirements(password)

            if password_error:
                raise forms.ValidationError(password_error)

            if password != confirm_password:
                raise forms.ValidationError('Differents passwords', code='invalid')
        
        return cleaned_data
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class RegisterPositionForm(forms.Form):
    position = forms.CharField(max_length=150)

    class Meta:
        model = Position
        fields = '__all__'