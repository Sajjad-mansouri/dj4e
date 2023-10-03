from django import forms
from .models import Auto,Make
class AutoForm(forms.ModelForm):
	class Meta:
		model=Auto
		fields='__all__'

class MakeForm(forms.ModelForm):
	class Meta:
		model=Make
		fields='__all__'