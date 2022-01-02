from django import forms

from .models import dataModel

class dataForm(forms.ModelForm):
	class Meta:
		model=dataModel
		fields=["title","description",]
