from django import forms
from .models import Policy

class PolicyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = ['policy_number', 'holder_name', 'policy_type', 'issue_date', 'is_active']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}), # برای باز شدن تقویم
        }