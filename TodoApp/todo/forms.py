from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'due_date', 'due_time','description','remind_minutes']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows':
            4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', onclick="location.reload();"))
        self.helper.layout = Layout(
            Row(
                Column('name'),
                Column('due_time'),
                Column('due_date'),
                Column('description'),
                Column('completed'),
                Column('remind_minutes'),
                css_class='form-row'
            ),
        )