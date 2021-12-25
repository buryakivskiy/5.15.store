from django import forms
from .models import FeedBack


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['name', 'phone', 'description', 'call_time', 'email']