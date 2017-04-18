from django import forms
from bartleby.models import *

class RecordForm(forms.ModelForm):
    class Meta:
        model = RecordForm
        fields = [ 'file_name']
        widgets = {
                'file_name': forms.TextInput(attrs={'placeholder': 'File Name'}),
        }
