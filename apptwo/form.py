from django import forms
from apptwo.models import user

class newuser(forms.ModelForm):
    class Meta:
        model = user
        fields = '__all__'