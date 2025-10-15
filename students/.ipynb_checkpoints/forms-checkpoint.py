from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    agree_terms = forms.BooleanField(required=True, label="I agree to the terms and conditions")

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'master_average', 'wilaya', 'agree_terms']
