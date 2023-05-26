from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django import forms
from .models import Task, List

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
                Column('remind_minutes'),
                css_class='form-row'
            ),
        )



class ListForm(forms.ModelForm):
    class Meta:
        DAY_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]
        model = List
        fields = ["item","due_time","due_week", "week_of"]
        widgets = {
            'item': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task here'}),
            'due_time': forms.TimeInput(attrs={'type': 'time'}),
            'due_week': forms.DateInput(attrs={'type': 'date'}),
            'week_of': forms.Select(choices=DAY_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(ListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit', onclick="location.reload();"))
        self.helper.layout = Layout(
            Column(
                Column('item'),
                Column('due_time'),
                Column('due_week'),
                Column('week_of'),
                css_class='form-row'
            ),
        )

