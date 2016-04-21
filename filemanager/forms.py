from django import forms
from models import Files


class FileUploadForm(forms.ModelForm):

	class Meta:
		model = Files
		fields = ('file_name', 'file')

		widgets = {
			'file_name': forms.TextInput(
				attrs={'class': 'form-control', 'autofocus': 'autofocus', 'placeholder': 'File name'})
		}