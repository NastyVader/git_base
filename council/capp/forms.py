from django import forms
from django.contrib.auth.models import User
from django.db.models import fields
from .models import UnionForm

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UnionRegisteration(forms.ModelForm):
    class Meta():
        model = (UnionForm)
        fields = '__all__'

