from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        # exclude=['roll']
        labels={
            'name':'Student Name',
            'roll':'Student Roll',
        }
        widgets = {
            'name': forms.TextInput(),
            # 'roll':forms.PasswordInput()
        }
        help_texts ={
            'name':"Write your full Name"
        }
        error_messages={
            'name':{'required':'Your name is required'}
        }
