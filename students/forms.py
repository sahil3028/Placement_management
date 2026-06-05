from django import forms

from students.models import StudentProfile


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
            'full_name',
            'college_name',
            'branch',
            'graduation_year',
            'cgpa',
            'phone_number',
            'skills',
            'github_url',
            'linkedin_url',
            'resume',
        ]

        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'college_name': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'branch': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'graduation_year': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),
            'cgpa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01',
                }
            ),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'skills': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                }
            ),
            'github_url': forms.URLInput(
                attrs={'class': 'form-control'}
            ),
            'linkedin_url': forms.URLInput(
                attrs={'class': 'form-control'}
            ),
            'resume': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }