# email_app/forms.py
from django import forms
from .models import EmailInfo

class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailInfo
        fields = ['to_email', 'company_name', 'purpose', 'message_content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    to_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    purpose = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message_content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 120px;'}))
