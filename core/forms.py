from django import forms

from core.models import Leave

class DateInput(forms.DateInput):
    input_type = 'date'


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields =[
            'staff',
            'start_date',
            'end_date',
            'leave_type'
        ]
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
    