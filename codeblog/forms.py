from django import forms 
from django.forms import ModelForm
from .models import *
from ckeditor.widgets import CKEditorWidget

class GenreSelect(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ['genre']
		widgets = {
		'genre': forms.Select(attrs={'class': 'form-control'})
		}

class CodeForm(forms.ModelForm):
	class Meta:
		model = Post 
		fields = ('title', 'description', 'importance')
		widgets = {
		   'title': forms.TextInput(attrs={'class': 'form-control'}),
		   'description': forms.Textarea(attrs={'class': 'form-control'}),
		   'importance': forms.Select(attrs={'class': 'form-control'})
		}

class ContentForm(forms.ModelForm):
	class Meta:
		model = Content
		fields = ['heading', 'code']
		widgets = {
		    'heading': forms.TextInput(attrs={'class': 'form-control w-100'}),
		    'code': forms.Textarea(attrs={'class':'form-control'})
		}
