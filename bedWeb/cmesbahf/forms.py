from django import forms
from django.core import validators
from django.core.validators import FileExtensionValidator



validate_file = FileExtensionValidator(allowed_extensions=['csv'],
                                        message='Wrong File Format',
                                        code='200')

class uploader(forms.Form):
    description_name = forms.CharField(max_length=50)
    #task = forms.ChoiceField(choices = oneFileTasks)
    fileOne = forms.FileField(validators=[validate_file])
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])


