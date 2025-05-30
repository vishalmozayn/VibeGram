from django.forms import ModelForm
from django import forms
from.models import *

class PostCreateForm(ModelForm):
    class Meta:
       model = Post
       fields = ['url' , 'body','tags']
       labels={
           'body': 'Caption',
           'tags':'Category',
       }
       widgets={
           'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption....', 'class': 'font1 text-4xl'}),
           'url' : forms.TextInput(attrs={'placeholder': 'Add url...','class':'font1'}),
           'tags' : forms.CheckboxSelectMultiple(attrs={'placeholder':'Add tags....'}),
       }    
       
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields=['body','url','tags']
        labels={
            'body': 'Caption',
            'tags':'Category'
        }
        widgets={
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url...','class': 'font1'}),
            'tags' : forms.CheckboxSelectMultiple(attrs={'placeholder':'Add tags....'}),
        }
        
class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Add comment....'})
            
        }
        labels = {
            'body' : ''
        }
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder' : 'Add reply...', 'class' : '!text-sm'})
            
        }
        labels = {
            'body' : ''
        }