from django import forms
from app.models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        widgets = {'password':forms.PasswordInput}
        help_texts = {'username':'required charcters,digits'}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_name','address','profile_pic']


