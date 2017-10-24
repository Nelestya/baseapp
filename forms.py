from django import forms
from .models import BugReport, ContactUs

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'mail', 'message']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'mail', 'message']
