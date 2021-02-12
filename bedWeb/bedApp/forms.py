from django import forms
from django.core import validators
from django.core.validators import FileExtensionValidator


twoFilesTasks= [('subtract','subtract'),
('intersect','intersect')]

oneFileTasks = [('merge','merge'),
('sort','sort')]

validate_file = FileExtensionValidator(allowed_extensions=['bed'],
                                        message='Wrong File Format',
                                        code='200')

class uploaderTwo(forms.Form):
    description_name = forms.CharField(max_length=50)
    task = forms.ChoiceField(choices = twoFilesTasks)
    fileOne = forms.FileField(validators=[validate_file])
    fileTwo = forms.FileField(validators=[validate_file])
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])
        
    
    
class uploaderOne(forms.Form):
    description_name = forms.CharField(max_length=50)
    task = forms.ChoiceField(choices = oneFileTasks)
    fileOne = forms.FileField(validators=[validate_file])
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])


