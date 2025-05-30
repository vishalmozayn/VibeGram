from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import*
    
class ProfileForm(ModelForm):
    
    class Meta:
        model=Profile
        exclude=['user']
        labels= {
            'realname' : 'Name'
        }
        widgets ={
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows':3})
        }
        
        
class UsernameForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
        
class EmailForm(ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email']