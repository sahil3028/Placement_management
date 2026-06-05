from django import forms

from companies.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('company_name', 'description', 'location', 'website')
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company name',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Describe the company, culture, and focus areas',
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City, State',
            }),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com',
            }),
        }

    def clean_company_name(self):
        name = self.cleaned_data['company_name'].strip()
        if not name:
            raise forms.ValidationError('Company name is required.')
        return name
