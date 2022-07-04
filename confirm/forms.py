from django import forms
from .models import Reservation

# class ConfirmForm(forms.Form):
#     CHOICES = (
#         ('Yes', 'Yes'),
#         ('No', 'No'))
#     choice = forms.ChoiceField(choices = CHOICES)
#     first_name = forms.CharField(max_length=12, min_length=1, error_messages={
#         'min_length': "Specify at least one character",
#         "max_length": 'Too many characters',
#         'required': 'Guest name is required!'
#     })
#     last_name = forms.CharField(error_messages={'required': 'Guest last name is required!'})
#     email = forms.EmailField(error_messages={'required': 'Guest e-mail is required!'})
#     feedback = forms.CharField(required=False, label='Anything else we should know?',
#                                widget=forms.Textarea(attrs={'rows':2, 'cols':20}))

class ConfirmForm(forms.ModelForm):
    class Meta:
        model = Reservation
        # fields = ['choice','first_name','last_name','email','feedback']
        fields = '__all__'
        labels = {
            'choice': 'Will you be attending?',
            'add_person': 'Are you bringing a +1? (if yes, please write their name below.)',
            'feedback': 'Anything else we should know (allergies, dietary requirements, secrets...)?'                        ''
        }
        error_messages = {
            'first_name': {
                'max_length': 'Too many characters',
                'min_length': "Specify at least one character",
                'required': 'Guest name is required!'

            },
            'last_name': {
                'max_length': 'Too many characters',
                'min_length': "Specify at least one character",
                'required': 'Guest name is required!'
            }
        }

