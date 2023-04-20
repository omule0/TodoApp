from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class TodoForm(forms.Form):
    itemContent = forms.CharField(label='Todo item')
    expiry = forms.DateTimeField(label='Expiry date and time', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            'itemContent',
            'expiry',
            Submit('submit', 'Create')
        )