from django import forms
from django.forms import Textarea

from .models import Registration
from crispy_forms.helper import FormHelper


# Create your forms here.
class RegistrationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()

        # self.helper.layout = Layout(
        #     'first_name',
        #     Fieldset('last_name', css_class='hello'),
        #     Fieldset('email', css_class='hello')
        # )




    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'first_name': Textarea(attrs={'rows': 1}),
            'last_name':Textarea(attrs={'rows': 1}),
            'field_of_study': Textarea(attrs={'rows': 1}),
        }

        # error_messages = {
        #     'resume': {
        #         'Only pdf is supported': ("Only pdf is supported"),
        #     },
        # }


