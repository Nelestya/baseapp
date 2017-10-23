from django import forms
from .models import BugReport

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'mail', 'message']
